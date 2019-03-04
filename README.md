# slack-vsphere

## Overview

- Slack Bot for VM provisioning to vSphere
- User could use this software as portable interface of vSphere environment.
  - Interactive-operation with SlackBot
  - Operate with simple text format as Slack message


## Hello, Bot

- Starting to use slack-vsphere bot, the following procedures would be required for your environments
  - Install required Python libraries
    - `pip install -r requirements.txt`
      - Case if your environment use `virtualenv`, start to create virtual environments for this function at first.
      - Note that Python `slackbot` libraries would be installed for your environments, which mush be required to run this programs.
  - Setting up configuration variables
    - Replace the value in `env_config.json` with the parameters for your environments
      - `vi env_config.json`
    - By default, variables for vSphere credentials(`VSPHERE_USERNAME` and `VSPHERE_PASSWORD`) are the below:
      - `VSPHERE_USERNAME` : `administrator@vsphere.local`
      - `VSPHERE_PASSWORD` : `VMware1!`
  - Start to run Slackbot programs
    - `python ./run_bot.py`
      - Case if you run programs permanently or run as background process, it would be preferable to run with `nohup` like below:
        - `nohup python ./run_bot &`

