#! /usr/bin/env python

import os, re, sys
	
def convert(lines, out):
	for line in lines:
		if not line.startswith('#'):
			each = line.strip().split('\t')
			if each[2] == 'exon':
				pat = re.search(r'gene_id "(.*?)"; transcript_id "(.*?)";', each[8])
				geneid = 'ID=' + pat.group(1)
				target = 'Target=' + pat.group(2)
				other = each[8].strip().split(';')[2:]
				other.insert(0, target)
				other.insert(0, geneid)
				each[8] = ';'.join(other)
				each[2] = 'cDNA_match'
				out.write('\t'.join(each) + '\n')
			
def main():
	with open(sys.argv[1], 'r') as inputfile, open('transcripts.gff3', 'w') as out:
		convert(inputfile, out)

if __name__ == '__main__':
	main()
