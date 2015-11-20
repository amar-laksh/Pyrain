from PIL import Image
import urllib2
import time
import random
from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve
import ImageEnhance
from pytesser import *
import re
import os



url = ""

def updateurl(a):
    global url
    if a == "central":
        url = "d_central.txt"
    elif a == "western":
        url = "d_western.txt"
    elif a == "harbour":
        url = "d_harbour.txt"
    elif a == "thane":
        url = "d_thane.txt"

def convert(this,oldlocation):
    global url
    link = oldlocation
    updateurl(this)
    for i in open(url):
        j = i.strip()
        j = j.split(" ")
        old = j[0]
        new = j[2]
        if old in oldlocation:
            newlocation = oldlocation.replace(old,new,10)
            print "newlocation - >",newlocation
            os.rename(oldlocation,newlocation)
            oldlocation = newlocation

#convert("western","C:\\Users\\p\\Desktop\\trains\\VIRAR-To-Mira_Road.html")
files= os.listdir("C:\\Users\\p\\Desktop\\trains\\thane")
for i in files:
    html = "C:\\Users\\p\\Desktop\\trains\\thane\\"+i
    print i
    convert("thane",html)
    print "#####################################"
