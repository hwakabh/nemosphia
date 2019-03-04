import json

'''
User Configurations:
    `API_TOKEN` : Get/Set your slack channel API-Token
    `VSPHERE_IP` : Set vSphere IP to be provisoned VMs
    `VSPHERE_USERNAME` : Set vSphere username
    `VSPHERE_PASSWORD` : Set vSphere password
'''

with open('./env_config.json') as f:
    df = json.load(f)

API_TOKEN = df['API_TOKEN']
DEFAULT_REPLY = "Hello World from SlackBot !1"
PLUGINS = ['plugins']
