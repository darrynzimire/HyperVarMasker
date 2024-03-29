from Bio import SeqIO
import pandas as pd
import argparse
import os
import sys
import gzip
from hypervmasker import output
from datetime import datetime
import time
from tqdm import tqdm


parser = argparse.ArgumentParser(description='This is a tool that masks the hypervariable regions in a multi-alignment FASTA database')
parser.add_argument('-infile',               type=str,   required=False,  metavar="<str>",        help='Directory where the fasta files are stored')
parser.add_argument('-offset', nargs=2,    type=int,   required=False,  metavar='(start, end)', help='start and end positions of hypervariable region')
parser.add_argument('-refname',            type=str,   required=True)
parser.add_argument('-refpos', type=int, required=False, default=1,  help='position of reference sequence in FASTA database')


args = parser.parse_args()
file = args.infile
# filepath = args.path
refname = args.refname
refpos = args.refpos
(startpos, endpos) = args.offset
# f_extension = args.out

start_time = datetime.now()


def read_dir(path):
    target_files = []
    if filepath is not None:
        files = os.listdir(path)
        for file in files:
            if file.endswith('.fasta' or '.fa'):
                target_files.append(file)
    else:
        cwd = os.getcwd()
        files = os.listdir(cwd)
        for file in files:
            if file.endswith('.fasta' or '.fa'):
                target_files.append(file)
    return target_files


def check_is_fasta(filename):
    if filename.endswith('.gz'):
        f = gzip.open(filename)
        with open(filename, "r") as handle:
            fasta = SeqIO.parse(handle, "fasta")
            return any(fasta)


def read_files(file, refname):

    try:
        with open(file, 'r') as handle:
            print('Reading input file: ' + file)
            output.progress_bar(4)
            dct = {record.id: str(record.seq) for record in SeqIO.parse(handle, 'fasta')}
            return dct
    except OSError:
        print('Warning: File not found!')
        print('Please check if correct path or file name was provided.\n\n')
        sys.exit()


def calc_alignedpos(ref_seq):
    """
    Modified from http://github.com/smallBixtools
    :param ref_seq:
    :return:
    """
    aligned_columns = []
    ref_pos = list(range(1, len(ref_seq)))

    character_count = 0
    added_for_this_char = False
    for curnt_col, seq_char in enumerate(ref_seq):
        curnt_col = curnt_col + 1
        if curnt_col >= len(ref_seq):
            break
        if seq_char != '-':
            character_count += 1
            added_for_this_char = False

        if character_count in ref_pos:
            if not added_for_this_char:
                aligned_columns.append(curnt_col)
                added_for_this_char = True
    if len(aligned_columns) != len(ref_pos):
        while len(aligned_columns) < len(ref_pos):
            aligned_columns.append("NA")

    return ref_pos, aligned_columns


def calc_new_offset(ref_pos, aligned_pos, offset):

    startpos = offset[0]
    endpos = offset[1]
    df = pd.DataFrame(columns=['ref_positions', 'aligned_positions'])
    df['ref_positions'] = ref_pos
    df['aligned_positions'] = aligned_pos
    start = df.loc[df['ref_positions'] == startpos, 'aligned_positions'].iloc[0]
    end = df.loc[df['ref_positions'] == endpos, 'aligned_positions'].iloc[0]
    new_pos = (start, end)

    return new_pos


def mask_seq(args, startpos, endpos):
    header = args[0]
    seq = args[1]
    var_regions = seq[startpos-1:endpos]
    masked_string = ''.join(seq.replace(var_regions, ''))
    return var_regions, masked_string


def main():

    output.startmessage()
    if sys.version_info[0] < 3:
        print("Please run this with a Python version greater than 3. Now exiting.")
        sys.exit()

    refseq = read_files(file, refname)
    if refname not in refseq.keys():
        print("It appears the specificed reference sequence name is not found in the input fasta file. "
              "Please confirm and try again. Now exiting.")
        sys.exit()

    x = calc_alignedpos(refseq[list(refseq.keys())[0]])
    new_pos = calc_new_offset(x[0], x[1], (startpos, endpos))
    var_regions = []
    print('\nWriting processed sequences to output file....')
    output.progress_bar(4)

    for k, v in refseq.items():
        proc_seq = mask_seq((k, v), new_pos[0], new_pos[1])
        var_regions.append(proc_seq[0])
        output.write_seq(k, proc_seq[1])

    print('\nWriting run information to file....')
    output.progress_bar(4)
    output.run_info(file, refname, refseq.keys(), var_regions)
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))


if __name__ == '__main__':
    main()


