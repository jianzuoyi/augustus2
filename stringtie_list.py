#!/usr/bin/env python
#########################################################################
# File Name: stringtie_list.py
# Author: Tang Hao
# mail: tanghao@genebang.com
# Created Time: Wed 05 Jul 2017 04:31:37 PM CST
#########################################################################

import sys, os

def deal_list(lines):
	with open('{path}/03.stringtie/stringtie.lst'.format(path = os.getcwd()), 'w') as out:
		for line in lines:
			file = '_'.join(os.path.basename(line.strip().split(',')[0]).split('_')[:-1])
			out.write('{path}/03.stringtie/{f}/{f}.gtf \n'.format(path = os.getcwd(), f = file))

def main():
	with open(sys.argv[1], 'r') as file:
		lines = file.readlines()
	deal_list(lines)

if __name__ == '__main__':
    main()
