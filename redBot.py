#Reddit chatbot made by griffinpuc
#GitHub: https://github.com/griffinpuc
# :)

from time import gmtime, strftime
import praw
import pdb
import re
import os
import ast
import sys
import time

class main():

    class process:
        def __init__(self, blacklist, subreddit, name, key, message, action):
            reddit = praw.Reddit('redbot7337')
            self.key = key
            self.path = os.getcwd() + "\\" + blacklist
            self.message = message
            self.action = action
            self.subreddit = reddit.subreddit(subreddit)
            self.name = name

    processes = []
    actions = {}

    def start(self):
        for process in self.processes:
            self.scansub(process)

    def setup(self, path):
        if not os.path.isfile(path):
            blacklist = []
        else:
            with open(path, "r") as f:
                blacklist = ast.literal_eval(f.read())
        return blacklist

    def scansub(self, process):
        blacklist = self.setup(process.path)
        for submission in process.subreddit.hot(limit=5):
                if submission.id not in blacklist:
                    if (re.search("redbot", submission.title, re.IGNORECASE)):
                        if (re.search(process.key, submission.title, re.IGNORECASE)):
                            process.action(submission, process.message)
                            blacklist.append(submission.id)
                            with open(process.path, 'w') as f:
                                f.write(str(blacklist))
                                f.close()

    def addprocess(self, process):
        self.processes.append(process)
        self.console("addprocess", str(process.action), process.name)

    def addaction(self, name, action):
        self.actions[name] = action
        self.console("addaction", str(action), name)

    def restart_line(self):
        sys.stdout.write('\r')
        sys.stdout.flush()

    def console(self, call, info, data):
        time = strftime("%H:%M:%S", gmtime())
        if call == "createpost":
            print(time + "[redBot]: {" + call + " " + info + "} " + "TO POST [" + data + "]")
        if call == "addprocess":
            print(time + "[redBot]: {" + call + " " + info + "} " + "ADDED PROCESS [" + data + "]")
        if call == "addaction":
            print(time + "[redBot]: {" + call + " " + info + "} " + "ADDED ACTION [" + data + "]")
        if call == "startprocess":
            print(time + "[redBot]: {" + call + " " + info + "} " + "INITIALIZING A PROCESS [" + data + "]")
        else:
            pass