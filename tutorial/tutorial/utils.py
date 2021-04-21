
def save2file(p):
    with open("test2.json", "a") as f:
        for key in p.keys():
            f.write(str(key + ":" + p[key]).replace('\r\n', '') + '\n')

def _save2file(p):
    with open("test2.json", "a") as f:
        for key in p.keys():
            f.write(str(key +":" + p[key]).replace('\r\n','') +'\n')