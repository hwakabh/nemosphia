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

DEFAULT_REPLY = '''
```
Syntax : COMMAND [ARGS]
    - getvminfo <NAME_OF_VM>
    - getnetinfo <NAME_OF_VM>
    - listallvms
    - listallnets
    - createvm <NAME_OF_VM> <VM_SPEC>
    - deletevm <NAME_OF_VM>
    - shutdownvm <NAME_OF_VM>
    - startvm <NAME_OF_VM>

Each VM_SPEC would be defined as:
  - high
    - 2 Core per Socket / 4 vCPU
    - 8 GiB vRAM
  - mid
    - 2 Core per Socket / 2 vCPU
    - 4 GiB vRAM
  - low
    - 1 Core per Socket / 1 vCPU
    - 1 GiB vRAM
    - NOTE: If no VM_SPEC parameters was provided, Lowest spec VM would be createda
```
'''

PLUGINS = ['plugins']
