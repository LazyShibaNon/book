import tkinter as tk
from tkinter import messagebox

import hashlib
import requests
import os
import csv
from bs4 import BeautifulSoup 
from mypackage import myfuntion as my

def _booK():
    
    wiN1=tk.Toplevel(wiN)
    wiN1.title("收集資料")
    wiN1.geometry("200x150")
    
    btN1 = tk.Button(wiN1, text="關閉視窗",bg="Plum", font=("微軟正黑體", 13), width=12, height=1, command=wiN1.destroy)
    btN1.pack() 
    
    sBar=tk.Scrollbar(wiN1)
    sBar.pack(side=tk.RIGHT,fill=tk.Y)
    
    listBox=tk.Listbox(wiN1,width=400,height=200,bg="LemonChiffon", font=("微軟正黑體", 12,"bold"),yscrollcommand=sBar.set)
    listBox.pack(side=tk.BOTTOM,fill=tk.BOTH)
    sBar.config(command=listBox.yview)

    
    
    evenT2="Line_noupdate"
    myCode="6TJ7Zn6qr0xpzlqdNkDpW"
    

    myHead=my._headers()
    urL="https://www.books.com.tw/web/sys_saletopb/books/"
    htmL=requests.get(urL).text.encode("utf-8-sig")
    
    
    newHash=hashlib.md5(htmL).hexdigest()
    oldHash=""
    if os.path.exists("oldnews.txt"):
        with open("oldnews.txt","r") as filE:
            oldHash=filE.read()
    with open("oldnews.txt","w") as filE:
        filE.write(newHash)
    
    if newHash==oldHash:
        listBox.insert(tk.END,"資料未更新")
        valuE1= "焦急鬼，資料還沒更新，乖嘿再等等!!!"       
        urL_msg="https://maker.ifttt.com/trigger/"+evenT2+"/with/key/"+myCode+"?value1="+valuE1
        replY=requests.get(urL_msg)
        listBox.insert(tk.END,replY,"訊息傳送成功")

    else:
        rQ=requests.get(urL,headers=myHead).text
        souP=BeautifulSoup(rQ,"html5lib")
        with open("book.csv","a",newline="",encoding="utf-8-sig") as csvFile:
            writeR = csv.writer(csvFile)
            writeR.writerow(["書名","作者","超連結"])
            vI=1
            for mySoup in souP.find_all("li","item"):
                try:
                    bookName = mySoup.find("h4").a.text
                    bookWriter = mySoup.ul.li.text
                    bookUrl = mySoup.a["href"]
                    writeR.writerow([bookName,bookWriter,bookUrl])
                    vI=vI+1
                except:
                    continue
        listBox.insert(tk.END,"資料更新成功")
        valuE1="懶鬼，來看看最新的暢銷排行榜吧!!"
        urL_msg="https://maker.ifttt.com/trigger/"+evenT2+"/with/key/"+myCode+"?value1="+valuE1
        replY=requests.get(urL_msg)
        listBox.insert(tk.END,replY,"訊息傳送成功")


def _exIt():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if qQ:
        wiN.destroy()
    

wiN = tk.Tk()
wiN.title("~博客來暢銷書排行榜~")
wiN.geometry("300x200")
wiN.configure(bg="MistyRose")

lbL = tk.Label(wiN,text="暢銷書籍排行榜 ",bg="Tan", font=("微軟正黑體", 20))
lbL.pack()

lbL2 = tk.Label(wiN,bg="MistyRose")
lbL2.pack()

btN1 = tk.Button(wiN, text="收集資料",bg="LightBlue", font=("微軟正黑體", 12), width=12, height=1, command=_booK)
btN1.pack()

lbL3 = tk.Label(wiN,bg="MistyRose")
lbL3.pack()

btN5 = tk.Button(wiN, text="離開",bg="Thistle", font=("微軟正黑體", 12), width=12, height=1, command=_exIt)
btN5.pack()

wiN.mainloop()
