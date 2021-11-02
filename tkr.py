from flask import Flask,render_template,request
import json,codecs

class CyberTKAppWrapper(object):
 app=Flask(__name__,template_folder='./templates',static_folder='./templates/static')
 def __init__(self,name):
  pass
 def run(self):
  self.app.run(debug=True)
 @app.route('/',methods=['POST','GET'])
 def L():
  return render_template("L.html")
 @app.route('/V',methods=['POST','GET'])
 def V():
  if request.method=='GET':
   return render_template("L.html")
  if request.method=='POST':
   topen=codecs.open("d.json","r","utf-8")
   t=json.load(topen)
   o=request.form['o']
   if o=="Special 2":
    t["adana"]+=2
    t["tavukpirzola"]+=2
    t["etpirzola"]+=2
    t["kanat"]+=4
    t["etsis"]+=2
    with open('d.json','w')as fp:
     json.dump(t,fp,ensure_ascii=False,sort_keys=True,indent=4)
    return render_template('L.html',adana=t["adana"],etpirzola=t["etpirzola"],etsis=t["etsis"],kanat=t["kanat"],köfte=t["köfte"],tavukgögüs=t["tavukgögüs"],tavukpirzola=t["tavukpirzola"],tavuksis=t["tavuksis"],calculation_success=True)
   if o=="Adana":
    t["adana"]+=2
    with open('d.json','w')as fp:
     json.dump(t,fp,ensure_ascii=False,sort_keys=True,indent=4)
    return render_template('L.html',adana=t["adana"],etpirzola=t["etpirzola"],etsis=t["etsis"],kanat=t["kanat"],köfte=t["köfte"],tavukgögüs=t["tavukgögüs"],tavukpirzola=t["tavukpirzola"],tavuksis=t["tavuksis"],calculation_success=True)
   if o=="Etpirzola":
    t["etpirzola"]+=3
    with open('d.json','w')as fp:
     json.dump(t,fp,ensure_ascii=False,sort_keys=True,indent=4)
    return render_template('L.html',adana=t["adana"],etpirzola=t["etpirzola"],etsis=t["etsis"],kanat=t["kanat"],köfte=t["köfte"],tavukgögüs=t["tavukgögüs"],tavukpirzola=t["tavukpirzola"],tavuksis=t["tavuksis"],calculation_success=True)
   if o=="Etsis":
    t["etpirzola"]+=3
    with open('d.json','w')as fp:
     json.dump(t,fp,ensure_ascii=False,sort_keys=True,indent=4)
    return render_template('L.html',adana=t["adana"],etpirzola=t["etpirzola"],etsis=t["etsis"],kanat=t["kanat"],köfte=t["köfte"],tavukgögüs=t["tavukgögüs"],tavukpirzola=t["tavukpirzola"],tavuksis=t["tavuksis"],calculation_success=True)
   if o=="Kanat":
    t["kanat"]+=8
    with open('d.json','w')as fp:
     json.dump(t,fp,ensure_ascii=False,sort_keys=True,indent=4)
    return render_template('L.html',adana=t["adana"],etpirzola=t["etpirzola"],etsis=t["etsis"],kanat=t["kanat"],köfte=t["köfte"],tavukgögüs=t["tavukgögüs"],tavukpirzola=t["tavukpirzola"],tavuksis=t["tavuksis"],calculation_success=True)
   if o=="Köfte":
    t["köfte"]+=5
    with open('d.json','w')as fp:
     json.dump(t,fp,ensure_ascii=False,sort_keys=True,indent=4)
    return render_template('L.html',adana=t["adana"],etpirzola=t["etpirzola"],etsis=t["etsis"],kanat=t["kanat"],köfte=t["köfte"],tavukgögüs=t["tavukgögüs"],tavukpirzola=t["tavukpirzola"],tavuksis=t["tavuksis"],calculation_success=True)
   if o=="Tavukgögüs":
    t["tavukgögüs"]+=1
    with open('d.json','w')as fp:
     json.dump(t,fp,ensure_ascii=False,sort_keys=True,indent=4)
    return render_template('L.html',adana=t["adana"],etpirzola=t["etpirzola"],etsis=t["etsis"],kanat=t["kanat"],köfte=t["köfte"],tavukgögüs=t["tavukgögüs"],tavukpirzola=t["tavukpirzola"],tavuksis=t["tavuksis"],calculation_success=True)
   if o=="Tavukpirzola":
    t["tavukpirzola"]+=3
    with open('d.json','w')as fp:
     json.dump(t,fp,ensure_ascii=False,sort_keys=True,indent=4)
    return render_template('L.html',adana=t["adana"],etpirzola=t["etpirzola"],etsis=t["etsis"],kanat=t["kanat"],köfte=t["köfte"],tavukgögüs=t["tavukgögüs"],tavukpirzola=t["tavukpirzola"],tavuksis=t["tavuksis"],calculation_success=True)
   if o=="Tavuksis":
    t["tavuksis"]+=3
    with open('d.json','w')as fp:
     json.dump(t,fp,ensure_ascii=False,sort_keys=True,indent=4)
    return render_template('L.html',adana=t["adana"],etpirzola=t["etpirzola"],etsis=t["etsis"],kanat=t["kanat"],köfte=t["köfte"],tavukgögüs=t["tavukgögüs"],tavukpirzola=t["tavukpirzola"],tavuksis=t["tavuksis"],calculation_success=True)
   if o=="Karışık et":
    t["adana"]+=1
    t["etpirzola"]+=1
    t["etsis"]+=2
    t["köfte"]+=1
    with open('d.json','w')as fp:
     json.dump(t,fp,ensure_ascii=False,sort_keys=True,indent=4)
    return render_template('L.html',adana=t["adana"],etpirzola=t["etpirzola"],etsis=t["etsis"],kanat=t["kanat"],köfte=t["köfte"],tavukgögüs=t["tavukgögüs"],tavukpirzola=t["tavukpirzola"],tavuksis=t["tavuksis"],calculation_success=True)
   if o=="Reset":
    t["adana"]=0
    t["etpirzola"]=0
    t["etsis"]=0
    t["kanat"]=0
    t["köfte"]=0
    t["tavukgögüs"]=0
    t["tavukpirzola"]=0
    t["tavuksis"]=0
    with open('d.json','w')as fp:
     json.dump(t,fp,ensure_ascii=False,indent=4)
    return render_template('L.html',adana=t["adana"],etpirzola=t["etpirzola"],etsis=t["etsis"],kanat=t["kanat"],köfte=t["köfte"],tavukgögüs=t["tavukgögüs"],tavukpirzola=t["tavukpirzola"],tavuksis=t["tavuksis"],calculation_success=True)
a=CyberTKAppWrapper('wrap')
a.run()