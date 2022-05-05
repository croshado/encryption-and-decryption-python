# encryption-and-decryption-python

#imports/library used------------------------------------------modules--
from curses import window
from tkinter import *
from stat import S_IREAD
import tkinter as tk
from tkinter import filedialog
import os
import stat

window=Tk()
window.title("Cryptography")
window.maxsize(width=1200,height=900)
window.minsize(width=1200,height=900)
window.configure(bg='#fff')
window.resizable(False,False)

img= PhotoImage(file='encryption.png')
Label(window, image=img, border=0, bg='white' ).place(x=50,y=40)

#-----------------------variablesdeclared----------------------------------------

Msg = StringVar()
wo=StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()
y= StringVar()
R=StringVar()
p_info=StringVar()
t=StringVar()
password=StringVar()
send=StringVar()
gpass=StringVar()
q=StringVar()
q=['','']
va=StringVar()
num = IntVar()



#---------------------------labels and entrybox------------------------------------------------------------------

lblMsg= Label(text='Text',fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light',14, 'bold'))
lblMsg.place(x=50,y=50)
entrymsg= Entry(width=25, textvariable=Msg ,fg='black', border=0 , bg='white',font=('Microsoft Yahei UI Light',11))
entrymsg.place(x=150,y=50)

Frame(width=208, height=2, bg='black').place(x=150,y=75)



#------------------------------------------------------------------------------------------------------------------
lbldatabase= Label(text='Database Details Saving', fg='#57a1f8',bg='white', font=('Microsoft Yahei UI Light',18, 'bold'))
lbldatabase.place(x=700,y=40)

#------------------------------------------------------------------------------------------------------------------
lblnum=Label(text='Access file', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light',14, 'bold'))
lblnum.place(x=650,y=100)
txtfilenum=Entry(width=25,textvariable=num,fg='black',border=0, bg='white', font=('Microsoft Yahei UI Light',11))
txtfilenum.place(x=770, y=100)

Frame(width=208, height=2, bg='black').place(x=770,y=125)

#-------------------------------------------------------------------------------------------------------------------

lblkey= Label(text='Key(int.)',fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light',14, 'bold'))
lblkey.place(x=50,y=100)
txtkey= Entry(width=25,textvariable=key ,fg='black', border=0 , bg='white',font=('Microsoft Yahei UI Light',11))
txtkey.place(x=150,y=100)

Frame(width=208, height=2, bg='black').place(x=150,y=125)

#--------------------------------------------------------------------------------------------------------------------

menu= StringVar()
menu.set("Choose Action")
drop= OptionMenu(window,menu,"Encrypt", "Decrypt","Encrypt file","Decrypt File","Decrypt standard file")

drop.place(x=175, y=150)

#-----------------------------------------------------------------------------------------------------------------------

lblfilename= Label(text='Filename*',fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light',14, 'bold'))
lblfilename.place(x=40,y=200)
txtfilename= Entry(width=25,textvariable=t, fg='black', border=0 , bg='white',font=('Microsoft Yahei UI Light',11))
txtfilename.place(x=150,y=200)

Frame(width=208, height=2, bg='black').place(x=150,y=225)

#------------------------------------------------------------------------------------------------------------------------

lblResult=Label(text='Result',fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light',14, 'bold'))
lblResult.place(x=55,y=270)
txtResult=Entry(width=25,textvariable=Result, fg='black', border=0 , state=DISABLED, disabledbackground='white' , bg='white',font=('Microsoft Yahei UI Light',11))
txtResult.place(x=150,y=270)

Frame(width=208, height=2, bg='black').place(x=150,y=295)

#-------------------------------------------------Functions---------------------------------------------------------------

def conditions():
    if menu.get()=='Encrypt':
        Encrypt()
    
    elif menu.get() == 'Decrypt':
        dcrypt()

    elif menu.get() == "Encrypt file":
        encryptfile()

    elif menu.get() == "Decrypt File":
        decryptionfile()

    elif menu.get() == "Decrypt standard file":
        decryptstandardfile()
    
#-------------------------------------------------------------------------------------------------------------------------


def insert():
    text="D:\\"
    rext=".txt"
    tj=len(txtfilename.get())
    txtfilename.insert(tj, rext)
    txtfilename.insert(0, text)
    return None

#----------------------------------------------------------------------------------------------------------------------------

def savefile():
    
    file=open(txtfilename.get(),"w")
    file.write(f"Encypted txt- {txtResult.get()}\n{key.get()}\n")
    file.close()

#-----------------------------------------------------------------------------------------------------------------------------


def decryptstandardfile():
 mylines = []                          
 root = tk.Tk()
 root.withdraw()

 file_path = filedialog.askopenfilename() 
 with open (f'{file_path}', 'rt') as myfile: 
    for myline in myfile:                
        mylines.append(myline)           

 print (mylines)
 t=mylines[0][14:-1]
 Msg.set(t)
 y=mylines[1][0]
 key.set(y)
 dcrypt()


#------------------------------------------------------------------------------------------------------------------------------

def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#------------------------------------------------------------------------------------------------------------------------------

def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)

#---------------------------------------------------------------------------------------------------------------------------------

def Encrypt():
    
    msg = Msg.get()
    k = key.get()
    lblResult.config(text="E-txt")
    Result.set(encode(k, msg))


#----------------------------------------------------------------------------------------------------------------------------------

def dcrypt():
    
    msg = Msg.get()
    k = key.get()
    lblResult.config(text="D-txt")
    Result.set(decode(k, msg))


#----------------------------------------------------------------------------------------------------------------------------------

def qExit():
    window.destroy()

#------------------------------------------------------------------------------------------------------------------------------------


def Reset():

    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")
    t.set("")
    password.set("")

#------------------------------------------------------------------------------------------------------------------------------------

def read():
   os.chmod(txtfilename.get(), S_IREAD)

#-----------------------------------------------------------------------------------------------------------------------------------

def encryptfile():
    root = tk.Tk()
    root.withdraw()
    enfile = filedialog.askopenfilename()
    with open (f'{enfile}', 'r') as f:
            f=f.read()
            msg = Msg.set(f)
            r1 = random.randint(0, 9)
            key.set(r1)
            msg = Msg.get()
            k = key.get()
            lblResult.config(text="E-txt")
            Result.set(encode(k, msg))
            with open(f'{enfile}', 'w') as f:
             f.write(f'{Result.get()}\n{k}')
             os.chmod(enfile, S_IREAD)

#-----------------------------------------------------------------------------------------------------------------------------------

def decryptionfile():
    box=[]
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilename()
    os.chmod(file, stat.S_IWRITE)      
    with open (f'{file}', 'rt') as myfile: 
     for i in myfile:                
        box.append(i)   

    bn=box[0][0:-1]  
    msg=Msg.set(bn)
    cv=box[0][-1]
    lk=box[1][0]
    key.set(lk)
    msg = Msg.get()
    k = key.get()
    lblResult.config(text="D-txt")
    Result.set(decode(k, msg))
    with open(f'{file}', 'w') as f:
      f.write(f'{Result.get()}')

#-----------------------------------------------for database--------------------------------------------------------------------------------------


def  database():
    from unittest import result
    from firebase import firebase 
 
    firebase = firebase.FirebaseApplication("https://encryption-5713a-default-rtdb.asia-southeast1.firebasedatabase.app/", None)
    data = {
       'Encryption is ':f'Encypted txt- {txtResult.get()}\n{key.get()}\k'
      }

    result=firebase.post(f"https://encryption-5713a-default-rtdb.asia-southeast1.firebasedatabase.app//ui//{txtfilename.get()}", data)
   
def getdatabase():
    from unittest import result
    from firebase import firebase 
    
    firebase = firebase.FirebaseApplication("https://encryption-5713a-default-rtdb.asia-southeast1.firebasedatabase.app/", None)
    op=firebase.get(f"https://encryption-5713a-default-rtdb.asia-southeast1.firebasedatabase.app//ui//{txtfilename.get()}", '')
    print(op)
    r=list(op)
    print(r)
    nb=txtfilenum.get()
    fg=int(nb)
    b=op[r[fg]]['Encryption is ']
    
    print(b)
    dex = b.index('\n')
    z=b[14:dex]
    Msg.set(z)
    trex=b.index('\k')
    u=b[dex+1:trex]
    key.set(u)






#----------------------------------------------------------------------------------------------------------------------------

btnResult=Button(width=20,pady=7 , text='Result', bg='#57a1f8', fg='white',border=0,command=lambda:conditions()).place(x=50,y=360)

#-----------------------------------------------------------------------------------------------------------------------------

btnsavetxt=Button(width=20,pady=7 , text='Savetxt', bg='#57a1f8', fg='white',border=0, command=lambda:[insert(),savefile(),read()]).place(x=250,y=360)

#-----------------------------------------------------------------------------------------------------------------------------

btndatabase=Button(width=15,pady=7, text='database', bg='#57a1f8',fg='white', border=0,command=lambda:database()).place(x=660,y=170)

#-----------------------------------------------------------------------------------------------------------------------------

btngetdatabase=Button(width=15,pady=7, text='getdata', bg='#57a1f8',fg= 'white', border=0, command=lambda:getdatabase()).place(x=830,y=170)

#-------------------------------------------------------------------------------------------------------------------------------

imgbtn=PhotoImage(file='reset.png')

labimg=Label(image='C:\\reset.png').pack(pady=500)

btnreset= Button(width=100, pady=7, text='h', border=6, command= lambda:Reset()).place(x=50,y=500)







window.mainloop()
