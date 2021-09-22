# GPT3-Discord-RP-Bot
Discord GOpenAI/GPT-3 roleplay chatbot.
Harvests AI and username/character intelligence.

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
openai.api_key = "OPENAI API KEY"

#Discord key
dkey = 'DISCORD KEY'

```

To obtain openai key, visit their website and register for one:
https://beta.openai.com/ Click join the waitlist, and wait for a email (this can take a LONG time, like months.)

Then put the key into the API key spot for OpenAI in the python file.


On discord developers page here:
https://discord.com/developers/applications

Create a new application, give it a name such as "RP-Bot"

Set a avatar if you wish.

Set a description and save changes.

Then click bot and click add bot.

Hit yes, then copy the token and put it in the python file replacing "DISCORD KEY"

Then open the Oauth tab.

Checkmark "Bot" then below that check "Read message history" and "Send Messages."

Copy the link to add the bot to your server after running the python file, make sure to install requirements with pip.

Commands are listed above.



Note: There is a sentiment analysis to check for negative inputs/outputs in the code. It is currently set about in the middle.
