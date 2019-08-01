# slackbot-vsphere

## Overview

- Slack Bot for VM provisioning to vSphere
  - Wrapper of vSphere API functions
- User could use this software as portable interface of vSphere environment.
  - Interactive-operation with SlackBot
  - Operate with simple text format as Slack message

## Prerequirements

- Install required Python libraries
  - `pip install -r requirements.txt`
    - Case if your environment use `virtualenv`, start to create virtual environments for this function at first.
    - Note that Python `slackbot` libraries would be installed for your environments, which mush be required to run this programs.

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
