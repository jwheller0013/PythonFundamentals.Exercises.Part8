import os

#Given a file path (absolute or relative)

#write to a file all of the contents of the directory and the child directories bellow

cwd = os.getcwd()

def list_dir (start, alist):
    dircontents = os.listdir(os.path.realpath(start))
    with open('test_file3', 'a') as f:
        f.write(str(os.path.realpath(start)) + "\n")
        f.close()
    for i in dircontents:
        newpath = os.path.join(start, i)
        if os.path.isfile(cwd+'/'+ str(newpath)) == True:
            alist.append(newpath)
            with open('test_file3', 'a') as f:
                f.write(str(i) + "\n")
                f.close()
        elif os.path.isdir(cwd+'/'+ str(newpath)) == True:
            list_dir(newpath, alist)
#slide 162 in thinkpython2 pdf

# list_test = []
# list_dir('PythonFundamentals.Exercises.Part8', list_test)

#!!!!! must run in terminal ensuring you are at a clear terminal not in a folder already!!!!!
# only works in current directory you run from