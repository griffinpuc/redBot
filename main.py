#Reddit chatbot made by griffinpuc
#GitHub: https://github.com/griffinpuc

import praw
import pdb
import re
import os
import ast

reddit = praw.Reddit('redbot7337')
subreddit = reddit.subreddit("griffinp")

currentdir = os.getcwd()
replied_file = "posts_replied_to.txt"
path = (currentdir + "\\" + replied_file)


class printout:
    def __init__(self, info, ID, post):
        self.info = info
        self.ID = ID
        self.post = post

    def console(self):
        print("[redBot]: " + self.info + " " + self.ID + " title: " + self.post)


class process:
    def __init__(self, key, blacklist, message):
        self.key = key
        self.blacklist = blacklist
        self.message = message

    def run(self):
        scansub(self.key, self.blacklist, self.message)


def setup():

    if not os.path.isfile(path):
        posts_replied_to = []

    else:
        with open(path, "r") as f:
            posts_replied_to = ast.literal_eval(f.read())

    return posts_replied_to


def writeblacklist(posts_replied_to):

    with open(path, 'w') as f:
        f.write(str(posts_replied_to))
        f.close()


def writepost(submission, message):
    
    submission.reply(message)

    info = printout("REPLIED TO", submission.id, submission.title)
    info.console()

    info = printout("ADDED POST", submission.id, submission.title)
    info.console()


def scansub(key, blacklist, message):

    for submission in subreddit.hot(limit=5):
            if submission.id not in blacklist:
                if re.search(key, submission.title, re.IGNORECASE):
                    writepost(submission, message)
                    blacklist.append(submission.id)
                    writeblacklist(blacklist)


def main():
    blacklist = setup()

    pr1 = process("i love python", blacklist, "i love python too!")

    print("Running processes...")

    while True:
        pr1.run()

main()