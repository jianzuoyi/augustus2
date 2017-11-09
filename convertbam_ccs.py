#!/usr/bin/env python
#########################################################################
# File Name: /its1/GB_BT2/tanghao/Project/annotation_pipeline_V2/convertbam_ccs.py
# Author: Tang Hao
# mail: tanghao@genebang.com
# Created Time: Mon 24 Jul 2017 04:32:30 PM CST
#########################################################################

import sys, os 

def deal_fofn(fofn):
	q = {}
	with open(fofn, 'r') as lines:
		for path in lines:
			path = path.strip()
			if path:
				filename = os.path.basename(path)
				sample_name = '_'.join(filename.split('_')[:-1])
				if sample_name in q.keys():
					q[sample_name].append(path)
				else:
					q[sample_name] = [path]
	return q

def write_shell(dict):
	with open('all.sh', 'w') as out:
		for k, v in dict.iteritems():
			with open(k + '.sh', 'w') as each:
				cmd = '''date &&
cd {path}/../01.bax2bam &&
/its1/GB_BT1/lixiangfeng/software/smrtlink5/smrtcmds/bin/bax2bam -o {k} {v1} {v2} {v3} &&
cd {path}/../02.CCS &&
/its1/GB_BT1/lixiangfeng/software/smrtlink5/smrtcmds/bin/ccs --numThreads 24 --noPolish --minLength 100 --maxLength 15000 --minPasses 0 --minPredictedAccuracy 0.85 --minZScore -999 --maxDropFraction 0.8 --minSnr 3.75 --reportFile {k}_report.txt {path}/../01.bax2bam/{k}.subreads.bam {k}.ccs.bam &&
date
	'''.format(path = os.getcwd(), k = k, v1 = v[0], v2 = v[1], v3 = v[2])
				each.write(cmd)
				out.write('sh {path}/{k}.sh'.format(k = k, path = os.getcwd()) + '\n')

def main():
	dict = deal_fofn(sys.argv[1])
	write_shell(dict)

if __name__ == '__main__':
	main()
