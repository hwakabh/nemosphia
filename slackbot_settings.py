import os
import sys

API_TOKEN = os.environ.get('API_TOKEN')
if API_TOKEN == None:
    print('>>> No API_TOKEN parameter configured, please use `export API_TOKEN="YOUR_TOKEN"` commands first.')
    sys.exit('>>> Bot programs failed to run, exit')

# DEFAULT_REPLY = "Hello World from SlackBot !!"
PLUGINS = ['plugins']
