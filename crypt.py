import base64

def importfile(type):
    questionstring = raw_input("Import " + type + " from file? (y/n): ")

    if questionstring == 'y':
        path = raw_input("path: ")
        try:
            file = open(path, 'r')
        except IOError:
            print "File doesn't exist!"
            print "Exiting..."
            exit()
        output = file.read()
        file.close()
    else:
        output = raw_input(type + ": ")
    return output

def exportfile(option, string):
    if option == 'y':      
        file = raw_input("Path to file: ")
        file = open(file, 'w')
        file.write(string)
        file.close()
        print "Done!"
    print "Exiting..."
    exit()

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc))

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

ftype = raw_input("e/d: ")
if ftype != 'e' and ftype != 'd':
    print "Whoops, Invalid input!"
    print "Exiting..."
    exit()

string = importfile("String")
key = importfile("Key")
try:
    if ftype == 'd':
        result = decode(key, string)
    elif ftype == 'e':
        result = encode(key, string)
    print result
    question = raw_input("Export to file? (y/n): ")
    exportfile(question, result)
except TypeError:
    print "Invalid key"

