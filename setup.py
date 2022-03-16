import os
import os.path
import sys

def goTroughFiles(path, function):
    """
    Go trough all subfiles

    Parameters
    ----------
    path (string) : Name of the root folder
    function : function you want to apply on each file

    Note
    ----
    A function applied on each filed must have a similar signature than the following :
        def myFunc(filePath, data)
    """
    files = os.listdir(path)
    error = False
    for file in files:
        if file != ".metadata":
            filePath = "%s/%s" % (path, file)
            if os.path.isdir(filePath):
                goTroughFiles(filePath, function)
            else:
                state = function(filePath, {
                    "args" : sys.argv
                })
                if not state[0]:
                    print(state[1])
                    error = True

