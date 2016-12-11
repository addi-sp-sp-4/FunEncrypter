import optparse
import base64


parser = optparse.OptionParser()
parser.add_option("--key-file", help="Path where key is stored", default=False, action="store")
parser.add_option("--string-file", help="Path where string is stored", default=False, action="store")
parser.add_option("-k", help="Key", default=False, action="store")
parser.add_option("-s", help="String", default=False, action="store")
parser.add_option("--export", "-x", help="Path where you want to store input", default=False, action="store")
parser.add_option("--encrypt", "-e", help="Encrypt", default=False, action="store_true")
parser.add_option("--decrypt", "-d", help="Decrypt", default=False, action="store_true")
(args, _) = parser.parse_args()
#print args

if args.key_file == False and args.k == False or args.key_file != False and args.k != False:
    parser.print_help()
    exit()
if args.string_file == False and args.s == False or args.string_file != False and args.s != False:
    parser.print_help()
    exit()

if args.encrypt != False and args.decrypt != False:
    parser.print_help()
    exit()

def readfile(path):

    file = open(path, 'r')
    output = file.read()
    file.close()
    return output

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

ex = False
if args.s == False:
    try:
        string = readfile(args.string_file)
    except IOError:
        ex = True
else:
    string = args.s

if args.k == False:
    try:
        key = readfile(args.key_file)
    except IOError:
        ex = True
else:
    key = args.k

if ex == True:
    print "Whoops, a file error"
    exit()

if args.encrypt == False:
    try:
        result = decode(key, string)
    except TypeError:
        print "Whoops, Your key is incorrect"
        print "Exiting..."
        exit()
else:
    result = encode(key, string)
print result
if args.export != False:
    try:
        file = open(args.export, 'w')
        file.write(result)
    except IOError:
        print "Whoops, a file error"
    
