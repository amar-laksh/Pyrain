
"""
import requests
headers = {'User-Agent': 'Mozilla/5.0','Content-Type': 'application/html; charset=UTF-8'}
payload = {'courseCode':'ISC','uniqueId':'5537920',''}
link = 'http://www.cisce.org/Results/Result/ShowResult?'
session = requests.Session()
#resp = session.get(link,headers=headers)
cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(session.cookies))
resp = session.post(link,headers=headers,data=payload)


print resp






$.ajax({ type: 'GET', dataType: 'html', contentType: 'application/html; charset=utf-8', url: '/Results/Result/ShowResult', data: { courseCode: $("#courseDropDown").val(), uniqueId: isNaN(parseInt($("#UniqueId").val()))? 0 : $("#UniqueId").val(), captcha: $("#Captcha").val(), code: $("#RequestId").val() }
#until here sucesss!"############

url = "ajaxurl"
my_params={'part_number':'1234'}
r = session.get( url = url, data = my_params, cookies =cookies,headers =headers )
"""
from PIL import Image
import urllib2
import time
import random
from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve
import ImageEnhance
from pytesser import *
import re

"""

while True:
    page = urllib2.urlopen('http://www.cisce.org/results/result/viewresult#')
    soup = BeautifulSoup(page)
    x = soup.body.find(id='RequestId')
    y = x['value']
    print y

"""

def get(link,fil):
    urlretrieve(link,fil)




def STT(rou):
   import speech_recognition as sr
   r = sr.Recognizer()
   print "Listening..."
   with sr.Microphone() as source:                # use the default microphone as the audio source
       audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
   try:
       print "Recognizing..."
       rou = r.recognize(audio)# recognize speech using Google Speech Recognition
       return rou
   except LookupError:                            # speech is unintelligible
       print("Could not understand audio")

def speak(sent,rate = 150):
    import pyttsx
    engine = pyttsx.init()
    engine.setProperty('rate',rate)
    voiceid = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
    engine.setProperty('voice', voiceid)
    engine.say(sent)
    engine.runAndWait()
    engine.stop()

def tracktrain(route,station,destination):
    trainlink ='http://mumbailifeline.com/timetable.php?sel_route='+route+'&sfrom='+station+'&sto='+destination+'&time1=7%3A00+AM&time2=9%3A00&Submit=Submit'     
    filename = str(station+"-To-"+destination+".html")
    get(trainlink,filename)
    """
    page = urllib2.urlopen(trainlink)
    soup = BeautifulSoup(page)
    x = soup.body.find(id='static-style')
    try:
        y = re.findall(r'<strong.*?>(.*?)</strong>', str(x))
        print y
        speak("Total Distance of the journey is "+str(y[2])+" kilometers")
        speak("Ticket for First Class is "+str(y[3])+" Rupees")
        speak("Ticket for Second Class is "+str(y[4])+" Rupees")
        speak("Total Trains Found are "+str(y[5])+" in number")
    except:
        speak("Sorry no information is available.")
    """

def updatestations(route):
    global stationlist
    mainlink = 'http://mumbailifeline.com/index.php?sel_route='+route+'&sfrom=Mumbai_CST&sto=Mumbai_CST&time1=7%3A00+AM&time2=9%3A00'
    page = urllib2.urlopen(mainlink)
    soup = BeautifulSoup(page)
    x = soup.body.find(id='sfrom')
    stationlist = re.findall(r'"([^"]*)"', str(x))
    #FILE SAVING FOR DEBUGGING AND OFFLINE USE
    """
    filename = route+'_stations.txt' 
    f = open(filename,'w')
    for i in stationlist:
        f.write(i+"\n")
    f.close()
    """
def decode_stations(de):
    if de == "sandhurst" or de == "Sandhurst":
        de = "Sandhurst_Road"
        return de
    elif de == "cotton" or de == "Cotton":
        de = "Cottan_Green"
        return de
    elif de == "victoria" or de == "Victoria":
        de = "Mumbai_CST"
        return de
    elif de == "victoria" or de == "Victoria":
        de = "Mumbai_CST"
        return de
    elif de == "victoria" or de == "Victoria":
        de = "Mumbai_CST"
        return de
    elif de == "carry" or de == "Carry":
        de = "Currey_Road"
        return de
    else:
        return de


def getdatabase(route):
    global stationlist
    updatestations(route)
    for c in range(33,len(stationlist),1):
        for j in range(15,len(stationlist),1):
            if stationlist[c] != "sfrom" and stationlist[j] != "sfrom" and stationlist[c] != "selected" and stationlist[j] != "selected" and stationlist[c] != stationlist[j]:
                print stationlist[c]," TO ",stationlist[j]
                tracktrain(route,stationlist[c],stationlist[j])
"""
while True:
    route = ""
    sent = ""
    source = ""
    dest = ""
    stationlist = []
    speak("Tell me the route to go on")
    route = STT(route)
    route = route.lower()
    print "UPDATING DATABASE FOR "+route
    if route != "central" and route!="harbour" and route!="thane vashi" and route!="western":
        speak("Sorry Wrong information entered")
        continue
        
    if route == "thane vashi":
        updatestations("thane_vashi")
    updatestations(route)
    speak("Now Tell me the source and destination")
    sent = STT(sent)
    a = sent.split(" ")
    source = a[0]
    dest = a[2]
    source = decode_stations(source)
    dest = decode_stations(dest)
    source = source[0].upper()+source[1:]
    dest = dest[0].upper()+dest[1:]
    print "TRACKING TRAINS FROM "+source+" To "+dest + " on " +route+" route"
    tracktrain(route,source,dest)
    print "DONE."

"""
getdatabase("harbour")
