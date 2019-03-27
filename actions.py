#Reddit chatbot made by griffinpuc
#GitHub: https://github.com/griffinpuc

from imageai.Prediction import ImagePrediction
from weather import Weather, Unit
import redBot
import praw
import pdb
import re
import sys
import os
import ast
import requests
import json

redbot = redBot.main()
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.getcwd() + "\data\\resnet50_weights_tf_dim_ordering_tf_kernels.h5")
prediction.loadModel()

for _ in range(12):
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

#All new actions go here:

def writepost(submission, message):
    submission.reply(message)
    redbot.console("createpost", submission.id, submission.title)



def getweather(submission, message):
    redbot.console("startprocess", submission.id, submission.title)

    api_key = "34c5bb47d74c25810d2e4ab65ebc1bc3"
    keywords = [ "whats the weather in", "what is the weather in", "what's the weather in"]

    title = submission.title.split(" ")
    
    for keyword in keywords:
        if keyword in submission.title:

            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = title[title.index("in")+1]
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url) 

            x = response.json() 

            if x["cod"] != "404": 
                z = x["weather"] 
                y = x["main"] 
                submission.reply("Hello! In " + city_name + " it is currently " + str(z[0]["description"]) + " and is " + str(round((((y["temp"] - 273.15)* 1.8) + 35), 1)) + " degrees F.")
                redbot.console("createpost", submission.id, submission.title)


def whatsthisimage(submission, message):
    redbot.console("startprocess", submission.id, submission.title)

    url = submission.url

    Picture_request = requests.get(url)
    if Picture_request.status_code == 200:
        with open("data\image.jpg", 'wb') as f:
            f.write(Picture_request.content)
            f.close()


    #prediction = loadlibrary()
    predictions, probabilities = prediction.predictImage(("data\image.jpg"), result_count=5 )
    prediction1 = predictions[0].replace("_", " ")
    prediction2 = predictions[1].replace("_", " ")

    submission.reply("It is a " + prediction1 + ". I am " + str(round(probabilities[0], 2)) +
                     "% sure that this is a " + prediction1 + ". But it has the possibility to be a " +
                     prediction2 + " as well. You're welcome!")

    redbot.console("createpost", submission.id, submission.title)