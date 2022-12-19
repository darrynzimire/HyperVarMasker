# encoding=utf-8


def manpage():

    text = 'HyperVarMasker \n' \
           'author: Darryn Zimire \n' \
           'author email: darryn.zimire@uct.ac.za \n' \
           'source: http://github.com/darrynzimire/HyperVMasker \n' \
           'License: MIT \n' \
            'Date: December 2022 \n'\
           '\n' \
           'HyperVarMasker is a simple command-line interface implemented in Python 3. \n' \
           'The tool masks or slice out the hypervariable regions in an amino-acid multi-sequence alignment \n' \
           'stored in a FASTA database. The tool is specifically built for HIV-1 sequencing data but is organism\n' \
           'agnostic, provided that a valid FASTA database and target slicing positions are set as parameters. \n' \


    print(text)
    '\n'
    print('program: hypervmasker\n'
          "\n"
          'This is the commands and arguments to run the application. \n'
          "\n"
          'usage: hypervmasker -infile <Input_alignment.fasta>  -offset <132 152>  -refname <HXB2> \n'
          "\n"
          'Parameters: \n'
          '\n'
          '-infile           Input FASTA file to be processed \n'
          '-offset           start and end positions of the target regions (start, end) \n'
          '-refname          name of the reference sequence in the input FASTA file \n'
          '-outfilename      output files prefix \n'

          )


def main():
    manpage()


if __name__ == '__main__':
    main()