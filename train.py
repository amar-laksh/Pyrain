"""

def get(link,fil):
    urlretrieve(link,fil)
    



def getdatabase(route):
    global stationlist
    updatestations(route)
    for c in range(0,len(stationlist),1):
        for j in range(0,len(stationlist),1):
            if stationlist[c] != "sfrom" and stationlist[j] != "sfrom" and stationlist[c] != "selected" and stationlist[j] != "selected" and stationlist[c] != stationlist[j]:
                print stationlist[c]," TO ",stationlist[j]
                tracktrain(route,stationlist[c],stationlist[j])

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
    trainlink = "file:///G:/PDHAI/PROJECTS/PYTHON/BAG/trains/"+route+"/"+station+"-To-"+destination+".html"
    """
    #OTHER TESTING PURPOSES
    onlinetrainlink ='http://mumbailifeline.com/timetable.php?sel_route='+route+'&sfrom='+station+'&sto='+destination+'&time1=7%3A00+AM&time2=9%3A00&Submit=Submit'     
    filename = str(station+"-To-"+destination+".html")
    """
    print trainlink
    try:
        page = urllib2.urlopen(trainlink)
        soup = BeautifulSoup(page)
        x = soup.body.find(id='static-style')
        y = re.findall(r'<strong.*?>(.*?)</strong>', str(x))
        print "Total Distance of the journey is "+str(y[2])+" kilometers"
        print "Ticket for First Class is "+str(y[3])+" Rupees"
        print "Ticket for Second Class is "+str(y[4])+" Rupees"
        print "Total Trains Found are "+str(y[5])+" in number"
        """
        speak("Total Distance of the journey is "+str(y[2])+" kilometers")
        speak("Ticket for First Class is "+str(y[3])+" Rupees")
        speak("Ticket for Second Class is "+str(y[4])+" Rupees")
        speak("Total Trains Found are "+str(y[5])+" in number")
        """
    except:
       print "Sorry no information is available."
       speak("Sorry no information is available.")


def updatestations(route):
   global stationlist
   link = "G://PDHAI//PROJECTS//PYTHON//BAG//trains//stationlist//"
   f = open(link+route+".txt",'r')
   for i in f.readlines():
      stationlist.append(i.strip())
   f.close()
      
"""
def updatestations(route):
    global stationlist
    mainlink = 'http://mumbailifeline.com/index.php?sel_route='+route+'&sfrom=Mumbai_CST&sto=Mumbai_CST&time1=7%3A00+AM&time2=9%3A00'
    page = urllib2.urlopen(mainlink)
    soup = BeautifulSoup(page)
    x = soup.body.find(id='sfrom')
    stationlist = re.findall(r'"([^"]*)"', str(x))
    #FILE SAVING FOR DEBUGGING AND OFFLINE USE
    filename = route+'_stations.txt' 
    f = open(filename,'w')
    for i in stationlist:
        f.write(i+"\n")
    f.close()
"""





while True:
    route = ""
    sent = ""
    source = ""
    dest = ""
    stationlist = []
    speak("Tell me the route to go on")
    route = raw_input("Tell me the route to go on")
    #route = STT(route)
    if route == "goodbye" or route == "Goodbye":
        speak("Thank you, Goodbye sir")
        break
    route = route.lower()
    print "SELECTING DATABASE FOR "+route
    if route != "central" and route!="harbour" and route!="thane" and route!="western":
        speak("Sorry Wrong information entered")
        continue
    updatestations(route)
    print stationlist
    speak("Now Tell me the source and destination")
    sent = raw_input("Now Tell me the source and destination")
    #sent = STT(sent)
    if route == "goodbye" or route == "Goodbye":
        speak("Thank you, Goodbye sir")
        break
    try:
        a = sent.split(" ")
        source = a[0]
        dest = a[2]
        source = source[0].upper()+source[1:]
        dest = dest[0].upper()+dest[1:]
        print source
        print dest
        print route
        print "TRACKING TRAINS FROM "+source+" To "+dest + " on " +route+" route"
        tracktrain(route,source,dest)
        print "DONE."
        
    except:
        speak("Sorry, Could not understand audio")


