#!/usr/bin/env python

import re, sys

def convert(lines, out):
	for line in lines:
		line = line.strip()
		if line and not line.startswith('#'):
			each = line.split()
			if each[2] == 'mRNA':
				geneID = re.search(r'ID=transcript:(.*?);', each[8]).group(1)
				out.write('\t'.join([each[0], geneID, each[3], each[4]]) + '\n')

def main():
	with open(sys.argv[1], 'r') as files, open('mscanx.gff', 'w') as out:
		convert(files, out)

if __name__ == '__main__':
	main()
