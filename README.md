# LNC 2025 Challenge Submission Template

In order to automate the deployment of challenges, the challenge committee has
defined a standard folder structure (with specific metadata files) to facilitate
an easier way to deploy challenges. This document defines how we plan on
translating challenge folders into actual CTFd challenges.

## Flag Format

To ensure consistency, LNC has defined a flag format for all challenge creators
to follow. The flag should match the regex expression of `^LNC25\{.*\}$`. An
example of a flag that matches the said regex expression is
`LNC25{th1s_1s_A_fl4g}`.

## Folder Template

The challenge & file structure should look like this:

```
challenge_name/
    |
    ├─ dist/
    │       ├─ files_to_give_to_participants
    |
    ├─ service/
    │       ├─ Dockerfile
    │       ├─ files_to_host_challenge
    |
    ├─ solution/
    │       ├─ writeup.md
    │       ├─ solution_files
    |
    ├─ chall.json
    ├─ README.md
```

Additional folders can be added, but they will be ignored by the deployment
script. Each of the folders defined above serve a specific purpose as documented
below:

`dist/`

All files within the `dist/` folder **will be given** to the participants, so
don't leak any sensitive information here. This folder can be left empty if your
challenge has no files to give to the participants.

`service/`

This folder will contain all the deployment-related files. A `Dockerfile`
**must** be present to tell us how to build your challenge. Refer to the
`examples` folder in this repository for how `service` folders should look
like.

`solution/`

This folder should contain a `writeup.md` file, with additional assets like
**images** or **solve scripts** to assist the reader in solving your challenge. While
the `writeup.md` filename is not necessary, it's best to have a naming
convention to follow.

`chall.json`

This file contains additional challenge metadata for deployment to CTFd. The
full specs on how to craft this file is documented in the section below.

## Chall.JSON Structure

This file should contain the following **compulsory** fields:

| Field       | Type | Description                                                                                                                                                    |
| ----------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name        | str  | Challenge name. Should match folder name when possible.                                                                                                        |
| author      | str  | The challenge author's name.                                                                                                                                   |
| category    | str  | One of the following categories (`crypto`, `forensics`, `misc`, `osint`, `pwn`, `re`, `web`). If unsure, put it as `misc`.<br><br>**This is case sensitive!!** |
| difficulty  | str  | One of the following difficulties (`easy`, `medium`, `hard`, `insane`).<br><br>**This is case sensitive!!**                                                    |
| description | str  | A description of the challenge. Encode any newlines with `\n`.<br><br>_Note: If you have a service, the connection URL will be automatically filled in below._ |
| discord     | str  | The challenge author's discord username.                                                                                                                       |
| flag        | str  | The challenge flag. Should match the regex `LNC25\{.*\}$`                                                                                                      |

The file can also contain the following **optional** fields. Some or all of these fields can be left out in your `chall.json`.

| Field        | Type      | Description                                                                                                                                                                   |
| ------------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| port         | int       | The port that your service exposes, between `1` and `65535`. Both `port` and the `service/` folder should exist or an error would be thrown.                                  |
| requirements | List[str] | A list of strings containing the `name` of the challenges a user has to complete before unlocking the current challenge.                                                      |
| hints        | List[obj] | A list of objects containing hints. Each hint object should have a `cost` (int) and `description` (str). An example hint object can be found in the `examples` section below. |

### Chall.json Examples

**Bare minimum chall.json**

```json
{
    "name": "Lorem Ipsum",
    "author": "John Doe",
    "category": "misc",
    "difficulty": "easy",
    "description": "This is a multi-line\ndescription.",
    "discord": "john.doe",
    "flag": "LNC25{f4k3_fl4g_f0r_t3st1ng}"
}
```

**Challenge with a service**

Let's assume a Flask challenge with the following code:

```python
from flask import Flask

app = Flask (__name__)

# ...Flask stuff...

app.run(port=8080)
```

Your `chall.json` should look similar to:

```json
{
    "name": "Web Challenge",
    "author": "John Doe",
    "category": "web",
    "difficulty": "easy",
    "description": "I made a web application! Hack me.", // Connection URL will be appended by the script
    "discord": "john.doe",
    "flag": "LNC25{f4k3_fl4g_f0r_t3st1ng}",
    "port": 8080 // Same as the Python script
}
```

**Adding hints**

```json
"hints": [
  {
    "cost": 10,
    "description": "Lorem ipsum dolo amet ..."
  }
]
```

**Adding requirements**

```json
// challenge-1/chall.json
{
    "name": "Challenge 1",
    "author": "John Doe",
    "category": "misc",
    "difficulty": "easy",
    "description": "This is a multi-line\ndescription.",
    "discord": "john.doe",
    "flag": "LNC25{f4k3_fl4g_f0r_t3st1ng}"
}

// challenge-2/chall.json
{
    "name": "Challenge 2",
    "author": "John Doe",
    "category": "misc",
    "difficulty": "medium",
    "description": "This is a multi-line\ndescription.",
    "discord": "john.doe",
    "flag": "LNC25{f4k3_fl4g_f0r_t3st1ng_aga1n}",
    "requirements": ["Challenge 1"]
}
```

## Frequently Asked Questions (FAQs)

**Q**: If I am creating a static challenge (forensics, crypto, etc.), do I need
to include a `service` folder? \
**A**: No, you do not need to include a `service` folder if your challenge is
static.

**Q**: I'm having trouble submitting my challenge, what should I do? \
**A**: Please contact your school's LNC 2025 representative for assistance,
alternatively you can contact the challenge team by opening a ticket on our
[Discord](https://discord.gg/H6U6NykFRe) server.
