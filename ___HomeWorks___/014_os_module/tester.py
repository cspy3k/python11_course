import os
# import functions
print(os.getcwd())
sortdir = 'needs_sorting'
full_path = os.path.join(os.getcwd(), sortdir)
print(full_path)
print(os.path.basename(full_path))
print(os.path.dirname(full_path))
# os.chdir('needs_sorting')
dirpath = []
files = []
exts = []
filetree = os.walk(sortdir)
for dirpath_, dirs_, files_ in filetree:
    if  dirpath_ == sortdir:
        dirs = dirs_
        files = files_
    print(dirpath_, dirs_, files_)
    pass
print(dirpath, dirs, files)
quit()
for filename in files:
    exts.append(os.path.splitext(filename)[1])
exts = list(set(exts))
#
#
#
# print(functions.menu())
# import os
# import functions
# # import re
#
# global dirpath, dirnames, filenames
# dirpath, dirnames, filenames = [], [], []
#
# choice = functions.menu()
#
# if choice == "1":
#     files,exts = functions.chk_dir()
#
#
#
# filetree = os.walk('needs_sorting/')
#
# dirlist = []
# print(type(dirlist))
#
#
# for dirpath, dirnames, filenames in filetree:
#     print('Current dir: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)
#
# # if not dirnames:
# #     print(f'No directories found in "{dirpath}"...')
# # else:
# #     print(f'Some directories found in "{dirpath}", cleaning up!!!')
# #     for dirname in dirnames:
# #     os.remove()
#
# # find all extensions
# #
# exts = []
# for filename in filenames:
#     print(filename)
#     exts.append(os.path.splitext(filename)[1])
# print(exts)
# exts = list(set(exts))
# print(exts)
#
#
# print(f'There are {len(filenames)} files and {len(exts)} different file extensions.')
