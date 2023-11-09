import fileinput
import sys
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

filelist = [fileinput.FileInput(f,inplace=True)for f in sys.argv[1].split('\n')]
original = [line.strip() for line in sys.argv[2].split('\n')]
modified = [line.strip() for line in sys.argv[3].split('\n')]

print(original)
print(modified)
print(filelist)

replaced = False
for file in filelist:
    for line in file:
      for original_str, modified_str in zip(original, modified):
        if original_str in line:
           print(line.replace(original_str, modified_str), end='')
           replaced = True
           break
      if not replaced:
        print(line, end='')
      else:
         replaced = False
