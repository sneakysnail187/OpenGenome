import numpy as np
from Bio.Affy import CelFile

with open ("GSM7585785_31116_HF-30512_RA_SPR856_HGU133P.CEL", "r") as handle:
    c = CelFile.read(handle)

    print (c.ncols, c.nrows)
    print(c.intensities)
    print(c.stdevs)
    print(c.npix)