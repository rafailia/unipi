"""
Name          :Rafailia
Surname       :Ioannou
Programm Title: IMDB Movies Score and Awards
Date          :30/09/16
Description   : First install the requests module.
"""
import requests
import json
import sys
#web service
url = "http://www.omdbapi.com/?t=";
print("Input the movie title with \" at begin and the end. Sample \"The Godfather\"");
#Read the input movie title
try:
	title=str(input());
except Exception:
		print("Oops! Something went wrong. Try again...");
		sys.exit();
response = requests.get(url+title+"&r=json");
if(response.ok):
	jData = json.loads(response.content);
	if(jData["Response"]=="True"):
		print("Imdb rating:" + jData["imdbRating"]);
		print("Awards:" + jData["Awards"]);	
	else:
		print("Error:Movie Not Found");
