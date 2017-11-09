#!/usr/bin/env python
#########################################################################
# File Name: shell.py
# Author: Tang Hao
# mail: tanghao@genebang.com
# Created Time: Thu 29 Jun 2017 03:53:01 PM CST
#########################################################################

import os, sys

def reads_data(lines):
	q = {}
	for line in lines:
		read1 = line.strip().split(',')[0]
		read2 = line.strip().split(',')[1]
		dir = read1.strip().split('/')[-2]
		file = '_'.join(os.path.basename(read1).split('_')[:-1])
		q[file] = [read1, read2]
	return q

def shell(dict):
	os.system('mkdir shell 01.cleandata 02.hisat 03.stringtie')
	allshell = open('shell/all_shellscript.sh', 'w')
	for k in dict.keys():
		read1 = dict[k][0]
		read2 = dict[k][1]
		with open('shell/{d}_hisat_stringtie.sh'.format(d = k), 'w') as out:
			cmd = '''echo start the program at `date +%Y-%m-%d' '%H:%M:%S` &&
/its1/GB_BT1/xutong/pipeline/RNAref-cloud/Modules/filter/SOAPnuke filter  --cut 0  --qualRate 0.5  --index  --lowQual 5  --nRate 0.1 -Q 1 -5 1 -1 {r1} -2 {r2}  -f AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC   -r AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTA  -o {path}/01.cleandata/{d} -C {d}_clean_1.fq -D {d}_clean_2.fq &&
mkdir -p {path}/02.hisat/{d};
/opt/bio/hisat2-2.0.4/hisat2  --dta --no-discordant  --no-mixed  --threads 8 -x {path}/00.build_db/genome -1 {path}/01.cleandata/{d}/{d}_clean_1.fq.gz -2 {path}/01.cleandata/{d}/{d}_clean_2.fq.gz  2> {path}/02.hisat/{d}/hisat.log | samtools sort --threads 8 --output-fmt bam -o {path}/02.hisat/{d}/{d}_sort.bam &&
mkdir -p {path}/03.stringtie/{d};
/opt/bio/stringtie-1.2.4.Linux_x86_64/stringtie -p 8 -l {d} -o {path}/03.stringtie/{d}/{d}.gtf {path}/02.hisat/{d}/{d}_sort.bam &&
echo finish the program at `date +%Y-%m-%d' '%H:%M:%S`'''.format(r1 = read1, r2 = read2, d = k, path = os.getcwd())
			out.write(cmd)
		allshell.write('sh {path}/shell/{d}_hisat_stringtie.sh \n'.format(path = os.getcwd(), d = k))
	allshell.close()

def main():
	with open(sys.argv[1], 'r') as file:
		lines = file.readlines()
	readsdata = reads_data(lines)
	shell(readsdata)

if __name__ == '__main__':
    main()
