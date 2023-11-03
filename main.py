from win32com.client import Dispatch
import requests
import json

url = f"https://api.weatherapi.com/v1/current.json?key=34e7b48e38c8436d988125327230211&q={"city"}"
r = requests.get(url)
city = input("Enter the name of the city \n")
vdic = json.loads(r.text)
v = vdic["current"]["temp_c"]

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)

if __name__ == '__main__':
    speak(f" This is {city} and the weather in the city is {v} degree")