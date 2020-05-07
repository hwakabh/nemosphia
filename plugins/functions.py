# coding: utf-8
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

import os
import time
import subprocess
import json
from .pkg.vSphere import VcEndpoint
from .pkg.vSphere import VirtualMachine

# Get vSphere credentials securely from environmental variables
VC_IPADDR = os.environ.get('VSPHERE_IP')
VC_USERNAME = os.environ.get('VSPHERE_USERNAME')
VC_PASSWORD = os.environ.get('VSPHERE_PASSWORD')

vcapi = VcEndpoint(
    ip=VC_IPADDR,
    user=VC_USERNAME,
    passwd=VC_PASSWORD
)

# ---- CRUD Implementation with vSphere RESTful-API
def create_virtual_machine(vmname, vmspec):
    uriprefix = '/vcenter/vm'
    
    with open('./plugins/specs/CentOS-7-{0}.json'.format(vmspec)) as f:
        spec_json = json.load(f) 
    # add vmname to JSON post data
    spec_json['spec']['name'] = vmname

    response = vcapi.https_post(uriprefix=uriprefix, data=spec_json)
    return json.loads(response)


def get_vm_list():
    uriprefix = '/vcenter/vm'
    response = vcapi.https_get(uriprefix=uriprefix)
    return response


def get_network():
    uriprefix = '/vcenter/network'
    response = vcapi.https_get(uriprefix=uriprefix)
    return response


def get_vm_id(vmname):
    response = get_vm_list()
    for vm in response['value']:
        if vm['name'] == vmname:
            return vm['vm']


def find_network_id(netname):
    response = get_network()
    for net in response['value']:
        if net['name'] == netname:
            return net['network']

def destroy_vm(vmid):
    uriprefix = '/vcenter/vm/{}'.format(vmid)
    response = vcapi.https_delete(uriprefix=uriprefix, data={})
    return response


# ---- Functions for Slackbot use 
@respond_to(r'^getvminfo\.*')
def get_vm_info(message):
    if message.body['text'].split()[0]  == 'getvminfo':
        options = message.body['text'].split()[1:]
        if len(options) == 0:
            message.reply('No VM name provided, nothing to do.')
        elif len(options) == 1:
            vmname = options[0]
            message.reply('Sure, checking information of VM ... ')
            time.sleep(3)
            message.reply('The basic information of VM [ {} ]'.format(vmname))

            vms = get_vm_list()
            is_found = False
            vm_found = {}
            for vm in vms['value']:
                if vm['name'] == vmname:
                    is_found = True
                    vm_found = vm
                else:
                    pass
            if is_found:
                vm_info = '```'
                for k, v in vm_found.items():
                    vm_info += '{0} : {1} \n'.format(k, v)
                vm_info += '```'
                message.send(vm_info)
            else:
                message.send('Sorry. No VM found whose name is [ {} ]'.format(vmname))

        else:
            message.reply('Too many options provides. Check usage.')
            show_usage(message)
    else:
        message.reply('Do you mean `getvminfo` ??')


@respond_to(r'^getnetinfo\.*')
def get_net_info(message):
    if message.body['text'].split()[0]  == 'getnetinfo':
        options = message.body['text'].split()[1:]
        if len(options) == 0:
            message.reply('No network name provided, nothing to do.')
        elif len(options) == 1:
            netname = options[0]
            message.reply('Sure, checking information of virtual network ... ')
            time.sleep(3)
            message.reply('The basic information of virtual network [ {} ]'.format(netname))

            networks = get_network()
            is_found = False
            net_found = {}
            for network in networks['value']:
                if network['name'] == netname:
                    is_found = True
                    net_found = network 
                else:
                    pass
            if is_found:
                net_info = '```'
                for k, v in net_found.items():
                    net_info += '{0} : {1} \n'.format(k, v)
                net_info += '```'
                message.send(net_info)
            else:
                message.send('Sorry. No network found whose name is [ {} ]'.format(netname))

        else:
            message.reply('Too many options provides. Check usage.')
            show_usage(message)
    else:
        message.reply('Do you mean `getvminfo` ??')


@respond_to(r'^listallvms\.*')
def list_all_vmname(message):
    if message.body['text'].split()[0] == 'listallvms':
        options = message.body['text'].split()[1:]
        if len(options) == 0:
            message.reply('Right, let me find list of VM name ...')
            time.sleep(3)

            vmnames = []
            vms = get_vm_list()
            for vm in vms['value']:
                vmnames.append(vm['name'])

            message.reply('Here\'s the list of VM name !!')
            message.send(str(vmnames))
        else:
            message.reply('Too many options provides. Check usage.')
            show_usage(message)
    else:
        message.reply('Do you mean `listallvms` ??')


@respond_to(r'^createvm\.*')
def create_vm(message):
    if message.body['text'].split()[0] == 'createvm': 
        options = message.body['text'].split()[1:]
        vmspec = 'low'
        if len(options) == 0:
            message.reply('Required at least VM name, nothing to do.')
            show_usage(message)
        elif len(options) > 2:
            message.reply('Too many options provides. Check usage.')
            show_usage(message)
        else:
            vmname = options[0]
            # Spec validation
            if len(options) == 2:
                if (options[1] == 'high') or (options[1] == 'mid') or (options[1] == 'low'):
                    vmspec = options[1]
                    message.reply('Fine !! Let me create your VM named [ {0} ] with spec [ {1} ]'.format(vmname, vmspec))
                    ret = create_virtual_machine(vmname=vmname, vmspec=vmspec)
                    if ret is not None:
                        message.send('>>> Successufly provisioned your VM.')
                        power_on_vm(vmid=ret['value'])
                        message.send('>>> Powered On your VM.')
                    else:
                        message.send('>>> Sorry..., failed to create your VM.')
                else:
                    message.reply('Wrong spec provided. Spec of VM should be [ high | mid | low ]')
            # Default spec (user omitting the spec)
            else:
                message.reply('Fine !! Let me create your VM named [ {0} ] with default spec [ {1} ]'.format(vmname, vmspec))
                ret = create_virtual_machine(vmname=vmname, vmspec=vmspec)
                if ret is not None:
                    message.send('>>> Successufly provisioned your VM.')
                    power_on_vm(vmid=ret['value'])
                    message.send('>>> Powered On your VM.')
                else:
                    message.send('>>> Sorry..., failed to create your VM.')

    else:
        message.reply('Do you mean `createvm` ??')


@respond_to(r'^deletevm\.*')
def delete_vm(message):
    if message.body['text'].split()[0] == 'deletevm': 
        options = message.body['text'].split()[1:]
        if len(options) == 0:
            message.reply('Required at least VM name to delete, nothing to do.')
            show_usage(message)
        elif len(options) > 1:
            message.reply('Sorry, currently I can delete only one VM ...')
        else:
            vmname = options[0]
            message.reply('Okay, delete your VM named [ {} ]'.format(vmname))
            vmid_to_delete = get_vm_id(vmname=vmname)
            if vmid_to_delete is not None:
                ret = destroy_vm(vmid=vmid_to_delete)
                if ret is not None:
                    message.send('>>> Successufly delete your VM.')
                else:
                    message.send('>>> Sorry..., failed to delete your VM it might because powering on now. Please check VM power status.')
            else:
                message.send('>>> Failed to delete your VM. VM name provided might not exist on vSphere.')

    else:
        message.reply('Do you mean `deletevm` ??')


@respond_to(r'^shutdownvm\.*')
def shutdown_vm(message):
    if message.body['text'].split()[0] == 'shutdownvm': 
        options = message.body['text'].split()[1:]
        if len(options) == 0:
            message.reply('Required at least VM name to power off, nothing to do.')
            show_usage(message)
        elif len(options) > 1:
            message.reply('Sorry, currently I can shutdown only one VM ...')
        else:
            vm = VirtualMachine(vc=vcapi)
            vmname = options[0]
            message.reply('Okay, powering off your VM named [ {} ]'.format(vmname))
            vmid_to_shut = get_vm_id(vmname=vmname)
            if vmid_to_shut is not None:
                ret = vm.power_off(vmid=vmid_to_shut)
                if ret is not None:
                    message.send('>>> Successufly powered off your VM.')
                else:
                    message.send('>>> Sorry..., failed to power off your VM.')
            else:
                message.send('>>> Failed to power off your VM. VM name provided might not exist on vSphere.')

    else:
        message.reply('Do you mean `shutdownvm` ??')


@respond_to(r'^startvm\.*')
def start_vm(message):
    if message.body['text'].split()[0] == 'startvm': 
        options = message.body['text'].split()[1:]
        if len(options) == 0:
            message.reply('Required at least VM name to power on, nothing to do.')
            show_usage(message)
        elif len(options) > 1:
            message.reply('Sorry, currently I can start only one VM ...')
        else:
            vm = VirtualMachine(vc=vcapi)
            vmname = options[0]
            message.reply('Okay, powering on your VM named [ {} ]'.format(vmname))
            vmid_to_start = get_vm_id(vmname=vmname)
            if vmid_to_start is not None:
                ret = vm.power_on(vmid=vmid_to_start)
                if ret is not None:
                    message.send('>>> Successufly powered on your VM.')
                else:
                    message.send('>>> Sorry..., failed to power on your VM.')
            else:
                message.send('>>> Failed to power on your VM. VM name provided might not exist on vSphere.')

    else:
        message.reply('Do you mean `shutdownvm` ??')


@respond_to(r'^listallnets\.*')
def list_all_networks(message):
    if message.body['text'].split()[0] == 'listallnets':
        options = message.body['text'].split()[1:]
        if len(options) == 0:
            message.reply('Right, let me find list of network name ...')
            time.sleep(3)

            networks = []
            nets = get_network()
            print(nets)
            for net in nets['value']:
                networks.append(net['name'])
                # Display modifications
            message.reply('Here\'s the list of virtual networks !!')
            message.send(str(networks))
        else:
            message.reply('Too many options provides. Check usage.')
            show_usage(message)
    else:
        message.reply('Do you mean `listallnets` ??')


@respond_to(r'^help\.*')
def get_help(message):
    message.reply('Of course, here is the help page of mine.')
    show_usage(message)


@respond_to(r'^thank\.*|^Thank\.*')
def reply_to_thanks(message):
    message.reply('My pleasure, thank you too.')
