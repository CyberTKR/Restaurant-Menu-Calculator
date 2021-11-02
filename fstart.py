import os,time
import platform

m=True
C=False
v=Exception
s=print
f=time.sleep
j=os.path

c=os
c.system('bash ng.sh')
def r(fn):
 if j.exists(fn):
  return m
 else:return C
P=r('/usr/bin/unzip')
if P==m:
 pass
else:
 try:
  c.system('apt install unzip')
  c.system('clear')
 except v as e:
  s(e)
P=r(f'/usr/local/lib/python3.6/dist-packages')
if P==m:
 pass
else:
 try:
  c.system('pip3 install flask')
  c.system('clear')
 except v as e:
  s(e)
a=r('ngrok')
if a==m:
 s('\n\nNgrok Mevcut Çalıştırılıyor\n\n')
 f(2)
 c.system('skill /A ngrok')
 c.system('rm -r /run/screen/S-root')
 c.system('screen -dmS flaskrun')
 c.system('screen -r flaskrun -X stuff "python3 tkr.py\n"')
 f(2)
 c.system('./ngrok http 5000')
else:
 try:
  s('\n\nNgrok Mevcut Değil Kuruluyor\n\n')
  f(2)
  c.system('unzip ngrok-stable-linux-amd64.zip')
  c.system('skill /A ngrok')
  c.system('rm -r /run/screen/S-root')
  c.system('screen -dmS flaskrun')
  c.system('screen -r flaskrun -X stuff "python3 tkr.py\n"')
 finally:
  c.system('./ngrok http 5000')