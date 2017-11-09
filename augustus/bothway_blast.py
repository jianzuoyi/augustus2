#! usr/bin/env python

import sys, re, os

def addtap(lines):
	with open('cat_both_cds.fa', 'w') as out:
		for line in lines:
			if line.startswith('>'):
				line = line.strip().split()[0] + '_1\n'
			out.write(line)
		for line in lines:
			if line.startswith('>'):
				line = line.strip().split()[0] + '_2\n'
			out.write(line)
def main():
	with open(sys.argv[1], 'r') as input:
		lines = input.readlines()
		addtap(lines)

if __name__ == '__main__':
	main()
