#!/usr/bin/env python

import sys, re

def extraction(gffs, IDs, pep):
	blocks = gffs.read().strip().split('\n\n')
	q = {}
	for block in blocks:
		id = re.search(r'ID=(evm.model.*?);', block).group(1)
		q[id] = block

	p = {}
	for line in pep:
		line = line.strip()
		if line.startswith('>'):
			i = line[1:]
		else:
			p[i] = line

	with open('final_hits.gff3', 'w') as out_gff, open('final_hits.pep', 'w') as out_pep:
		for id in IDs:
			id = id.strip()
			out_gff.write(q[id] + '\n')
			out_pep.write('>' + id + '\n' + p[id] + '\n')	

def main():
	with open(sys.argv[1], 'r') as IDs, open(sys.argv[2], 'r') as gffs, open(sys.argv[3], 'r') as pep:
		extraction(gffs, IDs, pep)

if __name__ == '__main__':
	main()
