import os

#======================
#  Task: Find File
#======================

def findFile(path, targetFile):
    """
    Recursively searches for a target file in a given directory path.

    Parameters:
        path (str): The directory path to search in.
        targetFile (str): The name of the file to find.

    Returns:
        bool: True if the target file is found, False otherwise.

    Example:
        >>> findFile("C:/Users/John/Documents", "report.docx")
        True
    """

    ########################
    # Insert your code here:
    #  (replace the underscores)
    #-----------------------       
    if os.path.isfile(path):
        # split the path into pieces
        if os.path.basename(path) == targetFile:
            return True
        else:
            return False

    retVal = False
    if os.path.isdir(path):
        for fileName in os.listdir(path):
            childpath = os.path.join(path, fileName) # current path combined with file name
            retVal = findFile(childpath, targetFile)
            if retVal == True:
                return True
    return retVal