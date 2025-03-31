# LNC 2024 Challenge Submission Template 

## Flag Format
- LNC25{flag}

## Template 
The challenge & file structure should look like this:
```
challenge_name/
    |
    ├─ dist/
    │       ├─ file_to_give_to_participants
    |
    ├─ service/
    │       ├─ container-name/
    │           ├─ Dockerfile
    │           ├─ files_to_host_challenge
    |
    ├─ solution/
    │       ├─ writeup.md
    │       ├─ solution_files
    |
    ├─ chall.yaml
    ├─ README.md
```

*note from organizing team: please ensure that your `README.md` & `chall.yaml` contains the same information*
* You can generate `chall.yaml` using https://github.com/Jus-Codin/CTF-Architect
  * Please use this!

- `dist`
  - This folder contains all the files that **will be given** to the participants, leave this folder empty if none.
- `service`
  - This folder contains all the files that will be used by the organizers to host your challenge, leave this folder empty if none.
  - `container-name`
    - This folder contains all the files that will be used to build the docker image for your challenge, do note that this may be given to participants to host the challenge locally if they wish to do so.
    - `Dockerfile`
      - This file contains the instructions to build the docker image for your challenge.
- `solution`
  - This folder should contain a writeup of your challenge and solution files if any.
  - If your challenge is generated using a script, please include the script in this folder.

## Frequently Asked Questions (FAQs)
- **Q**: If I am creating a static challenge (forensics, crypto, etc.), do I need to include a `service` folder?
  - **A**: No, you do not need to include a `service` folder if your challenge is static.
- **Q**: I'm having trouble submitting my challenge, what should I do?
  - **A**: Please contact your school's LNC 2025 representative for assistance, alternatively you can contact the challenge team by opening a ticket on our [Discord](https://discord.gg/H6U6NykFRe) server.
