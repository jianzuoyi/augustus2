#! /usr/bin/env python

import os, sys, re

def filter(lines):
	for line in lines:
		each = line.strip().split()
		if each[0].split('_')[-1] == '1' and each[1].split('_')[-1] == '2' and float(each[2]) < 80:
			print line.strip()
def main():
	with open(sys.argv[1], 'r') as input:
		filter(input)

if __name__ == '__main__':
	main()
