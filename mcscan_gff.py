#!/usr/bin/env python

import sys, re

def deal(lines):
	with open('Mcscanx.gff', 'w') as out:
		for line in lines:
			each = line.strip().split('\t')
			if each[2] == 'gene':
				id = 'evm.model.' + re.search(r'ID=evm.TU.(.*?);', each[8]).group(1)
				out.write('\t'.join([each[0], id, each[3], each[4]]) + '\n')

def main():
	with open(sys.argv[1], 'r') as files:
		deal(files)

if __name__ == '__main__':
	main()
