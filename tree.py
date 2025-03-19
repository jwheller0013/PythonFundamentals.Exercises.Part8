import os

# x = os.listdir('/Users/jim/Projects/p1/')
# print(x)

# def lister(name):
#     y = os.path.realpath(str(name))
#     x = os.path.isdir(y)
#     if x == True:
#         dir_list = []
#         dir_list = os.listdir(os.path.realpath(y))
#         print(dir_list)
#         for i in dir_list:
#             lister(dir_list(i))
#     if x == False:
#         pass

# lister('Tasty')

# for root, dirs, files in os.walk('/Users/jim/Projects/p1/Tasty/'):
#     for file in files:
#         print(os.path.join(root,file))
#os.walk seems to be the key to list out directory told do not need walk() by Kris

# def pathing():
#     path = os.path.realpath('p1')
#     for root, dirs, files in os.walk(str(path)):
#         for file in files:
#             print(os.path.join(root, file))
#
# pathing()

#Given a file path (absolute or relative)

#write to a file all of the contents of the directory and the child directories bellow

#cwd only gets from current directory cannot take variables
cwd = os.getcwd()
# print(cwd)
# # print(os.path.isdir(cwd), True)
# # print(os.path.isfile(cwd), False)
# print(os.path.isdir(cwd+'/'+'tree.py'), False)
# print(os.path.isfile(cwd+'/'+'tree.py'), True)
# print(os.path.isdir(os.path.join(cwd,'tree.py')), False)

def list_dir (start, alist):
    dircontents = os.listdir(os.path.realpath(start))
    for i in dircontents:
        newpath = os.path.join(start, i)
        if os.path.isfile(cwd+'/'+ str(newpath)) == True:
            alist.append(newpath)
        elif os.path.isdir(cwd+'/'+ str(newpath)) == True:
            list_dir(newpath, alist)
#slide 162 in thinkpython2 pdf

list_test = []
list_dir('p1', list_test)
print(list_test)


#!!!!! must run in terminal ensuring you are at a clear terminal not in a folder already!!!!!
# only works in current directory you run from