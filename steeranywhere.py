import time
import serial
import win32api
import win32con
import time
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import serial.tools.list_ports
com=list(serial.tools.list_ports.comports());
l=len(com)
print l
i=0
while i<l:
    print str(i)+":  "+com[i][1]
    i+=1
f=raw_input("Enter the number: ")
f=int(f)
comport=com[f][0]
pr='1'    
def press(direc):
    global pr
    if direc=='1':
        win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
        pr='1'
    elif direc=='2':
        win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x25,0 ,0 ,0)
        time.sleep(.09)
        win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
        pr='2'
    elif direc=='3':
        win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x25,0 ,0 ,0)
        #time.sleep(.05)
        #win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
        pr='3'
    elif direc=='4':
        win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x25,0 ,0 ,0)
        pr='4'
    elif direc=='8':
        win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x27,0 ,0 ,0)
        time.sleep(.09)
        win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
        pr='8'
    elif direc=='7':
        win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x27,0 ,0 ,0)
        #time.sleep(.05)
        #win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
        pr='7'
    elif direc=='6':
        win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x27,0 ,0 ,0)
        pr='6'
    elif direc=='5':
        press(pr);
    else:
        win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)


ser = serial.Serial(
    port=comport,
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
ll=0
ser.isOpen()
while True:
    line=ser.readline()
    print line
    if line[0]=='3':
        win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x26,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
        win32api.keybd_event(0x28,0 ,win32con.KEYEVENTF_KEYUP ,0)
        ser.close();
        break
    while True:
        fwd=line[0]
        direc=line[1]
        if fwd=='2':
            win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(0x26,0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(0x28,0 ,win32con.KEYEVENTF_KEYUP ,0)
            break
        elif fwd=='3':
            ll=1
            win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(0x26,0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(0x28,0 ,win32con.KEYEVENTF_KEYUP ,0)
            break
        line=ser.readline()
        print line
    if ll==1:
        ser.close()
        break
    while True:
        line=ser.readline()
        print line
        if len(line)>2:
            fwd=line[0]
            direc=line[1]
            if fwd=='1':
                win32api.keybd_event(0x28,0 ,win32con.KEYEVENTF_KEYUP ,0)
                win32api.keybd_event(0x26,0 ,0 ,0)
            elif fwd=='4':
                win32api.keybd_event(0x26,0 ,win32con.KEYEVENTF_KEYUP ,0)
                win32api.keybd_event(0x28,0 ,0 ,0)
            elif fwd=='2':
                win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
                win32api.keybd_event(0x26,0 ,win32con.KEYEVENTF_KEYUP ,0)
                win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
                win32api.keybd_event(0x28,0 ,win32con.KEYEVENTF_KEYUP ,0)
                break
            elif fwd=='3':
                ll=1
                win32api.keybd_event(0x25,0 ,win32con.KEYEVENTF_KEYUP ,0)
                win32api.keybd_event(0x26,0 ,win32con.KEYEVENTF_KEYUP ,0)
                win32api.keybd_event(0x27,0 ,win32con.KEYEVENTF_KEYUP ,0)
                win32api.keybd_event(0x28,0 ,win32con.KEYEVENTF_KEYUP ,0)
                break
            else:
                win32api.keybd_event(0x26,0 ,win32con.KEYEVENTF_KEYUP ,0)
                win32api.keybd_event(0x28,0 ,win32con.KEYEVENTF_KEYUP ,0)
            press(direc)
    if ll==1:
        ser.close()
        break
