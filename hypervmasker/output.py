import os
from datetime import datetime
import pandas as pd
import numpy as np
import time
from tqdm import tqdm
import sys


def startmessage():
	text = 'HyperVMasker v.0.1.1\n'\
			'Copyright 2022 UCT HIV-Diversity \n\n'\

	print(text)


def progress_bar(num):
	for i in tqdm(range(num)):
		time.sleep(0.5)


def make_dir():
	now = datetime.now()
	date_time_obj = datetime.strftime(now, '%Y%m%d-%H-%M')
	directory = '{}{}'.format('./HyperVarMasker_output_', date_time_obj)
	file_path = os.path.join(directory)
	if not os.path.isdir(directory):
		os.mkdir(directory)

	return  file_path


def write_seq(header, seq):
	fp = make_dir()
	with open(fp + '/masked_seq.fasta', 'a') as _h:
			_h.write('{}{}\n'.format('>', header))
			_h.write('{}\n'.format(seq))


def num_seq(file):
	size = len([1 for i in open(file, 'r') if i.startswith('>')])
	return size


def run_info(file, ref, header, var_regions):
	fp = make_dir()
	now = datetime.now()
	date_time_obj = datetime.strftime(now, '%Y%m%d-%H%M')

	with open(fp + '/run_info.txt', 'a') as handle:
		date = datetime.now().date()
		time = datetime.now().strftime('%H:%M')
		number_of_sequences = num_seq(file)
		d = '{}{}\n'.format(f'Run date: ', date)
		t = '{}{}\n'.format(f'Run time: ', time)
		numseq = '{}{}\n'.format(f'Number of sequences processed: ', number_of_sequences)
		filename = '{}{}\n'.format(f'Input file name: ', file)
		ref = '{}{}\n'.format(f'Reference: ', ref)
		subheading = 'Masking information: '
		line = ''.join('-' for i in range(60))
		handle.write('\n{}{}{}{}{}\n\n{}\n{}\n\n'.format(d, t, numseq, filename, ref, subheading, line)
						 )
		df = pd.DataFrame(columns=[f'sequence name', f'target region'])
		df[f'sequence name'] = header
		df[f'target region'] = var_regions
		df.index = np.arange(1, len(df) + 1)
		handle.write(df.to_string())








