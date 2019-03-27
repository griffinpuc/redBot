import redBot
import os

redbot = redBot.main()

#Main loop
def main():

    redbot.addaction("bwrite", writepost)
    redbot.addaction("weather", getweather)

    redbot.addprocess(redbot.process("blacklist.txt", "griffinp", "pyprocess", "hey", "hi hows it going", redbot.actions['bwrite']))
    redbot.addprocess(redbot.process("blacklist.txt", "griffinp", "pyprocess", "weather", None, redbot.actions['weather']))


    print("Running processes...")

    while True:
        redbot.start()


#All new actions go here:
#================================================================================================================

def writepost(submission, message):
    submission.reply(message)
    redbot.console("createpost", submission.id, submission.title)



def getweather(submission, message):
    


#================================================================================================================

#Must be at the bottom
main()