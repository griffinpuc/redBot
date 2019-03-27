#Reddit chatbot made by griffinpuc
#GitHub: https://github.com/griffinpuc

import praw

reddit = praw.Reddit('redbot7337')

subreddit = reddit.subreddit("griffinp")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")