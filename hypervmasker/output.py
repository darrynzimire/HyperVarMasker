import os
from datetime import datetime


def startmessage():
	text = 'HyperVMasker v.0.1.1\n'\
			'Copyright 2022 UCT HIV-Diversity \n\n'\

	print(text)


def make_dir():
	now = datetime.now()
	date_time_obj = datetime.strftime(now, '%Y%m%d-%H%M')
	directory = './Masked_data'
	file_path = os.path.join(directory)
	if not os.path.isdir(directory):
		os.mkdir(directory)

	return file_path


def write_seq(header, seq):
	fp = make_dir()
	with open(fp + '/masked_seq.fasta', 'a') as _h:
			_h.write('{}{}\n'.format('>', header))
			_h.write('{}\n'.format(seq))


def write_var_regions(header, seq):
	fp = make_dir()
	with open(fp + '/run_info.txt', 'a+') as handle:
		handle.write('{}{}{}{}\n'.format('>', header, ' :', seq))

		# print(f'{s[0]:<10}{s[1]:<17}{s[2]:<5}{s[3]:<12}{s[4]:>12}')
		#     ^       ^^^       ^^^       ^^       ^^^       ^^^
		# f-string  left-10   left-17   left-5   left-12   right-12
		# handle.write('{}\n\n'.format(seq))






