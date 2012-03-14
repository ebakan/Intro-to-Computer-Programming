import urllib
class html:
    def __init__(self):
        self.url="http://"+raw_input()
        self.file="html.txt"
    def readSource(self):
        sock=urllib.urlopen(self.url)
        self.src=sock.read()
        sock.close()
    def writeSource(self):
        f=open(self.file, 'w')
        f.write(self.src)
        f.close()
    def dump(self):
        self.readSource()
        self.writeSource()
if __name__=='__main__':
    html=html()
    html.dump()
