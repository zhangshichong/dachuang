import base64

with open('test.jpg') as fjpg:
    image_data = fjpg.read()
    base64_data = base64.b64encode(image_data)
print base64_data
