#!/usr/bin/env python
import os, sys

def reads_data(lines):
	q = {}
	for line in lines:
		line = line.strip()
		if line:
			read1 = line.split(',')[0]
			read2 = line.split(',')[1]
			dir = read1.split('/')[-2]
			file = '_'.join(os.path.basename(read1).split('_')[:-1])
			q[file] = [read1, read2]
	return q

def shell(dict):
	if not os.path.exists('03.stringtie'):
		os.system('mkdir 03.stringtie')
	allshell = open('shell/all_stringtiescript.sh', 'w')
	for k in dict.keys():
		read1 = dict[k][0]
		read2 = dict[k][1]
		with open('shell/{d}_stringtie.sh'.format(d = k), 'w') as out:
			cmd = '''echo start the program at `date +%Y-%m-%d' '%H:%M:%S` &&
mkdir -p {path}/03.stringtie/{d};
/opt/bio/stringtie-1.2.4.Linux_x86_64/stringtie -p 24 -l {d} -o {path}/03.stringtie/{d}/{d}.gtf {path}/02.hisat/{d}/{d}_sort.bam &&
echo finish the program at `date +%Y-%m-%d' '%H:%M:%S`'''.format(r1 = read1, r2 = read2, d = k, path = os.getcwd())
			out.write(cmd)
		allshell.write('sh {path}/shell/{d}_stringtie.sh \n'.format(path = os.getcwd(), d = k))
	allshell.close()

def main():
	with open(sys.argv[1], 'r') as file:
		lines = file.readlines()
	readsdata = reads_data(lines)
	shell(readsdata)

if __name__ == '__main__':
    main()
