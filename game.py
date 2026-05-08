import random
import pygame
import json
tl=["что","это","как","о","ура","спасибо","нет","да","помоги","мне","страшно","а","я","боюсь","больно","плохо"]
spritesheet=["sashadef","sashasad","sussasha","sashagood","sashashock","sashashock2","sashashocked","sashascary","sashascary2"]
def tokenise(text,tokenslist):
    txts=text.split(" ")
    tokenret=[]
    for t in txts:
        try:
            tokenslist.index(t)
        except:
            pass
    return tokenret
def detokenise(tokens,tokenslist):
    tokenret=""
    for t in tokens:
        t=int(t)
        while t > len(tokenslist)-1:
            t=t-len(tokenslist)
        while t < 0:
            t=t+len(tokenslist)
        try:
            tokenret=tokenret+" "+tokenslist[t]
        except:uwuo=0
    return tokenret
def match(inp,ws,outsc):
    out=[]
    outi=[]
    for o in range(outsc):
        outi.append([])
    for ind,i in enumerate(inp):
        outi.append([])
        for iwww,w in enumerate(ws[ind]):
            outi[iwww].append(w*i)
    for o in outi:
        out.append(sum(o))
    return out
def learn(eps,exps,inpexs):
    wvars=[]
    wvarsmis=[]
    for e in range(eps):
        wvar=[]
        nmis=0
        for i in range(len(inpexs[0])):
            wvar.append([])
            for o in range(len(exps[0])):
                wvar[i].append(random.uniform(-1.0000, 1.0000))
        for i,o in enumerate(exps):
            for iooo,ot in enumerate(match(inpexs[i],wvar,len(o))):
                try:
                    if int(ot)==o[iooo]: 
                        nmis+=1
                    else:
                        while int(ot)>16:
                            ot-=16
                        while int(ot)<0:
                            ot+=16
                        if int(ot)-16==o[iooo]:
                            nmis+=1
                except:pass
                print("e:"+str(e)+", nonmistake: "+str(nmis))
        wvarsmis.append(nmis)
        wvars.append(wvar)
    for i,nmis in enumerate(wvarsmis):
        if nmis==max(wvarsmis):
            return wvars[i]          
lastpain=0
lastfear=0
mood=100
angry=0
fear=0
love=50
pain=0
objtype=0
objtypes=["bed","TV","saw","box"]
inexs=[[100,0,0,50,0],[50,50,50,10,0],[10,30,30,15,0],[20,60,70,1,75],[25,100,75,25,99],[100,5,100,0]]
oexs=[[4,4,100,0,0,75,0],[10,16,49,50,40,30,4],[10,11,29,40,20,10],[10,15,10,90,100,1,7],[10,15,24,100,79,25,7],[4,5,100,1,100,0,3]]
#oexs=[[4,4,0],[10,16,4],[10,11,10],[10,15,7],[10,15,7],[4,5,3]]
epsn=input("epoches number: ")
try:
    int(epsn)
except: 
    epsn=ord(epsn)
ws=learn(int(epsn),oexs,inexs)
sashamove=False
for i in inexs:
    print(detokenise(match(i,ws,6)[:2],tl))
pygame.init()
objs=[{"type":"saw","pos":(0,0),"rotate":0},{"ftime":0,"y1":500,"type":"box","c":True,"pos":[0,500],"rotate":0},{"ftime":0,"y1":500,"type":"box","c":True,"pos":[50,500],"rotate":0},{"ftime":0,"y1":500,"type":"box","c":True,"pos":[100,500],"rotate":0},{"ftime":0,"y1":500,"type":"box","c":True,"pos":[150,500],"rotate":0},{"ftime":0,"y1":500,"type":"box","c":True,"pos":[200,500],"rotate":0},{"ftime":0,"y1":500,"type":"box","c":True,"pos":[250,500],"rotate":0},{"ftime":0,"y1":500,"type":"box","c":True,"pos":[300,500],"rotate":0},{"ftime":0,"y1":500,"type":"box","c":True,"pos":[350,500],"rotate":0},{"ftime":0,"y1":500,"type":"box","c":True,"pos":[400,500],"rotate":0},{"ftime":0,"y1":500,"type":"box","c":True,"pos":[450,500],"rotate":0}]
frame=pygame.display.set_mode((500,500))
sashx=150
sashy=150
run=True
frametv=0
sashapos=(250,250)
objin=False
pygame.display.set_icon(pygame.image.load("textures/sashadef.png"))
pygame.display.set_caption("AI playground")
while run:
    sashyl=str(sashy)
    if sashy<450:
        objin=False
        for o in objs:
            if int(o["pos"][0]) in range(int(sashx-50),int(sashx+50)) and not objin:
                objxl=[]
                for o2 in objs:
                    if o2["type"]=="box" and int(o2["pos"][0]) in range(int(sashx-50),int(sashx+50)):objxl.append(o2["pos"][1])
                if o["type"]=="box" and int(sashy)<o["pos"][1]-50 and o["pos"][1]==min(objxl):
                    #objin=True
                    sashy+=1
#    if sashyl==str(sashy) and sashy<450:
#        sashy+=0
# this=is(" madden by", "KecoBcTaBpo")
#        print(str(sashy)+";"+sashyl)
    if lastpain==pain and pain>0:
        pain-=1
    lastpain=pain
    frame.fill((50,125,230))
    #mood,angry,fear,love,pain=match([mood,angry,fear,love,pain],ws,7)[1:6]
    while mood>100:
        mood-=100
    while angry>100:
        angry-=100
    while fear>100:
        fear-=100
    while love>100:
        love-=100
    while pain>100:
        pain-=100
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            run=False
        if e.type==pygame.FINGERDOWN:
            pygame.key.start_text_input()
        if e.type==pygame.KEYDOWN:
            sashamove=False
            if e.key==pygame.K_r:
                mp=list(pygame.mouse.get_pos())
                for o in objs:
                    if int(mp[0]) in range(int(o["pos"][0]),int(o["pos"][0]+50)) and int(mp[1]) in range(int(o["pos"][1]),int(o["pos"][1]+50)):objs.remove(o)
            if e.key==pygame.K_s:
                fln=input("save's name: ")
                open(fln+".json","w").write(json.dumps(ws))
            if e.key==pygame.K_l:
                fln=input("save's name: ")
                ws=json.load(open(fln+".json","r"))
            if e.key==pygame.K_1:
                objtype=0
            elif e.key==pygame.K_2:
                objtype=1
            elif e.key==pygame.K_3:
                objtype=2
            elif e.key==pygame.K_4:
                objtype=3
            else:
                objtype=0
        if e.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] in range(sashx,sashx+50) and pygame.mouse.get_pos()[1] in range(sashy,sashy+50) and sashamove==False:
                sashamove=True
            if sashamove==True:
                sashsmove=False
                sashx,sashy=pygame.mouse.get_pos()
            if not pygame.mouse.get_pos()[0] in range(sashx,sashx+50) and not pygame.mouse.get_pos()[1] in range(sashy,sashy+50) and sashamove==False:
                obj={"c":False,"y1":pygame.mouse.get_pos()[1],"type":objtypes[objtype],"pos":list(pygame.mouse.get_pos()),"rotate":0, "ftime":0}
                objs.append(obj)
    for obj in objs:
        if obj["type"]=="saw":
            obj["rotate"]+=50
            frame.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("textures/saw.png"),(50,50)),obj["rotate"]),obj["pos"])     
            if obj["pos"][0] in range(sashx-200,sashx+200):
                if obj["pos"][1] in range(sashy-100,sashy+100):
                    fear=(200-int((abs(obj["pos"][0]-sashx)+abs(obj["pos"][1]-sashy))//2))/2
                    love=(int((abs(obj["pos"][0]-sashx)+abs(obj["pos"][1]-sashy))//2))/2
            if obj["pos"][0] in range(sashx-100,sashx+100):
                if obj["pos"][0] in range(sashx-25,sashx+25):
                    if obj["pos"][1] in range(sashy-25,sashy+25) and not pain>=100:
                        pain+=1
                        if angry<99.5:
                            angry+=0.5
                        if mood>0:
                            mood-=0.5
        if obj["type"]=="TV":
            #obj["rotate"]+=50
            if frametv==0:
                frame.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("textures/TV1.png"),(50,50)),obj["rotate"]),obj["pos"])
                frametv=1
            else:
                frame.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("textures/TV2.png"),(50,50)),obj["rotate"]),obj["pos"])
                frametv=0
            objin=False
            if obj["pos"][1]<450:
                for o in objs:
                    objin=False
            for o in objs:
                if int(o["pos"][0]) in range(int(obj["pos"][0]-50),int(obj["pos"][0]+50)) and not objin:
                    objxl=[]
                    for o2 in objs:
                        if not int(o2["pos"][1])==int(obj["pos"][1]) and int(o2["pos"][0]) in range(int(obj["pos"][0]-50),int(obj["pos"][0]+50)) and o2["type"]=="box":objxl.append(o2["pos"][1])
                    if o["type"]=="box" and int(obj["pos"][1])<o["pos"][1]-50 and o["pos"][1]==min(objxl):
                    #objin=True
                        obj["ftime"]+=0.01
            obj["pos"][1]=obj["y1"]+(98.1*(obj["ftime"]**2))/2
            if int(obj["pos"][0]) in range(int(sashx-200),int(sashx+200)):
                if int(obj["pos"][1]) in range(int(sashy-100),int(sashy+100)):
                    love=(200-int((abs(obj["pos"][0]-sashx)+abs(obj["pos"][1]-sashy))//2))/2
                    if mood<100:
                        mood+=(200-int((abs(obj["pos"][0]-sashx)+abs(obj["pos"][1]-sashy))//2))/100
        if obj["type"]=="bed":
            #obj["rotate"]+=50
            objin=False
            for o in objs:
                if int(o["pos"][0]) in range(int(obj["pos"][0]-50),int(obj["pos"][0]+50)) and not objin:
                    objxl=[]
                    for o2 in objs:
                        if not int(o2["pos"][1])==int(obj["pos"][1]) and int(o2["pos"][0]) in range(int(obj["pos"][0]-50),int(obj["pos"][0]+50)) and o2["type"]=="box":objxl.append(o2["pos"][1])
                    if o["type"]=="box" and int(obj["pos"][1])<o["pos"][1]-50 and o["pos"][1]==min(objxl):
                    #objin=True
                        obj["ftime"]+=0.01
            obj["pos"][1]=obj["y1"]+(0+98.1*(obj["ftime"]**2))/2
            frame.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("textures/bed.png"),(50,50)),obj["rotate"]),obj["pos"])     
            if int(obj["pos"][0]) in range(int(sashx)-200,int(sashx)+200):
                if int(obj["pos"][1]) in range(int(sashy-100),int(sashy+100)):
                    love=(200-int((abs(obj["pos"][0]-sashx)+abs(obj["pos"][1]-sashy))//2))/2
                    fear=(int((abs(obj["pos"][0]-sashx)+abs(obj["pos"][1]-sashy))//2))/2
        if obj["type"]=="box":
            #obj["rotate"]+=50
            objin=False
            objin=False
            for o in objs:
                if int(o["pos"][0]) in range(int(obj["pos"][0]-50),int(obj["pos"][0]+50)) and not objin:
                    objxl=[]
                    for o2 in objs:
                        if not int(o2["pos"][1])==int(obj["pos"][1]) and int(o2["pos"][0]) in range(int(obj["pos"][0]-50),int(obj["pos"][0]+50)) and o2["type"]=="box":objxl.append(o2["pos"][1])
                    if o["type"]=="box" and int(obj["pos"][1])<o["pos"][1]-50 and o["pos"][1]==min(objxl):
                    #objin=True
                        obj["ftime"]+=0.01
                #if objin==False:
                #    obj["ftime"]+=0.01
            obj["pos"][1]=obj["y1"]+(0+98.1*(obj["ftime"]**2))/2
            frame.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("textures/box.png"),(50,50)),obj["rotate"]),obj["pos"])
    currentspriten=int(match([mood,angry,fear,love,pain],ws,7)[6])
    while currentspriten>=len(spritesheet)-1:
        currentspriten-=len(spritesheet)
    while currentspriten<0:
        currentspriten+=len(spritesheet)
    try:
        frame.blit(pygame.transform.scale(pygame.image.load("textures/"+spritesheet[currentspriten]+".png"),(50,50)),(sashx,sashy))
    except:
         frame.blit(pygame.transform.scale(pygame.image.load("textures/"+spritesheet[0]+".png"),(50,50)),(sashx,sashy))
    frame.blit(pygame.font.SysFont("arial",36).render(detokenise(match([mood,angry,fear,love,pain],ws,7)[:2],tl),True,(255,255,255)),(sashx+50,sashy))
    #frame.blit(pygame.font.SysFont("arial",36).render(str([mood,angry,fear,love,pain]),True,(255,255,255)),(sashx+50,sashy+30))
    #frame.blit(pygame.font.SysFont("arial",36).render(str(match([mood,angry,fear,love,pain],ws,7)),True,(255,255,255)),(sashx+50,sashy+50))
    #frame.blit(pygame.font.SysFont("arial",36).render(str(ws),True,(255,255,255)),(sashx+50,sashy+30))
    pygame.display.update()