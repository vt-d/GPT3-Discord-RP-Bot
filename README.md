# GPT3-Discord-RP-Bot
Discord OpenAi roleplay chatbot. Harvests AI and username/character intelligence.

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Python 3.9.7](https://img.shields.io/badge/python-3.9.7-blue.svg)](https://www.python.org/downloads/release/python-397/)
Commands are:
```
!start
!stop
!reset
!rp (text)
!character (name of character you want to rp with)
```


Set these variables in the python file:
```
#OpenAI API key
openai.api_key = "OPENAI KEY"

#Discord key
dkey = 'DISCORD KEY'
```

### Setup OpenAI
1. To obtain the openai API key, visit their website and register for one:
https://beta.openai.com/ 

2. Click join the waitlist, and wait for a email (this can take a LONG time, like months.)

3. Put the key into the API key spot for OpenAI in the python file from the API settings on the OpenAI webpage once you get an account.

### Setup Discord Bot
1. On discord developers page here:
https://discord.com/developers/applications 

2. Create a new application, give it a name such as "RP-Bot"
Set a avatar if you wish.
Set a description and save changes.

3. Click bot and click add bot.

4. Hit yes, then copy the token and put it in the python file replacing "DISCORD KEY"

5. Open the Oauth tab. Checkmark "Bot" then below that check "Read message history" and "Send Messages."

6. Copy the link to add the bot to your server after running the python file, make sure to install requirements with pip.

```
Note: There is a sentiment analysis to check for negative inputs/outputs in the code. It is currently set about in the middle.
```
