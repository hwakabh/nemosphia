# slackbot-vsphere

## Overview

- Slack Bot for VM provisioning to vSphere
  - Wrapper of vSphere API functions
- User can use this software as portable interface for vSphere environment
  - Interactive-operation with SlackBot
  - Operate with simple text format as Slack message

## Prerequirements

- Install required Python libraries
  - `pip3 install -r requirements.txt`
    - In case your environment uses `virtualenv`, start by creating virtual environments for this function first
    - Note that Python `slackbot` libraries will be installed for your environment, which are required to run this program.

- Set your environmental variables
  - `export API_TOKEN="YOUR_SLACK_API_TOKEN"`
    - As security considerations, we should pass the credentials to Bot programs as environmental variables
    - With your shell where you'd run start this programs, set parameters with any commands.

- Adjust parameters in `env_config.json` to your environments
  - vSphere Credentials would be defined in the file so that you could statistically use the bot for your environment.
  - Before running the bot, you should modify parameters in the file.
  - The defined variables as vSphere credentials are the below:
    - `VSPHERE_IP` : Both IP address and FQDN are supported
    - `VSPHERE_USERNAME`
    - `VSPHERE_PASSWORD`

## Hello, Bot

- Start to run Slackbot programs
  - `python3 ./run_bot.py`

- Case if you run programs permanently or run as background process, it would be preferable to run with `nohup` like below:
  - `nohup python3 ./run_bot &`
