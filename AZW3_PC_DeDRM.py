
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
outdir=''

kindlekeyfile=sys.path[0]+'/kindlekey.k4i'


if not os.path.exists(kindlekeyfile):
    import kindlekey
    try:
        kindlekey.getkey(kindlekeyfile)
    except:
        pass
        
pidnums = []
serialnums = []

kDatabaseFiles = [kindlekeyfile]


rv = k4mobidedrm.decryptBook(infile, outdir, kDatabaseFiles, [], serialnums, pidnums)