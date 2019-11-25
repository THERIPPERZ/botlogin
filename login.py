
# -*- coding: utf-8 -*-
# Source Code : NoobLess Team #
# Arfine Meka.
# 
# -*- coding: utf-8 -*-
# ------------------------ IMPORT ------------------------ #

import time, random, sys, json, codecs, glob, urllib, pytz, ast, os, multiprocessing, subprocess, tempfile, string, six, urllib.parse, traceback, atexit, html5lib, re, wikipedia, ntpath, threading, base64, shutil, humanize, service, os.path, youtube_dl, requests
import urllib3
urllib3.disable_warnings()
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ------------------------ IMPORT ------------------------ #
from LineAPI.linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from LineAPI.akad import ChannelService,TalkService
from LineAPI.akad.ttypes import Message, Location, LoginRequest, ChatRoomAnnouncementContents, ContentType as Type
from thrift.protocol import TCompactProtocol, TBinaryProtocol, TProtocol
from thrift.transport import THttpClient, TTransport
from thrift.Thrift import TProcessor
from multiprocessing import Pool, Process
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread, activeCount
from time import sleep
from datetime import datetime, timedelta
from humanfriendly import format_timespan, format_size, format_number, format_length
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# ------------------------ LOGIN ------------------------ #
programStart = time.time()
client = LINE("")
client.log("Auth Token : " + str(client.authToken))
client.log("Timeline Token : " + str(client.tl.channelAccessToken))
clientMid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
mid = client.getProfile().mid
clientPoll = OEPoll(client)
botStart = time.time()
msg_send = {}
temp_flood = {}
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
creator = ['u406577b5a4fc096f85dfbcace7dec8a4','u637ee64df76580c741de37cc238fc17b']
adminbots = ['u406577b5a4fc096f85dfbcace7dec8a4','u637ee64df76580c741de37cc238fc17b']
superz = creator + adminbots
with open('by.json', 'r') as fp:
    wait = json.load(fp)
settings ={"keyCommand":"","setKey":False}

xxxs = {
    "clock": False,
    "cName":"",
    }

def tokenchrome():
    Headers = {
    'User-Agent': "Line/2.1.5",
    'X-Line-Application': "CHROMEOS\t2.1.5\tlognselfbot\t12.1.1",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def headersios():
    Headers = {
    'User-Agent': "Line/8.9.0",
    'X-Line-Application': "IOSIPAD\t11.2.5\tiPhone X\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
    return Headers

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
        
def backupData():
    try:
        backup = wait
        f = codecs.open('by.json','w','utf-8')
        json.dump(wait, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except:
        e = traceback.format_exc()
        client.sendMessage("u216a12909d301680792bd786f773e720",str(e))
        return False

def sendPost(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendMention(to, text="", mids=[]):
        arrData = ""
        arr = []
        mention = "@Arfinee Meka "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def menumessage():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuMessage =   "「 คำสั่งบอทล็อคอิน 」" + "\n\n" + \
                    "•  คำสั่งบอท >「ดูเมนูคำสั่ง 」" + "\n" + \
                    "•  ล็อคอิน1 > 「 เข้าสู่ระบบ 」" + "\n" + \
                    "•  ล็อคอิน2 > 「 เข้าสู่ระบบ 」" + "\n" + \
                    "•  ออกระบบ > 「 ออกระบบ」" + "\n" + \
                    "•  รายชื่อ >「เชคชื่อลูกค้า」" + "\n" + \
                    "•  ต่ออายุ @「 ต่อวันใช้งาน 」" + "\n" + \
                    "•  เพิ่ม @「เพิ่มลูกค้า」" + "\n" + \
                    "•  เพิ่ม1วัน @「 เล่นชั่วคราว 」" + "\n" + \
                    "•  ลบ @  「ลบลูกค้า」" + "\n" + \
                    "•  /ออน「 เชคออนบอท 」" + "\n" + \
                    "•  /รีบอท >แอดมินสั่ง<" + "\n" + \
                    "「 ֆҽlßօℓ BY: •₮€₳M•𖤍ĿɪϰüXཽ 」"
    return menuMessage
    
def clientBot(op):
    try:
        if op.type == 0:
            return   
                
        if op.type == 13:
            if op.param2 in superz:
                client.acceptGroupInvitation(op.param1)

        #if op.type in [22,24]:
         #   client.leaveRoom(op.param1)

        if op.type == 26:
            try:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    if msg.toType == 1:
                        to = receiver
                    if msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            pass
                        else:
                            cmd = command(text)
                            if text.lower().startswith('# ') and sender in ['u406577b5a4fc096f85dfbcace7dec8a4']:
                                a=subprocess.getoutput(client.mainsplit(msg.text))
                                k = len(a)//10000
                                for aa in range(k+1):
                                    try:
                                        client.generateReplyMessage(msg.id)
                                        client.sendReplyMessage(msg.id,to,'{}'.format(a.strip()[aa*10000 : (aa+1)*10000]))
                                    except:
                                        client.sendMessage(to, "Done")

                            if text.lower() == "renew" and sender in ['u406577b5a4fc096f85dfbcace7dec8a4']:
                                try:
                                    sam = {'MSG_SENDER_ICON': "https://os.line.naver.jp/os/p/"+sender,'MSG_SENDER_NAME':  client.getContact(sender).displayName,}                            
                                    client.sendMessage(to, "Update Library Done", contentMetadata=sam)
                                    restartBot()
                                except:
                                    e = traceback.format_exc()
                                    client.sendMessage("u406577b5a4fc096f85dfbcace7dec8a4",str(e))

                            if text.lower().startswith('เพิ่ม ') and sender in sender in ['u406577b5a4fc096f85dfbcace7dec8a4','u637ee64df76580c741de37cc238fc17b']:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 not in wait['info']:
                                        pay = time.time()
                                        nama = str(text.split(' ')[1])
                                        wait['name'][nama] =  {"mid":key1,"pay":pay+60*60*24*30,"runtime":pay,"token":{}}
                                        wait['info'][key1] =  '%s' % nama
                                        sendMention(msg.to, ' 「 Serivce 」\n@! เพิ่มผู้ใช้สำเร็จ\nอย่าลืมปิด letter sealing ในตั้งค่าความเป็นส่วนตัว',[key1])
                                    else:
                                        sendMention(msg.to, ' 「 Serivce 」\n@! บัญชีผู้ใช้นี้อยู่ในระบบแล้ว',[key1])
                                        
                            if text.lower().startswith('เพิ่ม1วัน ') and sender in ['u406577b5a4fc096f85dfbcace7dec8a4','u637ee64df76580c741de37cc238fc17b']:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 not in wait['info']:
                                        pay = time.time()
                                        nama = str(text.split(' ')[1])
                                        wait['name'][nama] =  {"mid":key1,"pay":pay+60*60*24*1,"runtime":pay,"token":{}}
                                        wait['info'][key1] =  '%s' % nama
                                        sendMention(msg.to, ' 「 Serivce 」\n@! เพิ่มผู้ใช้สำเร็จ\nอย่าลืมปิด letter sealing ในตั้งค่าความเป็นส่วนตัว',[key1])
                                    else:
                                        sendMention(msg.to, ' 「 Serivce 」\n@! บัญชีผู้ใช้นี้อยู่ในระบบแล้ว',[key1])
                                        
                            if text.lower().startswith('delsb') and sender in ['u406577b5a4fc096f85dfbcace7dec8a4']:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                aa = [a for a in wait['info']]
                                try:
                                    listContact = aa[int(query)-1]
                                    if listContact in wait['info']:
                                        b = wait['info'][listContact]
                                        os.system('screen -S %s -X kill'%b)
                                        try:subprocess.getoutput('rm -rf {}'.format(b))
                                        except:pass
                                        del wait['info'][listContact]
                                        del wait['name'][b]
                                        sendMention(to, ' 「 Serivce 」\n@! ลบรายชื่อนี้ออกจากระบบแล้ว', [listContact])
                                    else:
                                        sendMention(to, ' 「 Serivce 」\n@! ไม่พบรายชื่อนี้ในระบบ', [listContact])
                                except:pass

                            if text.lower().startswith('ลบ ') and sender in ['u406577b5a4fc096f85dfbcace7dec8a4','u637ee64df76580c741de37cc238fc17b']:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 in wait['info']:
                                        b = wait['info'][key1]
                                        os.system('screen -S %s -X kill'%b)
                                        try:subprocess.getoutput('rm -rf {}'.format(b))
                                        except:pass
                                        del wait['info'][key1]
                                        del wait['name'][b]
                                        sendMention(to, ' 「 Service 」\n@! ทำการตัดรายชื่อนี้ออกจากระบบแล้ว',[key1])
                                    else:
                                        sendMention(to, ' 「 Serivce 」\n@! ไม่พบรายชื่อนี้ในระบบ', [key1])

                            if text.lower() == 'รายชื่อ' and sender in ['u406577b5a4fc096f85dfbcace7dec8a4','u637ee64df76580c741de37cc238fc17b']:
                                h = [a for a in wait['info']]
                                k = len(h)//20
                                for aa in range(k+1):
                                    if aa == 0:dd = '「 List Login 」';no=aa
                                    else:dd = '';no=aa*20
                                    msgas = dd
                                    for a in h[aa*20:(aa+1)*20]:
                                        no+=1
                                        if wait['name'][wait['info'][a]]["pay"] <= time.time():sd = 'หมดอายุ'
                                        else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
                                        if no == len(h):msgas+='\n{}. @! {}'.format(no,sd)
                                        else:msgas += '\n{}. @! {}'.format(no,sd)
                                    sendMention(to, msgas, h[aa*20:(aa+1)*20])

                            if text.lower() == 'killall':
                                if msg._from in ['u3493c05f288ca15d669be2e16269e8f4']:
                                    h = ''
                                    no=0
                                    for a in wait['info']:
                                        us = wait["info"][a]
                                        try:
                                            os.system('screen -S %s -X kill'%us)
                                        except:pass
                                    client.generateReplyMessage(msg.id)
                                    client.sendReplyMessage(msg.id,to,'Done Kill All Customer')

                            if text.lower() == "ออกระบบ":
                              if sender in wait['info']:
                                us = wait["info"][sender]
                                contact = client.getContact(sender)
                                os.system('screen -S {} -X quit'.format(us))
                                os.system('rm -rf {}'.format(us))
                                if msg.toType == 2:
                                    client.sendMessage(to, "Name: {}\nStatus: ทำการออกจากระบบแล้ว".format(contact.displayName))
                                else:
                                    sendMention(to, "「 แจ้งเตือน 」\nคุณได้ทำการออกจากระบบอยู่แล้ว @! ", [sender])
                              else:
                                sendMention(to, ' 「 เกิดข้อผิดพลาด 」\nHi @!\nไม่พบรายชื่อคุณในระบบ\nโปรดติดต่อแอดมิน @! ', [sender, "u637ee64df76580c741de37cc238fc17b"])

                            if text.lower() == "ล็อคอิน1":
                                client.generateReplyMessage(msg.id)
                                if sender in wait['info']:
                                        us = wait["info"][sender]
                                        ti = wait['name'][us]["pay"]-time.time()
                                        sec = int(ti %60)
                                        minu = int(ti/60%60)
                                        hours = int(ti/60/60 %24)
                                        days = int(ti/60/60/24)
                                        wait['name'][us]["pay"] = wait['name'][us]["pay"]
                                        if wait["name"][us]["pay"] <= time.time():
                                            os.system('rm -rf {}'.format(us))
                                            os.system('screen -S %s -X kill'%us)
                                            sendMention(to, ' 「 หมดอายุ 」\n Sorry @! บัญชีของคุณหมดเวลาใช้งานแล้วแล้ว', [sender])
                                        else:
                                            us = wait["info"][sender]
                                            try:
                                                def kentod():
                                                    a = headersios()
                                                    a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    qr = clients.getAuthQrcode(keepLoggedIn=1, systemName='Game')
                                                    link = "line://au/q/" + qr.verifier
                                                    sendMention(to,"「 Login 」\nUser: @!\nFile: {}".format(link), [sender])
                                                    a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                                    a.update({'x-lpqs' : '/api/v4p/rs'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    req = LoginRequest()
                                                    req.type = 1
                                                    req.verifier = qr.verifier
                                                    req.e2eeVersion = 1
                                                    res = clients.loginZ(req)
                                                    wait['name'][us]["token"] = res.authToken
                                                    token = wait['name'][us]["token"]
                                                    os.system('screen -S %s -X kill'%us)
                                                    os.system('cp -r botgame {}'.format(us))
                                                    os.system('cd {} && echo -n "{} \c" > token.txt'.format(us, token))
                                                    os.system('screen -dmS {}'.format(us))
                                                    os.system('screen -r {} -X stuff "cd {} && python3 ln.py \n"'.format(us, us))
                                                    contact = client.getContact(sender)
                                                    sendMention(to, "「「 Done! 」\nName: {}\nMid: {}\nเวลาคงเหลือ: {} วัน {} ชั่วโมง {} นาที \nSuccess login user @! \n> กรุณากดลิ้งด้านล่างด้วย(กดแค่ครั้งแรกพอ) :\line://app/1602687308-GXq4Vvk9?type=text&text=•₮€₳M•𖤍ĿɪϰüXཽ".format(us,sender,days,hours,minu), [sender])
                                                thread = threading.Thread(target=kentod)
                                                thread.daemon = True
                                                thread.start()
                                            except:
                                                pass
                                else:
                                    sendMention(to, ' 「 Error 」\nHi @!\nไม่พบรายชื่อคุณในระบบ\nโปรดติดต่อแอดมิน @! ', [sender, "u637ee64df76580c741de37cc238fc17b"])

                            if text.lower() == "ล็อคอิน2":
                                client.generateReplyMessage(msg.id)
                                if sender in wait['info']:
                                        us = wait["info"][sender]
                                        ti = wait['name'][us]["pay"]-time.time()
                                        sec = int(ti %60)
                                        minu = int(ti/60%60)
                                        hours = int(ti/60/60 %24)
                                        days = int(ti/60/60/24)
                                        wait['name'][us]["pay"] = wait['name'][us]["pay"]
                                        if wait["name"][us]["pay"] <= time.time():
                                            os.system('rm -rf {}'.format(us))
                                            os.system('screen -S %s -X kill'%us)
                                            sendMention(to, ' 「 หมดอายุ 」\n Sorry @! บัญชีของคุณหมดเวลาใช้งานแล้วแล้ว', [sender])
                                        else:
                                            us = wait["info"][sender]
                                            try:
                                                def kentod():
                                                    a = headersios()
                                                    a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    qr = clients.getAuthQrcode(keepLoggedIn=1, systemName='Game')
                                                    link = "line://au/q/" + qr.verifier
                                                    sendMention(to,"「 Login 」\nUser: @!\nFile: {}".format(link), [sender])
                                                    a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                                    a.update({'x-lpqs' : '/api/v4p/rs'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    req = LoginRequest()
                                                    req.type = 1
                                                    req.verifier = qr.verifier
                                                    req.e2eeVersion = 1
                                                    res = clients.loginZ(req)
                                                    wait['name'][us]["token"] = res.authToken
                                                    token = wait['name'][us]["token"]
                                                    os.system('screen -S %s -X kill'%us)
                                                    os.system('cp -r du1 {}'.format(us))
                                                    os.system('cd {} && echo -n "{} \c" > token.txt'.format(us, token))
                                                    os.system('screen -dmS {}'.format(us))
                                                    os.system('screen -r {} -X stuff "cd {} && python3 online.py \n"'.format(us, us))
                                                    contact = client.getContact(sender)
                                                    sendMention(to, "「「 Done! 」\nName: {}\nMid: {}\nเวลาคงเหลือ: {} วัน {} ชั่วโมง {} นาที \nSuccess login user @! \n> กรุณากดลิ้งด้านล่างด้วย(กดแค่ครั้งแรกพอ) :\line://app/1602687308-GXq4Vvk9?type=text&text=•₮€₳M•𖤍ĿɪϰüXཽ".format(us,sender,days,hours,minu), [sender])
                                                thread = threading.Thread(target=kentod)
                                                thread.daemon = True
                                                thread.start()
                                            except:
                                                pass
                                else:
                                    sendMention(to, ' 「 Error 」\nHi @!\nไม่พบรายชื่อคุณในระบบ\nโปรดติดต่อแอดมิน @! ', [sender, "u637ee64df76580c741de37cc238fc17b"])
                            if text.lower() == 'เพิ่มฉัน' and sender in ['u637ee64df76580c741de37cc238fc17b']:
                                try:
                                    wait['name'][wait['info'][sender]]['pay'] = wait['name'][wait['info'][sender]]['pay']+60*60*24*30
                                    sendMention(to, ' 「 Serivce 」\nHello @! your expired selfbot now {}'.format(humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][msg._from]]["pay"]))),[msg._from])
                                except:
                                    e = traceback.format_exc()
                                    client.sendMessage("u637ee64df76580c741de37cc238fc17b",str(e))

                            if text.lower() == "บายบอท" and sender in ['u406577b5a4fc096f85dfbcace7dec8a4','u637ee64df76580c741de37cc238fc17b']:
                                client.leaveGroup(to)

                            if text.lower().startswith('ต่ออายุ ') and sender in ['u406577b5a4fc096f85dfbcace7dec8a4','u637ee64df76580c741de37cc238fc17b']:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 in wait['info']:
                                        wait['name'][wait['info'][key1]]['pay'] = wait['name'][wait['info'][key1]]['pay']+60*60*24*30
                                        sendMention(to, ' 「 Serivce 」\nHi @! your expired selfbot now {}'.format(humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][key1]]["pay"]))), [key1])
                                    else:pass                                  
                                       
                            if text.lower() == "คำสั่งบอท":
                                menuMessage = menumessage()
                                client.generateReplyMessage(msg.id)
                                client.sendReplyMessage(msg.id,to,str(menuMessage))

                            if cmd == "/ออน":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                client.sendMessage(to, "「 Time to ֆҽlßօℓ 」\n"+str(runtime))
                                
                            if cmd == 'Jam on'and sender in ['u406577b5a4fc096f85dfbcace7dec8a4','u637ee64df76580c741de37cc238fc17b']:
                                if xxxs["clock"] == True:
                                    client.sendMessage(msg.to,"already on")
                                else:
                                    xxxs["clock"] = True
                                    now2 = datetime.now()
                                    nowT = datetime.strftime(now2,"(%H:%M:%S)")
                                    profile = client.getProfile()
                                    profile.displayName = xxxs["cName"] + nowT
                                    client.updateProfile(profile)
                                    client.sendMessage(msg.to,"done")
                                    
                            if cmd == 'Jam off'and sender in ['u406577b5a4fc096f85dfbcace7dec8a4','u637ee64df76580c741de37cc238fc17b']:
                                if xxxs["clock"] == False:
                                    client.sendMessage(msg.to,"already off")
                                else:
                                    xxxs["clock"] = False
                                    client.sendMessage(msg.to,"done")
                                    
                            if cmd == 'up'and sender in ['u406577b5a4fc096f85dfbcace7dec8a4','u637ee64df76580c741de37cc238fc17b']:
                                if xxxs["clock"] == True:
                                    now2 = datetime.now()
                                    nowT = datetime.strftime(now2,"(%H:%M)")
                                    profile = client.getProfile()
                                    profile.displayName = xxxs["cName"] + nowT
                                    client.updateProfile(profile)
                                    client.sendMessage(msg.to,"Jam Update")
                                else:
                                    client.sendMessage(msg.to,"Please turn on the name clock")

                            if cmd == 'grouplist'and sender in ['u406577b5a4fc096f85dfbcace7dec8a4','u637ee64df76580c741de37cc238fc17b']:
                                groups = client.groups
                                ret_ = "╭──[ Group List ]"
                                no = 0 
                                for gid in groups:
                                    group = client.getGroup(gid)
                                    ret_ += "\n│ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                    no += 1
                                ret_ += "\n╰──[ Total {} Groups ]".format(str(len(groups)))
                                k = len(ret_)//10000
                                for aa in range(k+1):
                                    client.sendMessage(to,'{}'.format(ret_[aa*10000 : (aa+1)*10000]))
                            if text.lower() == 'rname'and sender in ['ใส่midแอดมิน']:
                                sendMention(to, "@!", [clientMid])

                            if cmd.startswith('joinme '):
                              if sender in ["u406577b5a4fc096f85dfbcace7dec8a4","u3493c05f288ca15d669be2e16269e8f4","u637ee64df76580c741de37cc238fc17b"]:
                               text = msg.text.split()
                               number = text[1]
                               if number.isdigit():
                                groups = client.getGroupIdsJoined()
                                if int(number) < len(groups) and int(number) >= 0:
                                    groupid = groups[int(number)]
                                    group = client.getGroup(groupid)
                                    target = sender
                                    try:
                                        client.getGroup(groupid)
                                        client.findAndAddContactsByMid(target)
                                        client.inviteIntoGroup(groupid, [target])
                                        client.sendMessage(msg.to,"Succes invite to " + str(group.name))
                                    except:
                                        client.sendMessage(msg.to,"I no there baby")
                                    
                            if text.lower() == "/รีบอท" and sender in ['u406577b5a4fc096f85dfbcace7dec8a4','u637ee64df76580c741de37cc238fc17b']:
                                try:
                                    sam = {'MSG_SENDER_ICON': "https://os.line.naver.jp/os/p/"+sender,'MSG_SENDER_NAME':  client.getContact(sender).displayName,}                            
                                    client.sendMessage(to, "รีเซ็ตระบบใหม่เรียบร้อบ\n[ล็อคอินใหม่เพื่อเข้าสู่ระบบเชลบอท]​", contentMetadata=sam)
                                    restartBot()
                                except:
                                    e = traceback.format_exc()
                                    client.sendMessage("u637ee64df76580c741de37cc238fc17b",str(e))

                            if cmd.startswith('invme '):
                              if sender in ["u637ee64df76580c741de37cc238fc17b"]:
                                cond = cmd.split(" ")
                                num = int(cond[1])
                                gid = client.getGroupIdsJoined()
                                group = client.getCompactGroup(gid[num-1])
                                client.findAndAddContactsByMid(sender)
                                client.inviteIntoGroup(gid[num-1],[sender])

                            if cmd.startswith('unsend') and sender in ['u637ee64df76580c741de37cc238fc17b']:
                                try:
                                    args = text.split(' ')
                                    mes = 0
                                    try:
                                        mes = int(args[1])
                                    except:
                                        mes = 1
                                    M = client.getRecentMessagesV2(to, 1001)
                                    MId = []
                                    for ind,i in enumerate(M):
                                        if ind == 0:
                                            pass
                                        else:
                                            if i._from == clientMid:
                                                MId.append(i.id)
                                                if len(MId) == mes:
                                                    break
                                    for i in MId:
                                        client.unsendMessage(i)
#                                    client.sendMessage(to, '「 Unsend 」\nUnsend {} Message'.format(len(MId)))
                                except:
                                    e = traceback.format_exc()
                                    client.sendMessage("u637ee64df76580c741de37cc238fc17b",str(e))
            except:
                e = traceback.format_exc()
                client.sendMessage("u637ee64df76580c741de37cc238fc17b",str(e))
    except:
        e = traceback.format_exc()
        client.sendMessage("u637ee64df76580c741de37cc238fc17b",str(e))

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    profile = client.getProfile()    
    while True:
        try:
            if xxxs["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile.displayName = xxxs["cName"] + nowT
                client.updateProfile(profile)
            time.sleep(120)
            print("UpdateName",nowT) 
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.start()    

def run():
    while True:
        try:
            backupData()
            ops = clientPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                    threads = []
                    for i in range(1):
                        thread = threading.Thread(target=clientBot(op))
                        threads.append(thread)
                        thread.start()
                        clientPoll.setRevision(op.revision)
            for thread in threads:
                thread.join()
        except:
            pass
            
if __name__ == "__main__":
    run()