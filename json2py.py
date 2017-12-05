import json

with open('r.json', 'r') as f:
    js = json.dumps(f.text)
    
    py = json.loads(js)
    print py
    f.close()
