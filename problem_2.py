#%% [markdown]
# # Problem 2: File Recursion
# For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"
#%% [markdown]
# Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().

#%%
import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files = []
    assert(type(suffix) == str), "Suffix has to be a string"
    assert(type(path) == str), "Path has to be a string"
    
    # Check if the current path is a file. If yes, simply return it
    if os.path.isfile(path) and path.endswith(suffix):
        return [path]
    
    # Check the current path for subdirectories and files
    subFiles = os.listdir(path)
    for file in subFiles:
        filePath = path + "/" + file
        if not os.path.isfile(filePath):
            files.extend(find_files(suffix, filePath))
        elif filePath.endswith(suffix):
            files.extend([filePath])
            
    return files

#%% [markdown]
# ## Tests

#%%
# Input: ".c", "./testdir"
# Expected output: Should find all *.c files in ./testdir:
# ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', 
# './testdir/subdir5/a.c', './testdir/subdir1/a.c']
print(find_files(".c", "./testdir"))


#%%
# Input: ".h", "./testdir"
# Expected output: Should find all *.h files in ./testdir:
# ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', 
# './testdir/t1.h', './testdir/subdir1/a.h']
print(find_files(".h", "./testdir"))


#%%
# Input: ".blob", "./testdir"
# Expected output: Should find all *.blob files in ./testdir.
# There are none, so the expected output is: []
print(find_files(".blob", "./testdir"))


#%%
# Input: "", "./testdir"
# Expected output: Should grab all files from ./testdir
# ['./testdir/.DS_Store', './testdir/subdir4/.gitkeep', 
#  './testdir/subdir3/.DS_Store', './testdir/subdir3/subsubdir1/b.h', 
#  './testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', 
#  './testdir/subdir2/.gitkeep', './testdir/subdir5/a.h', 
#  './testdir/subdir5/a.c', './testdir/t1.h', 
#  './testdir/subdir1/a.h', './testdir/subdir1/a.c']
print(find_files("", "./testdir"))


#%%
# NOTE: empty directories are not committed to github, so you might get an error message here.
#
# Input: ".c", "./katdir"
# The given directory is empty, so no matter the suffix it should always
# return []
print(find_files(".c", "./katdir"))
print(find_files("", "./katdir"))
print(find_files("blob", "./katdir"))


#%%
# Input: ".c", "./doesnotexist"
# The given directory does not exist, so it should throw a
# FileNotFoundError.
print(find_files(".c", "./doesnotexist"))

#%% [markdown]
# ## Code to demonstrate the use of some of the OS modules in python
# Just keeping this for personal reference.

#%%

import os

# Let us print the files in the directory in which you are running 
# this script from
print ("current directory: \n", os.listdir("."))

testdir = os.listdir("./testdir")
print ("\ntestdir directory: ", testdir, "\n")

# Let us check if this file is indeed a file!
print ("Is ./ex.py a file? ", os.path.isfile("./ex.py"), "\n")

print("Are the items in testdir files or not? Do they end with .c?")
for file in testdir:
    f = "./testdir/" + file
    print(f, ": \t", os.path.isfile(f), ", ", f.endswith(".c"))


