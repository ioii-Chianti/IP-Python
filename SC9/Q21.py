def count_files(p = '.'):
    import os
    if not os.path.isdir(p):   # p is the name of a file, not a directory
        return 1
    dir_content = os.listdir(p)   # get list of names (files & dir)
    return sum(map(count_files, dir_content))   # sum recursive count of content

print(count_files())