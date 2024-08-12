# RGB lights control server
The remote RGB lights control server

https://lights-control-server.leaptheorytech.com/

## environment values
- **JWT_SECRET**
- **JWT_SECRET_OLD** (Optional, use it if you need to change secrets smoothly)
- **JWT_ALGORITHM** (By default "EdDSA")
- **SLACK_SIGNING_SECRET** 
- **SLACK_TARGET_CHANNEL_ID** Slack channel ID from which emojis will be read to change color


## only 1 worker!
please use only one worker because the application stores the environment in global variables

## clients

- arduino based client https://github.com/anton-panfilov/lights_client