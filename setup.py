import setuptools
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='HyperVarMasker',
    version='0.0.1',
    description='A simple tool to mask hypervariable regions in a multiple-sequence alignment FASTA database',
    long_description=long_description,

    author='Darryn Zimire',
    author_email='darryn.zimire@uct.ac.za',
    license='MIT LICENSE',

    classifiers=[
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    # What does your project relate to?
    keywords='bioinformatics computational-biology',
    install_requires=['pandas',
                      'biopython',
                      ],
    packages=setuptools.find_packages(),
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'hypervmasker=man:main',
            'hypervmasker=main:main',


        ],

    },
)

