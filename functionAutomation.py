import pyautogui as pya
from time import sleep
from extractNumbers import extractor
from playMusic import soundPlay
from readingWriting import saveNos,read, write
import os

url=r'''https://web.whatsapp.com/send?phone='''
def startAutomation(userList,sendMsgList):
    sleep(10)
    for index,user in enumerate(userList):
        pya.hotkey('ctrl','t')
        sleep(3)
        pya.write(url+user)
        sleep(1)
        pya.press('enter')
        sleep(35)
        pya.moveTo(600,740)
        pya.click()
        sleep(1)
        for msg in sendMsgList:
            if(":{") in msg:
                for index,i in enumerate(msg.split(":{")):
                    list2=i.split("}")
                    if(index>0):
                        pya.write(":"+list2[0])
                        sleep(1.5)
                        pya.press('enter')     
                        sleep(1)   
                        pya.write(list2[1])
                    else:
                        pya.write(list2[0])
                        sleep(1)
                sleep(1)
                pya.press('enter')
            else:
                pya.write(msg)
                sleep(0.3)
                pya.press('enter')
            sleep(1)
        sleep(12)
        pya.hotkey('ctrl','w')
        sleep(1)
        write("midProcessing.txt",str(userList[index:]))
        sleep(1)



def initAuto(inputImpureNosString:str,userMsgToSend:str):
    userList=extractor(inputImpureNosString)
    userList=list(map(lambda x:x.replace("+",""),userList))
    userList=set(userList)-set(read("previousNumbers.txt"))
    userList=list(userList)
    if not (os.path.isfile("midProcessing.txt")):
        write("midProcessing.txt",str(userList))
        
    print(f"Assuming 1 min for each you number you require:",len(read("midProcessing.txt")),"mins")
    
    startAutomation(userList=read("midProcessing.txt"),sendMsgList=userMsgToSend)
    os.remove("midProcessing.txt")
    saveNos(userList)
    while True:
        soundPlay('sfx1.mp3')
        sleep(3)
