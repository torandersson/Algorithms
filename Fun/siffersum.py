#!/usr/bin/python
import optparse
import sys


USAGE = """%prog NUMBER

NUMBER    the number to calculate"""

def siffersum(number):
	if number == 0:
		return 0
	return number%10+siffersum(number/10)
	

def decimalToBinary(tal):
	binarystr = ""
	while(tal >= 1):
		if tal %2 != 0:
			binarystr += "1"
		else:
			binarystr += "0"
		tal = tal/2
	
	strlist = list(binarystr)
	strlist.reverse() 
	
	return ''.join(strlist)



if __name__ == '__main__':
    parser = optparse.OptionParser(USAGE)
    options, args = parser.parse_args()
    if len(args) != 1:
        print 'Error: Exactly 1 arguments required.'
        parser.print_help()
        sys.exit(1)
    NUMBER = int(args[0])
    print decimalToBinary(NUMBER)