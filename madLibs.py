#assn3
#ebakan
lst=[raw_input("adjective:"),
     raw_input("noun:"),
     raw_input("verb:"),
     raw_input("plural noun:"),
     raw_input("noun:"),
     raw_input("plural noun:"),
     raw_input("-ing verb:"),
     raw_input("-ing verb:"),
     raw_input("-ing verb:"),
     raw_input("plural noun:")]
ln=['IDLE is Python\'s Tkinter-based Integrated DeveLopment Environment. '
    'IDLE emphasizes a '+lst[0]+', clean design with a simple '+lst[1]+'. ',
    'Although it is suitable for beginners, even advanced users will find that IDLE has everything they really need to '+lst[2]+' pure Python '+lst[3]+'. ',
    'IDLE features a multi-window '+lst[4]+' with multiple '+lst[5]+', Python '+lst[6]+', and many other capabilities. ',
    'The editor has comprehensive '+lst[7]+' functions, including '+lst[8]+' multiple files. ',
    'Class browsers and path browsers provide fast access to '+lst[9]+' from a top level viewpoint without dealing with code folding.']
def out(ln):
    x=''
    for i in range(len(ln)):
        x+=ln[i]
    return x
if __name__=='__main__':
    print(out(ln))
    raw_input()
