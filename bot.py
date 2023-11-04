# *****************************************************************************
# ***************************  Python Source Code  ****************************
# *****************************************************************************
#
#   DESIGNER NAME:  Kushal Timsina
#
#       FILE NAME:  bot.py
#
# DESCRIPTION
#    This code turns an LED on and off (GPIO18) using the discord API.
#
# *****************************************************************************

import discord
import RPi.GPIO as GPIO
from discord.ext import commands

BOT_TOKEN = "NDk2ODI3Nzk1Nzg0MzM1Mzcx.GkGcbP.tlrGWLWRmaIlXW32q3W5XvrXMQPEdrM8nkr0iM"
LED_OUTPUT = 18
LED_ON = GPIO.HIGH
LED_OFF = GPIO.LOW

pwm_handle = None
intents = discord.Intents.default()
#intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def setup_gpio():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LED_OUTPUT, GPIO.OUT, initial=LED_OFF)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def on(ctx):
    global pwm_handle
    GPIO.output(LED_OUTPUT, LED_ON)
    await ctx.send("Turned the LED on!")

@bot.command()
async def off(ctx):
    global pwm_handle
    GPIO.output(LED_OUTPUT, LED_OFF)
    await ctx.send("Turned the LED off!")
    
pwm_handle = setup_gpio()
GPIO.output(LED_OUTPUT, LED_ON)
bot.run(BOT_TOKEN)
    
print("Up and running")