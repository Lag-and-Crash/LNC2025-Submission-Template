LNC 2025 Challenge Submission Template
===

## Table of Contents
- [Examples](#examples)
- [Flag Format](#flag-format)
- [Challenge Template](#challenge-template)
- [How to Make a Challenge](#how-to-make-a-challenge)
  - [Static Challenges](#static-challenges)
  - [Hosted Challenges](#hosted-challenges)
- [Packaging the Challenge](#packaging-the-challenge)
- [Frequently Asked Questions](#frequently-asked-questions)

## Examples
- [Static Challenge Example](./examples/Lets%20do%20RSA/)
- [Hosted TCP Challenge Example](./examples/Gimme%20Flag/)
- [Hosted Web with Backend Challenge Example](./examples/Gimme%20Flag/)
- [Hosted Static Web Challenge Example](./examples/what%20a%20mess/)

## Flag Format
The flag format for LNC 2025 is `LNC25{...}`. Please make sure that the flag is in this format.

## Challenge Template
The challenge folder structure is as follows:
```
.
└── 📁 {challenge_name}/
    ├── 📁 dist/
    │   └── 📄...
    ├── 📁 service/
    │   ├── 📁 {service_name}/
    │   │   ├── 📄...
    │   │   └── 🐋 Dockerfile
    │   └── 🐋 docker-compose.yml
    ├── 📄 chall.toml
    └── 📄 README.md
```

| File/Directory | Description |
| -------------- | ----------- |
| `dist/` | Directory containing the challenge files to give to users attempting the challenge. |
| `service/` | Directory containing the services for challenges that require hosting. |
| `service/{service_name}/` | Directory containing the files for the service. This folder must container a `Dockerfile` |
| `service/docker-compose.yml` | Docker Compose file to run the services. This is only needed for challenges that require specific configurations set in their docker compose. For most challenges, you do not need to specify this. |
| `chall.toml` | TOML file containing the metadata for the challenge. This is generated automatically by `chall-architect` |
| `README.md` | Markdown file containing the description of the challenge. This is generated automatically by `chall-architect` |

## How to Make a Challenge
There are two main types of challenges:
1. **Static Challenges**: These challenges are not hosted on a server and are given to the user as a file to download. Examples include cryptography challenges, reverse engineering challenges, etc.
2. **Hosted Challenges**: These challenges require a server to host the challenge. Examples include web challenges, pwn challenges, etc.

### Static Challenges
Static challenges are the easiest to make. Just prepare the following files:
1. **Challenge Files**: These are the files that the user will download to solve the challenge.
2. **Solution Files**: These are the files that contain the solution to the challenge, which will be used for vetting purposes. At the very least, please provide a `writeup.md` file containing the solution to the challenge. Scripts for solving challenges are also appreciated.

### Hosted Challenges
Hosted challenges require a bit more setup. You will need to create a service that hosts the challenge. This service will be run in a Docker container. The `Dockerfile` should expose the port the service is running on.

> [!IMPORTANT]  
> If you are unfamiliar with Docker, please read the [Docker Documentation](https://docs.docker.com/get-started/).

After creating your service, you also need to create solution files for vetting purposes. At the very least, please provide a `writeup.md` file containing the solution to the challenge. Scripts for solving challenges are also appreciated.

If you intend to provide the source code for the service to users solving the challenge, if the service has mulitple files, zip it up. 

> [!WARNING]
> Remember to remove any flags or sensitive information from the source code before distributing it to users!

#### Service Types
When packaging your hosted challenge using `chall-architect`, you will be asked to specify the type of service you are using. The following are the available service types:
- `web`     : A web service, must have a port exposed
- `tcp`     : A tcp service, must have a port exposed
- `ssh`     : An ssh service, must have a port exposed
- `secret`  : A secret service, it must have a port exposed, but will not be shown to users in the challenge info. This is useful for challenges where the service must be discovered by the player
- `internal`: An internal service, does not need to expose a port, and will not be shown in the challenge info. This is useful for challenges where the service should not be accessed directly, i.e. web admin bots for XSS challenges.

## Packaging the Challenge
After creating your challenge, you need to package it using `chall-architect`. This tool will generate the necessary metadata files for the challenge.

> [!IMPORTANT]
> Do note that this tool is still in development, and may not be fully functional. If you encounter any issues, please contact the LNC team, or JusCodin for assistance.

### 1. Download the `ctf_config.toml` File
You can find the `ctf_config.toml` file [here](./ctf_config.toml)

### 2. Run `CTF Architect`
For information on how to use `CTF Architect`, please refer to [this guide for installation](https://jus-codin.github.io/CTF-Architect/installation/), and [this guide for packaging challenges](https://jus-codin.github.io/CTF-Architect/guides/packaging-challenges/)

### 3. Submit the Challenge
> [!IMPORTANT]
> Incorrectly formatted or packaged challenges will most likely be rejected. However, you may be contacted for clarification if necessary. If you have any questions or concerns, do open a ticket on the [LNC Discord Server](https://discord.com/invite/H6U6NykFRe)

After packaging the challenge, fill up the Google Form and include the zipped challenge for review. If the challenge is accepted, it will be added to the CTF.

## Frequently Asked Questions
- **Q:** What do I do if I don't know how to write a `Dockerfile` for hosted challenges?
  - **A:** The preferred method is to refer to provided `Dockerfile`s in [examples](#examples). If you are still unsure, please contact your school's LNC 2025 representative for assistance, or open a ticket on the [LNC Discord Server](https://discord.com/invite/H6U6NykFRe).
- **Q:** My challenge has custom/non-standard hosting requirements, what do I do?
  - **A:** Please contact your school's LNC 2025 representative for assistance, or open a ticket on the [LNC Discord Server](https://discord.com/invite/H6U6NykFRe). We will do our best to accommodate your requirements.
