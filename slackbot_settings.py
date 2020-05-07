import os
import sys

API_TOKEN = os.environ.get('API_TOKEN')

# Base authentication with prechecking
print('>>> Starting slackbot, wait for a while to initializing...')
print('--->>> Prechecking base requirements')
if API_TOKEN is None:
    print('Failed to retrive API_TOKEN for slackbot.')
    print('Please set API_TOKEN as environmental variables on your runtime.')
    print('    export API_TOKEN=\'YOUR_TOKEN_PUBLISH_BY_SLACK_ADMIN\'')
    sys.exit(1)
else:
    print('done')

# DEFAULT_REPLY = "Hello World from SlackBot !!"
PLUGINS = ['plugins']
