#! /usr/bin/env python

import sys, os, re

def convert(lines):
	with open('AUGUSTUS.gff3', 'w') as out:
		for line in lines:
			each = line.strip().split()
			if each[2] == 'mRNA':
				each[2] = 'gene'
				out.write('\t'.join(each)[:-1] + '\n')
				mrna = line.strip().split()
				geneid = re.search(r'ID=(.*?);', mrna[8]).group(1)
				mrna[8] = 'ID=' + geneid + '_mrna;Parent=' + geneid
				out.write('\t'.join(mrna) + '\n')
				n = 0
			elif each[2] == 'CDS':
				n += 1
				each[2] = 'exon'
				id = geneid + '.exon' + str(n)
				each[8] = 'ID=' + id + ';' + 'Parent=' + re.search(r'ID=(.*?);', mrna[8]).group(1)
				out.write('\t'.join(each) + '\n')
				e = line.strip().split()
				e[8] = 'ID=' + geneid + '.cds' + str(n) + ';' + 'Parent=' + re.search(r'ID=(.*?);', mrna[8]).group(1)
				out.write('\t'.join(e) + '\n')

def main():
	with open(sys.argv[1], 'r') as inputfile:
		convert(inputfile)

if __name__ == '__main__':
	main()
