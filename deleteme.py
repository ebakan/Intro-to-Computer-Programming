def encode(inp,step):
    x = ""
    for i in inp:
        x+= chr((ord(i) + step - 97)%26+97)
    return x
print(encode(raw_input("Input:"),input("step:")))
