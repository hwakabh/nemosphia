from slackbot.bot import Bot  # When imported Bot class, `slackbot_settings.py` will run first.
import os
import sys


def main():
    # Fetch all dependencies
    VC_IPADDR = os.environ.get('VC_IPADDR')
    VC_USERNAME = os.environ.get('VC_USERNAME')
    VC_PASSWORD = os.environ.get('VC_PASSWORD')
    # Application specific authentication, after base auth with API_TOKEN
    print('--->>> Prechecking vSphere credentials')
    if (VC_IPADDR is None) or (VC_USERNAME is None) or (VC_PASSWORD is None):
        print('No vSphere credentials provided.')
        print('Confirm the parameters have been configured properly with environmental variables like:')
        print('    export VC_IPADDR=\'vcsa01.mylab.local\'')
        print('    export VC_USERNAME=\'administrator@vsphere.local\'')
        print('    export VC_PASSWORD=\'VMware1!\'')
        sys.exit(1)
    else:
        print('done')

    print()
    print('>>> Completed initializing, start to run bot.')
    print('    vCenter Server connected: {}'.format(VC_IPADDR))
    print('    Log in as : {}'.format(VC_USERNAME))
    bt = Bot()
    bt.run()


if __name__ == '__main__':
    main()