# slack-vsphere

## Overview

- Slack Bot for VM provisioning to vSphere
  - Wrapper of vSphere API functions
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


## Configuration examples

- By default, the file `env_config.json` is not included within this repository for the security reason.
  - `API_TOKEN` would be taken from each of your slack channel and this token should keep secure.

- Examples:
  - Output of executing commands for confirm `cat ./env_config.json`

```JSON
{
    "API_TOKEN" : "YOUR_API_TOKEN",
    "VSPHERE_IP": "YOUR_VCENTER_IP_ADDRESS",
    "VSPHERE_USERNAME": "administrator@vsphere.local",
    "VSPHERE_PASSWORD": "VMware1!"
}
```
