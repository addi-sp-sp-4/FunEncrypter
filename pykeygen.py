import optparse
import random
import string

parser = optparse.OptionParser()
parser.add_option("--length", "-l", help="Length of key", default=False, action="store")
parser.add_option("--export", "-x", help="Path of file to store", default=False, action="store")
(args, _) = parser.parse_args()

length = int(args.length)
if length == False:
	length = 256



result = ''
for i in range(length):
	if random.randint(1, 10) <= 5:
		result += str(random.randint(0, 9))
	else:
		result += random.choice(string.letters)

print result

if args.export != False:
	try:
		file = open(args.export, 'w')
		file.write(result)
		file.close()
	except IOError:
		print "Wrong path!"
