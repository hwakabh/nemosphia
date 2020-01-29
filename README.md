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
    - In case your environment uses `virtualenv`, start by creating virtual environments for this function first like:
      - `python3 -m venv venv`
        - You could specify the name of venv whatever you like
      - `source ./venv/bin/activate`
        - Confirm that the name of venv name would be added to the prompt of your shell
    - Note that Python `slackbot` libraries will be installed for your environment with this operations, which are required to run this program.

- Set your environmental variables
  - API Tokens
    - The slackbot programs will kick the API provided by Slack, and we need the Tokens for authentications.
    - Check your bots API tokens in Slack settings pages, and set them to parameter `API_TOKEN` with following command.
      - If you use `bash`:
      - `export API_TOKEN="YOUR_SLACK_API_TOKEN"`
        - As security considerations, we should pass the credentials to Bot programs as environmental variables
      - With your shell where you'd run start this programs, set parameters with any commands.
  - Credentials for vSphere
    - Credentials of vSphere environment, with vCenter Server, are defined in the file so that the bot program could use for your environment.
    - Before running the bot, you should set each values so that program could manage your vSphere environment.
    - For example, define variables as vSphere credentials with the commands like:
      - `export VSPHERE_IP='vcsa01.mylab.local'`
        - Both IP address and FQDN are supported
      - `export VSPHERE_USERNAME='administrator@vsphere.local'`
        - Notice that provided user should have the roles/permissions to create Virtual Machines or templates.
      - `export VSPHERE_PASSWORD='VMware1!'`

## Hello, Bot

- Start to run Slackbot programs
  - `python3 ./run_bot.py`

- Case if you run programs permanently or run as background process, it would be preferable to run with `nohup` like below:
  - `nohup python3 ./run_bot &`

## Licensing

- This programs is exported as open sources with the license of MIT License since sourced Python library `slackbot` is under the license.
