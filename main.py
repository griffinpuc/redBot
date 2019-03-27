import redBot
import actions
import os
import time
import sys

redbot = redBot.main()

#Main loop
def main():

    redbot.addaction("bwrite", actions.writepost)
    redbot.addaction("weather", actions.getweather)

    redbot.addprocess(redbot.process("blacklist.txt", "griffinp", "pyprocess", "hey", "hi hows it going", redbot.actions['bwrite']))
    redbot.addprocess(redbot.process("blacklist.txt", "griffinp", "pyprocess", "weather", "None", redbot.actions['weather']))

    while True:
        redbot.start()

main()