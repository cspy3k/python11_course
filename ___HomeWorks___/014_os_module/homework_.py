import os
import shutil
import functions
# import time
# import re

msg = ''
sortdir = 'needs_sorting'
full_path = os.path.join(os.getcwd(), sortdir)
print(full_path)
dirpath, dirs, filenames, files, exts = [], [], [], [], []

while True:
    choice = functions.show_menu(msg)
    msg = ''

    # check directory, scan for files and their different extensions
    if choice == "1":
        files, exts = functions.chk_files(sortdir)
        if len(files):
            msg = f'There are {len(files)} files and {len(exts)} different file extensions.'
        else:
            msg = f'"../{sortdir}" directory is empty!!!'
        continue

# remove previously created sorted dir-s
    if choice == "2":
#        dirs = functions.chk_dirs(sortdir)
        msg = functions.remove_dirs(sortdir)
        continue

# create subdirectories for sorting and copy each file to it's location
    if choice == "3":
        msg = functions.copy_target(sortdir)
        # err_num = 0
        # files, exts = functions.chk_files(sortdir)
        # if not len(files):
        #     msg = f'"../{sortdir}" directory is empty!!!'
        #     continue
        # else:
        #     for extension in exts:
        #         dirname = 'sorted_' + extension[1:len(extension)]
        #         print(dirname, end='')
        #         try:
        #             os.makedirs(sortdir + '\\' + dirname)
        #         except:
        #             print(' not created, makedirs error!!!')
        #             err_num += 1
        #             continue
        #         else:
        #             print(' directory created...')
        #             continue
        #     if err_num:
        #         msg = f'Failed to create {err_num} directories, try use option 2!!!'
        #     else:
        #         msg = f'{len(exts)} directories created. '
        #         for dirname in dirs:
        #             print(dirname)
        #     continue
