# discord-pi
This repo contains sample source code to interface the Raspberry Pi 4 with the discord API. 
To use this code, you'll first need a Discord bot. To create one, follow the instructions below:

# Prerequisites
## Creating a Discord Bot
1. Navigate to https://discord.com/developers/docs/intro
2. Click "Get Started"
3. Create "Create an App"
4. Name your bot. I called mine "Poketic"
5. Under "My Applications", you'll see the bot. Obtain its token by clicking on "Bot" on the left-hand side, under the settings navbar, and click the generate token button.
6. Save this somewhere in a notepad, as you'll need it later.
   
## Setting up the Pi
1. Connect GPIO18 to a 220 Ohm resistor, which is connected to the anode (long leg) of an LED
2. Connect the cathode (short leg) to GND.

# Getting Started
1. Create a file called "bot" in your Pi. I placed mine inside of Desktop.
2. Use the shell to Navigate to the "bot" directory. For me, that was `cd Desktop/bot`
3. Install `discord.py` with `sudo python3 -m pip install -U discord.py` on the Raspberry Pi
4. Take `bot.py` (found in this repo) and place it inside of the `bot` directory that you created in step #1.
5. Replace the `BOT_TOKEN` constant in the `bot.py` file with the bot authentication token that you obtained from Discord under the Prerequisites.
6. Run the file, and send a direct message to the bot.

# Commands
1. `!on` - Turn the LED on
2. `!off` - Turn the LED off

And there you go! 

Let me know if you have any suggestions.
