### HyperVarMasker: Masking hypervariable regions in multi-sequence alignment FASTA database

HyperVarMasker is a simple command-line interface implemented in Python 3. 
The tool masks or slice out the hyper-variable regions in an amino acid multi-sequence alignment 
stored in a FASTA database. The tool is specifically built for 
HIV-1 multiple sequence alignments but is organism agnostic, provided that 
a valid FASTA database and target cutting positions are set as parameters.

### System requirements:

* Python >= 3
* biopython
* pandas

### Installation:

The source code can be downloaded from the HIV-Diversity Github repository,
provided that the user has access permissions to the repository.

### Usage:

Here is a list of all the arguments needed to run HypeVarMasker:

| Parameters	  | Description 	                                                               |    	
|--------------|-----------------------------------------------------------------------------|
| -infile  	 | The input FASTA database to be processed	                                   |  
| -offset	   | The start and end positions of the target region in the reference sequence	 |  
| -refname   | The name of the reference sequence in the FASTA database<br/>               |


### Run example

hypevarmasker-run -infile Input_alignment.fasta -offset 132 152  -refname HXB2_Env


### License:

This application is licensed under the MIT License. See [LICENSE.md](LICENSE.md) file
for more information.


### Author:
Darryn Zimire, MSc. Bioinformatics (SU)  
Email: darryn.zimire@uct.ac.za  
Affiliation: UCT HIV Diversity Research Group



