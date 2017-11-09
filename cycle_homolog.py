#!/usr/bin/env python
#########################################################################
# File Name: cycle_homolog.py
# Author: Tang Hao
# mail: tanghao@genebang.com
# Created Time: Thu 13 Jul 2017 09:56:36 AM CST
#########################################################################

import sys, os

def homolog(pep, species, genome):
	cmd = '''mkdir -p {species}; cd {species} && perl /its1/GB_BT2/tanghao/Project/annotation_pipeline_V2/homolog/protein_map_genome.pl --step 1234 --cpu 5 --align_rate 0.01 --extend_len 500 --tophit 3 --blast_eval 1e-5 --lines 1000 {pep} {path}/00.formatdb/{g} & '''.format(g = genome, path = os.getcwd(), species = species, pep = pep)
	os.system(cmd)

def eachspecies(list, genome):
	for line in list:
		pep = line.strip().split()[1]
		species = line.strip().split()[0]
		homolog(pep, species, genome)

def main():
	with open(sys.argv[1]) as input:
		eachspecies(input, sys.argv[2])

if __name__ == '__main__':
    main()
