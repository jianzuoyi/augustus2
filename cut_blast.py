#!/usr/bin/env python

import sys, os

def cut_script(types, n):
	if types == 'nr':
		db = '/its1/pub/annotdb/nr/201605/nr'
	elif types == 'uniport':
		db = '/its1/pub/annotdb/uniprot/release-2017_07/plant.fa'
	os.system('mkdir split_{types}'.format(types = types))
	with open(types + '_blastall_all.sh', 'w') as out:
		for i in range(1, int(n)+1):
			cmd = '/opt/bio/ncbi-blast-2.6.0+-src/c++/bin/blastp -query {path}/../../06.PASA/cut/Pasa_update.{n} -out {path}/split_{types}/{types}.{n}.blast -outfmt 6 -evalue 1e-5 -num_threads 16 \n'.format(n = i, types = types, path = os.getcwd())
			out.write(cmd)

def main():
	cut_script(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
	main()
