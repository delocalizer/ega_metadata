#!/bin/bash

# generate a PBS job array to checksum/encrypt/checksum a list of files for
# transfer to EGA.

#Copyright 2022 QIMR Berghofer Medical Research Institute
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

if [ -z $1 ] | [ -z $2 ] ; then
        echo "Usage: $0 FILELIST OUTPUTDIR"
        exit 1
fi

# list of files to prepare (their original location)
filelist=$(readlink -f $1)
nfiles=$(wc -l < $filelist)
if (( $nfiles < 2 )); then
        echo "PBS array requires > 1 elements"
        exit 1
fi

# output directory for gpg and md5 files
outputdir=$2

qsub <<PBSSCRIPT
#PBS -l walltime=2:00:00
#PBS -l ncpus=2,mem=1gb
#PBS -N md5_gpg_md5
#PBS -J 1-$nfiles

# id of public key to encrypt with (must be in user's gpg keyring and trusted)
key_id="European Genome-Phenome Archive"

# the file for this job array element
filename=\$(sed -n "\${PBS_ARRAY_INDEX}p" $filelist)
filebase=\$(basename \$filename)

# md5sum, gpg encrypt and md5sum
tee >(md5sum |sed -e "s|\-$|\$filebase|g" > $outputdir/\$filebase.md5) < \$filename \
        | gpg --batch -r "\$key_id" -e \
        | tee >(md5sum |sed -e "s|\-$|\$filebase.gpg|g" > $outputdir/\$filebase.gpg.md5) > $outputdir/\$filebase.gpg
PBSSCRIPT
