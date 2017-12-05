):
 26     with open(s, 'rb') as f:
 27         b64 = base64.b64encode(f.read())
 28         f.close()
 29         return b64

