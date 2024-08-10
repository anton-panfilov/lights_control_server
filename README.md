# RGB lights control server
The remote RGB lights control server

## environment values
- **JWT_SECRET**
- **JWT_SECRET_OLD** (Optional, use it if you need to change secrets smoothly)
- **JWT_ALGORITHM** (By default "EdDSA")

## only 1 worker!
please use only one worker because the application stores the environment in global variables