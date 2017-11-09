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
	if not os.path.exists('02.hisat'):
		os.system('mkdir 02.hisat')
	allshell = open('shell/all_hisatscript.sh', 'w')
	for k in dict.keys():
		read1 = dict[k][0]
		read2 = dict[k][1]
		with open('shell/{d}_hisat.sh'.format(d = k), 'w') as out:
			cmd = '''echo start the program at `date +%Y-%m-%d' '%H:%M:%S` &&
mkdir -p {path}/02.hisat/{d};
/opt/bio/hisat2-2.0.4/hisat2  --dta --no-discordant  --no-mixed  --threads 16 -x {path}/00.build_db/genome -1 {path}/01.cleandata/{d}/{d}_clean_1.fq.gz -2 {path}/01.cleandata/{d}/{d}_clean_2.fq.gz  2> {path}/02.hisat/{d}/hisat.log | samtools sort --threads 8 --output-fmt bam -o {path}/02.hisat/{d}/{d}_sort.bam &&
echo finish the program at `date +%Y-%m-%d' '%H:%M:%S`'''.format(r1 = read1, r2 = read2, d = k, path = os.getcwd())
			out.write(cmd)
		allshell.write('sh {path}/shell/{d}_hisat.sh \n'.format(path = os.getcwd(), d = k))
	allshell.close()

def main():
	with open(sys.argv[1], 'r') as file:
		lines = file.readlines()
	readsdata = reads_data(lines)
	shell(readsdata)

if __name__ == '__main__':
	main()
