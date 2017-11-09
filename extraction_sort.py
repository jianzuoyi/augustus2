#!/usr/bin/env python

import sys, os, re

def gff_extraction(lines, out):
	q = {}
	for line in lines:
		line = line.strip()
		if line.startswith('#PROT'):
			id = line.split()[1]
			seq = line.split()[3]
			out.write('>' + id + '\n' + seq + '\n')
		elif line and not line.startswith('# ORIGINAL'):
			each = line.split('\t')
			if each[2] == 'gene':
				id = re.search(r'ID=(.+?);', each[8]).group(1)
				q[id] = [line]
			else:
				q[id].append(line)
	return q

def sort(dic, out):
	for k in sorted(dic, key = lambda x : (int(re.search(r'(\d+)\.(\d+)', x).group(1)), int(re.search(r'(\d+)\.(\d+)', x).group(2)))):
		out.write('\n'.join(dic[k]) + '\n\n')

def main():
	with open(sys.argv[1], 'r') as files, open('pasa_update.pep', 'w') as out1, open('Pasa_update.gff3', 'w') as out2:
		dic = gff_extraction(files, out1)
		sort(dic, out2)

if __name__ == '__main__':
	main()
