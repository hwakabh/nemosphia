import os
import sys

API_TOKEN = os.environ.get('API_TOKEN')
if API_TOKEN == None:
    print('>>> No API_TOKEN parameter configured, please use `export API_TOKEN="YOUR_TOKEN"` commands first.')
    sys.exit('>>> Bot programs failed to run, exit...')

# Get vSphere credentials securely from environmental variables
VC_IPADDR = os.environ.get('VSPHERE_IP')
VC_USERNAME = os.environ.get('VSPHERE_USERNAME')
VC_PASSWORD = os.environ.get('VSPHERE_PASSWORD')

if (VC_IPADDR is None) or (VC_USERNAME is None) or (VC_PASSWORD is None):
    print('>>> No vSphere credentials provided. Confirm the parameters have been configured properly with environmental variables like:')
    print('\t export VSPHERE_IP=\'vcsa01.mylab.local\'')
    print('\t export VSPHERE_USERNAME=\'administrator@vsphere.local\'')
    print('\t export VSPHERE_PASSWORD=\'VMware1!\'')
    sys.exit('>>> Bot programs failed to run, exit...')

# DEFAULT_REPLY = "Hello World from SlackBot !!"
PLUGINS = ['plugins']
