#Reddit chatbot made by griffinpuc
#GitHub: https://github.com/griffinpuc

from weather import Weather, Unit
import redBot
import praw
import pdb
import re
import os
import ast
import requests
import json

redbot = redBot.main()

#All new actions go here:

def writepost(submission, message):
    submission.reply(message)
    redbot.console("createpost", submission.id, submission.title)



def getweather(submission, message):

    api_key = "34c5bb47d74c25810d2e4ab65ebc1bc3"
    keywords = [ "whats the weather in", "what is the weather in", "what's the weather in"]

    title = submission.title.split(" ")
    
    for keyword in keywords:
        if keyword in submission.title:
            redbot.console("createpost", submission.id, submission.title)

            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = title[title.index("in")+1]
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url) 

            x = response.json() 

            if x["cod"] != "404": 
                z = x["weather"] 
                y = x["main"] 
                submission.reply("Hello! In " + city_name + " it is currently " + str(z[0]["description"]) + " and is " + str(((y["temp"] - 273.15)* 1.8) + 35) + " degrees F.")