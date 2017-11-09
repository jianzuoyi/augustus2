#!/usr/bin/env python

import sys, os ,re

def convert(lines, out):
	n = 0
	for line in lines:
		each = line.strip().split('\t')
		if each[2] == 'mRNA':
			n += 1
		else:
			each[2] = 'match'
			each[8] = 'ID=Genewise.'+str(n)+';Target=' + re.search(r'Parent=(.*?);', each[8]).group(1)
			out.write('\t'.join(each) + '\n')
	
def main():
	with open(sys.argv[1], 'r') as inputfile, open('homolog.gff3', 'w') as out:
		convert(inputfile, out)

if __name__ == '__main__':
	main()
