import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Vcenter:
    def __init__(self):
        with open('./env_config.json') as f:
            df = json.load(f)

        self.ipaddr = df['VSPHERE_IP']
        self.username = df['VSPHERE_USERNAME']
        self.password = df['VSPHERE_PASSWORD']

    def get_token(self):
        uri = 'https://{0}/rest/com/vmware/cis/session'.format(self.ipaddr)
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            }
        r = requests.post(uri, headers=headers, auth=(self.username, self.password),verify=False)
        token = json.loads(r.text)["value"]
        headers.update({"vmware-api-session-id":token})
        return headers
    
    def https_get(self, uriprefix):
        headers = self.get_token()
        uri = 'https://{0}/rest{1}'.format(self.ipaddr, uriprefix)
        print('DEBUG>>> GET from {}'.format(uri))

        # Initialize return value
        r = None
        try:
            r = requests.get(uri, headers=headers, verify=False)
            if r.status_code == 200:
                print('DEBUG>>> Return code 200, seems that Successfully GET content.')
                return json.loads(r.text)
            else:
                print('DEBUG>>> Return code is not 200, Check the connectivity or credentials...')
        except Exception as e:
            print('DEBUG>>> Some Error occurred when getting HTTP/HTTPS response.')
            print('Errors : ', e.args)
        else:
            pass

    def https_post(self, uriprefix, data):
        headers = self.get_token()
        uri = 'https://{0}/rest{1}'.format(self.ipaddr, uriprefix)
        print('DEBUG>>> POST to {}'.format(uri))

        # Initialize return value
        r = None
        try:
            r = requests.post(uri, headers=headers, verify=False, data=json.dumps(data))
            print('DEBUG>>> Trying to POST to vsphere. Raw response from vsphere are below :')
            print(r.text)
            if r.status_code == 200:
                print('DEBUG>>> Return code 200, seems that Successfully POST content.')
                return r.text
            else:
                print('DEBUG>>> Return code is not 200, Check the connectivity or credentials...')
                raise Exception
        except Exception as e:
            print('DEBUG>>> Some Error occurred when posting HTTP/HTTPS requests.')
            print('Errors : ', e.args)
            return None
        else:
            return r.text

    def https_delete(self, uriprefix, data):
        headers = self.get_token()
        uri = 'https://{0}/rest{1}'.format(self.ipaddr, uriprefix)
        print('DEBUG>>> DELETE uri is {}'.format(uri))

        # Initialize return value
        r = None
        try:
            r = requests.delete(uri, headers=headers, verify=False, data=json.dumps(data))
            print('DEBUG>>> Trying to DELETE to vsphere. Raw response from vsphere are below :')
            print(r.text)
            if r.status_code == 200:
                print('DEBUG>>> Return code 200, seems that Successfully DELETE content.')
                return r.text
            else:
                print('DEBUG>>> Return code is not 200, Check the connectivity or credentials...')
                raise Exception
        except Exception as e:
            print('DEBUG>>> Some Error occurred when deleting HTTP/HTTPS requests.')
            print('Errors : ', e.args)
            return None
        else:
            return r.text


class VirtualMachine:
    def __init__(self, vc):
        self.vc = vc

    def power_on(self, vmid):
        uriprefix = '/vcenter/vm/{}/power/start'.format(vmid)
        response = self.vc.https_post(uriprefix=uriprefix, data={})
        return response

    def power_off(self, vmid):
        uriprefix = '/vcenter/vm/{}/power/stop'.format(vmid)
        response = self.vc.https_post(uriprefix=uriprefix, data={})
        return response

