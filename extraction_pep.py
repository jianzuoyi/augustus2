#!/usr/bin/env python

import sys

def extraction(IDs, all):
	p = {}
	blocks = all.strip().split('>')
	for block in blocks[1:]:
		lines = block.strip().split('\n')
		id = lines[0].strip().split()[0]
		seq = ''.join(lines[1:])
		p[id] = seq
	with open(sys.argv[3], 'w') as out:
		for id in IDs:
			id = id.strip()
			out.write('>' + id + '\n' + p[id] + '\n')

def main():
	with open(sys.argv[1], 'r') as IDs, open(sys.argv[2], 'r') as pep:
		PEP = pep.read()	
		extraction(IDs, PEP)

if __name__ == '__main__':
	main()
