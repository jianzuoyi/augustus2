#!/usr/bin/env python

import sys

def extraction(lines, out):
	for line in lines:
		line = line.strip()
		if line:
			if not line.startswith('#'):
				id = line.split()[0]
				out.write(id + '\n')

def main():
	with open(sys.argv[1], 'r') as files, open('Pfam_hit_ID', 'w') as out:
		extraction(files, out)

if __name__ == '__main__':
	main()
