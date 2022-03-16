from fileFunction import checkFile, search
from setup import goTroughFiles
import sys

functions = {
    "check" : checkFile,
    "search" : search
}

if len(sys.argv) == 1:
    raise ValueError("No parameters given")
elif sys.argv[1] not in functions.keys():
    raise ValueError("Could not find %s, are you sure that function is registered ?" % sys.argv[1])
else:
    goTroughFiles("files", functions[sys.argv[1]])

