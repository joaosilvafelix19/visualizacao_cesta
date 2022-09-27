import os

def getParentDir(CurrentPath, levels = 1): 
    current_new = CurrentPath
    for i in range(levels + 1): 
        current_new = os.path.dirname(current_new) 
    return os.path.abspath(current_new).replace("\\", "/")