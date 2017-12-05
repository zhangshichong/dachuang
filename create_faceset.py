import requests
from datetime import datetime

api_key = 'bzrJS8GWq2ZfFwhS3XtNq3r-B5uieJgt'
secret = '2Vo-bB2i83TqAobymV1knX8bcRgefvwI'
url ='https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
display_name = 'test1'
outer_id = '10'
param = {'api_key': api_key,
         'api_secret': secret,
         'display_name': display_name,
         'outer_id': outer_id}


re = requests.post(url, data = param)
print re.text
with open("create_face.json", 'a') as f:
    f.write(re.text)
    now = datetime.now()
    f.write("**********changed at "+now.strftime("%Y-%m-%d %H:%M:%S"))
    f.close()






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
    b = pyobj['results'][0]['face_token']
    print a
    print b
    return a
