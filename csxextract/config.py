import os

# URL to Grobid service
GROBID_HOST = 'http://localhost:8080'

# Path to PDFBox jar
PDF_BOX_JAR = os.path.expanduser('~/bin/pdfbox-app-1.8.4.jar')

# PAth to ParsCit perl script for extraction
PARSCIT_PATH = os.path.expanduser('~/bin/pars_cit/bin/citeExtract.pl')

# Path to Filter Classificaiton JAR
FILTER_JAR_PATH = os.path.expanduser('~/bin/classifier/classifier.jar')
FILTER_ACL_PATH = os.path.expanduser('~/bin/classifier/acl')
FILTER_TRAIN_DATA_PATH = os.path.expanduser('~/bin/classifier/train_str_f43_paper.arff')

# Path to PDFFigures binary
PDFFIGURES_PATH = os.path.expanduser('~/bin/pdffigures')

# Path to Algorithms extractor JAR
ALGORITHMS_JAR_PATH = os.path.expanduser('~/bin/algextract/bin/algo_extractor.jar')
ALGORITHMS_PERL_PATH = os.path.expanduser('~/bin/algextract/bin/perl')
