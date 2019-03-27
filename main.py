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
    redbot.addaction("image", actions.whatsthisimage)

    #Add processes here
    #redbot.addprocess(redbot.process(blacklistname, subredd, name, keyword, message, action))
    redbot.addprocess(redbot.process("blacklist.txt", "griffinp", "pyprocess", "hey", "hi hows it going", redbot.actions['bwrite']))
    redbot.addprocess(redbot.process("blacklist.txt", "griffinp", "weatherprocess", "weather", "none", redbot.actions['weather']))
    redbot.addprocess(redbot.process("blacklist.txt", "griffinp", "imageprocess", "image", "none", redbot.actions["image"]))

    while True:
        redbot.start()

main()