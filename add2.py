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

face_set_token = '8882381178d55f521a3197ecdb4db862'

api_key = 'bzrJS8GWq2ZfFwhS3XtNq3r-B5uieJgt'
secret = '2Vo-bB2i83TqAobymV1knX8bcRgefvwI'

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

"""
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
    b = pyobj['results'][0]['face_token']
    print a
    print b
    return a
"""
def confirm():
    name = en1.get()
    no = en2.get()
    info = en3.get()
    s = ''
    with open('ca.jpg', 'rb') as f:
        s = f.read()
        f.close()
    jpg_token = add_image_to_faceset('ca.jpg')
    
    op = sqlite3.connect("photo.db")
    op.execute("insert into test values(?, ?, ?, ?, ?)",(jpg_token, name, no, info, buffer(s)))
    op.commit()
    op.close()

    

top = Tk()
top.geometry('400x400+0+0')
top.title('add face')

#label Name
label_name = Label(top, text='Name:', width=5, height=1)
label_name.place(x=250, y=50, anchor=NW)
en1 = StringVar()
en_name = Entry(top, textvariable = en1)
en_name.place(x=300, y=50,  anchor=NW)



#label No
label_no = Label(top, text='No.', width=5, height=1)
label_no.place(x=250, y=85,anchor=NW)
en2= StringVar()
en_no = Entry(top,textvariable = en2)
en_no.place(x=300, y=85, anchor=NW)

#label info
label_info = Label(top, text='Info:', width=5, height=1)
label_info.place(x=250, y=115, anchor=NW)
en3 = StringVar()
en_info = Entry(top, textvariable= en3)
en_info.place(x=300, y=115, anchor=NW)

#label INFOMATION
label_in = Label(top, text='infomation')
label_in.place(x=285, y=28, anchor=NW)


#
#info_label = Label(top, bg='red', width=15, height=12)
#info_label.place(x=250, y=50, anchor=NW)

#camera label
label4 = Label(top, text='camera')
label4.place(x=90, y=10)

#show pic label
while True:
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    cv2.imshow("img", img)
cv2.imwrite("ca.jpg", img)
cap.release()
jpg = Image.open("ca.jpg")
out = jpg.resize((160, 220), Image.ANTIALIAS)
out.save("ca.png")
src = PhotoImage(file = "ca.png")

show_label = Label(top, bg='gray', width = 160, height=220, image=src)
show_label.place(x=30, y=30, anchor=NW)
#confirm button
button_ok = Button(top, text='Confirm',command=confirm,  width=10,height=2)
button_ok.place(x=55, y=300, anchor=NW)
top.mainloop()
