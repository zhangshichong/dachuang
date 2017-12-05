from Tkinter import *
import Image
import cv2
import sqlite3
import base64
import requests
import json
from datetime import datetime
de_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
add_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
sear_url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
face_set_token = '8882381178d55f521a3197ecdb4db862'
api_key = 'bzrJS8GWq2ZfFwhS3XtNq3r-B5uieJgt'
secret = '2Vo-bB2i83TqAobymV1knX8bcRgefvwI'
top = Tk()
top.geometry('400x400+0+0')
top.title('face detection')

#global response matching token retk
retk = ''
#exact face token from response json string
def get_face_token(r):
    pyobj = json.loads(r.text)
    return pyobj['faces'][0]['face_token']

#to record face tokens in token_list.txt
def record_tokens(token):
    with open('token_list.txt', a) as f:
        f.write(token)
        f.write('\n')
        f.close()

#change jpg to base64
def jpg_to_b64(s):
    with open(s, 'rb') as f:
        b64 = base64.b64encode(f.read())
        f.close()
        return b64

#upload base64(s) to face++ and return response json string 
def upload_detect(s):
    param = {'api_key':api_key, 'api_secret': secret, 'image_base64':s}
    r = requests.post(de_url, data = param)
    print r.text
    with open('detect.result.json','a') as f:
        f.write(r.text)
        now = datetime.now()
        f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        f.close()
    with open('r.json', 'w') as f:
        f.write(r.text)
        now = datetime.now()
        f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        f.close()
    return r

def add_to_faceset(face_token):
    param = {'api_key':api_key, 'api_secret': secret, 'faceset_token':face_set_token, 'face_tokens':face_token}
    r = requests.post(add_url, data = param)
    with open('add_set.txt', 'a') as f:
        f.write(r.text)
        now = datetime.now()
        f.write("**"+now.strftime("%Y-%m-%d %H:%M:%S")+"***")
        f.close()
    pyobj = json.loads(r.text)
    num = pyobj["face_added"]
    if num > 0:
        print ('add to set successfully')
        with open('sets.txt', 'a') as f:
            f.write(face_token)
            now = datetime.now()
            f.write(" "+now.strftime("%Y-%m-%d %H:%M:%S")+'\n')
            f.close()
    else:
        print ('failed to add face token')


"""
#example
img = jpg_to_b64('1.jpg')
r = upload_detect(img)
r_token = get_face_token(r)
add_to_faceset(r_token)
"""
def get_jpg_token(jpg):
    img = jpg_to_b64(jpg)
    r = upload_detect(img)
    r_token = get_face_token(r)
    return r_token

def add_image_to_faceset(jpg):#need a jpg file
    img = jpg_to_b64(jpg)
    r = upload_detect(img)
    r_token = get_face_token(r)
    add_to_faceset(r_token)
    return r_token


def search_from_faceset(token):
    param = {'api_key':api_key, 'api_secret':secret, 'face_token':token, 'faceset_token':face_set_token}
    r = requests.post(sear_url, data = param)
    print r.text
    with open('search_response.txt', 'a') as f:
        f.write(r.text)
        now = datetime.now()
        f.write("  "+now.strftime('%Y-%m-%d %H:%M:%S')+"\n")
    pyobj = json.loads(r.text)
    a = pyobj['results'][0]['confidence']
    retk = pyobj['results'][0]['face_token']
    with open('query.txt', 'w') as f:
        f.write(retk)
        f.close()
    print a
    print retk
    return a

#top = Tk()
#top.geometry('400x400+0+0')
#top.title('face detection')

#label Name
en1=StringVar()
label_name = Label(top, text='Name:', width=5, height=1)
label_name.place(x=250, y=250, anchor=NW)
label1 = Label(top, text='', bg='gray', width=8, height=1, textvariable = en1)
label1.place(x=300, y=250,  anchor=NW)



#label No
en2 = StringVar()
label_no = Label(top, text='No.', width=5, height=1)
label_no.place(x=250, y=285,anchor=NW)
label2 = Label(top, text='', bg='gray', width=8, height=1, textvariable = en2)
label2.place(x=300, y=285, anchor=NW)

#label info
en3 = StringVar()
label_info = Label(top, text='Info:', width=5, height=1)
label_info.place(x=250, y=315, anchor=NW)
label3 = Label(top, text='', bg='gray', width=8, height=1, textvariable = en3)
label3.place(x=300, y=315, anchor=NW)

#label INFOMATION
label_in = Label(top, text='infomation')
label_in.place(x=285, y=28, anchor=NW)


#

#info_label = Label(top, bg='red', width=40, height=40)
#info_label.place(x=250, y=50, anchor=NW)

#camera label
label4 = Label(top, text='camera')
label4.place(x=90, y=10)

#camera picture
cap = cv2.VideoCapture(0)
ret, img = cap.read()
cv2.imwrite("ca1.jpg", img)
cap.release()
jpg = Image.open("ca1.jpg")
out = jpg.resize((160, 220), Image.ANTIALIAS)
out.save("ca1.png")
src = PhotoImage(file = "ca1.png")
show_label = Label(top, bg='yellow', width = 160, height=220, image=src)
show_label.place(x=30, y=30, anchor=NW)

tk_ca1 = get_jpg_token('ca1.jpg')
re_ca1 = search_from_faceset(tk_ca1)

op = sqlite3.connect("photo.db")
tk1 = ''
with open("query.txt", 'r') as f:
    tk1 = f.read()
    f.close()

cu = op.execute("select * from test where token = ?",(tk1,))


NAME = ''
TOKEN = ''
NO = ''
INFO = ''
PHOTO = ''

for row in cu:
    TOKEN = row[0]
    NAME = row[1]
    NO = row[2]
    INFO = row[3]
    PHOTO = row[4]
en1.set(NAME)
en2.set(NO)
en3.set(INFO)
with open('v.jpg','wb') as f:
    f.write(PHOTO)
    f.close()
cu.close()
op.close()
jpg = Image.open('v.jpg')
out = jpg.resize((80, 80), Image.ANTIALIAS)
out.save('v.png')
src2 = PhotoImage(file = 'v.png')
info_label = Label(top, bg='gray', width=80, height=140, image=src2)
info_label.place(x=290, y=50, anchor=NW)


#op = sqlite3.connect("photo.db")
"""
op.execute('''create table test (token nvarchar(40) not null primary key,
name nvarchar(20) not null,
no nvarchar(20) not null,
infomation nvarchar(200) default null,
photo blob not null)''')
op.commit()
"""
#insert , pay attention to buffer
#op.execute("insert into test values(?, ?, ?, ?, ?)",(token, name, no, info,buffer(s)))
#op.execute("delete * from test")
#op.commit()

#
"""
tk0 = ''
with open('query.txt', 'r') as f:
    tk0 = f.read()
    f.close()

cursor = op.execute("select * from test where token = ?",(tk0,))
for row in cursor:
    print row[0]
    print row[1]
    print row[2]
    print row[3]
#out1 = Image.open('v.jpg')
#out1.save('v.png')
src2 = PhotoImage(file = 'ca1.png')
info_label = Label(top, bg='red', width=60, height=100, image=src2)
info_label.place(x=250, y=50, anchor=NW)
#confirm button
#button_ok = Button(top, text='Confirm',width=10,height=2)
#button_ok.place(x=55, y=300, anchor=NW)
"""
top.mainloop()