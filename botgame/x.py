from xx import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
import time, random, requests, json, traceback, sys, re, subprocess, threading, livejson
app = "DESKTOPMAC\t5.11.1\tbyupy\t12"
cl = LINE(appName=app)
clm = cl.profile.mid;oepoll = OEPoll(cl)
alreadyLogin = []
def lineBot(op):
    try:
        if op.type == 25 or op.type == 26:
            msg = op.message
            if msg.text is None:
                return
            elif msg.text.lower().startswith("login"):
                alreadyLogin.append(msg._from)
                def thr():
                    try:
                        cl.findAndAddContactsByMid(msg._from)
                        cl.sendMentionV2(msg.id, msg.to, "@! ลิงค์ของคุณถูกส่งไปยังแชตส่วนตัว", [msg._from])
                        j = LINE(_to=msg._from, _client=cl, appName="DESKTOPMAC\t5.11.1\tbyupy\t12")
                        cmd = f"python3 ln.py {j.authToken}"
                        sid = subprocess.Popen(cmd.split(" "))
                        currentLogging[msg._from] = sid
                    except Exception as e:
                        print(e)
                        alreadyLogin.remove(msg._from)
                s = threading.Thread(target=thr)
                s.daemon = True
                s.start()
    except Exception as error:
        print(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        print(e)
