#!/usr/bin/env python
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
	if not os.path.exists('shell'):
		os.system('mkdir shell')
	if not os.path.exists('01.cleandata'):
		os.system('mkdir 01.cleandata')
	allshell = open('shell/all_SOAPnukescript.sh', 'w')
	for k in dict.keys():
		read1 = dict[k][0]
		read2 = dict[k][1]
		with open('shell/{d}_SOAPnuke.sh'.format(d = k), 'w') as out:
			cmd = '''echo start the program at `date +%Y-%m-%d' '%H:%M:%S` &&
/its1/GB_BT1/xutong/pipeline/RNAref-cloud/Modules/filter/SOAPnuke filter  --cut 0  --qualRate 0.5  --index  --lowQual 5  --nRate 0.1 -Q 1 -5 1 -1 {r1} -2 {r2}  -f AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC   -r AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTA  -o {path}/01.cleandata/{d} -C {d}_clean_1.fq -D {d}_clean_2.fq &&
echo finish the program at `date +%Y-%m-%d' '%H:%M:%S`'''.format(r1 = read1, r2 = read2, d = k, path = os.getcwd())
			out.write(cmd)
		allshell.write('sh {path}/shell/{d}_SOAPnuke.sh \n'.format(path = os.getcwd(), d = k))
	allshell.close()

def main():
	with open(sys.argv[1], 'r') as file:
		lines = file.readlines()
	readsdata = reads_data(lines)
	shell(readsdata)

if __name__ == '__main__':
	main()
