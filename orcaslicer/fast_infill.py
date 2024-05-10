#!python
import sys
import re
import os

source_file=sys.argv[1]

with open(source_file, "r") as f:
    lines = f.readlines()

# Process file to .gcode file for post-process script 
if (source_file.endswith('.gcode')):
    dest_file = re.sub('\.gcode$','',source_file)
    try:
        os.rename(source_file, dest_file+".sqv.bak")
    except FileExistsError:
        os.remove(dest_file+".sqv.bak")
        os.rename(source_file, dest_file+".sqv.bak")
    dest_file = re.sub('\.gcode$','',source_file)
    dest_file = dest_file + '.gcode'
else:
    dest_file = source_file
    os.remove(source_file)

in_infill = False

# Open the destination file and write
with open(dest_file, "w") as of:
    for line_Index in range(len(lines)):
        oline = lines[line_Index]
        # Parse gcode line
        if oline.startswith(';TYPE:Sparse infill'):
            in_infill = True
            of.write(oline)
            of.write('_USE_INFILL_SQV\n')
        elif oline.startswith(';TYPE') and in_infill:
            in_infill = False
            of.write(oline)
            of.write('_USE_NORMAL_SQV\n')
        else:
            of.write(oline)

of.close()
f.close()
