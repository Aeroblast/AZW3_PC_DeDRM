import sys
import os
import re
#most codes are borrowed from DeDRM_Tools

import mobidedrm
import k4mobidedrm
from argv_utils import add_cp65001_codec, set_utf8_default_encoding, unicode_argv
add_cp65001_codec()
set_utf8_default_encoding()

infile=sys.argv[1]
if  not os.path.isfile(infile):
    print 'Input file not exist!'
    exit()
outdir=os.path.dirname(infile)

kindlekeyfile=os.path.dirname(os.path.realpath(sys.argv[0]))+'\kindlekey.k4i'


if not os.path.exists(kindlekeyfile):
    import kindlekey
    try:
        kindlekey.getkey(kindlekeyfile)
    except:
        print 'Get Key Failed'
        exit()
        
pidnums = []
serialnums = []

kDatabaseFiles = [kindlekeyfile]


rv = k4mobidedrm.decryptBook(infile, outdir, kDatabaseFiles, [], serialnums, pidnums)
