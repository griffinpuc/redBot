#Reddit chatbot made by griffinpuc
#GitHub: https://github.com/griffinpuc

import redBot
import actions
import os
import time
import sys

redbot = redBot.main()

#Main loop
def main():

    #Add actions here
    #redbot.addaction(name, methodname)
    redbot.addaction("bwrite", actions.writepost)
    redbot.addaction("weather", actions.getweather)

    #Add processes here
    #redbot.addprocess(redbot.process(blacklistname, subredd, name, keyword, message, action))
    redbot.addprocess(redbot.process("blacklist.txt", "griffinp", "pyprocess", "hey", "hi hows it going", redbot.actions['bwrite']))
    redbot.addprocess(redbot.process("blacklist.txt", "griffinp", "pyprocess", "weather", "none", redbot.actions['weather']))

    while True:
        redbot.start()

main()