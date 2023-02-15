import functions
# import os
# import time
# import re

msg = ''
sortdir = 'needs_sorting'
print('\n\n\n\n\n\n\n\n\n')

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
        msg = functions.remove_dirs(sortdir)
        continue

# create subdirectories for sorting (and copy each file to it's location)
    if choice == "3":
        msg, result = functions.make_dirs(sortdir)
        if result:
            msg += functions.copy_files(sortdir)
        else:
            print('File copying aborted...')
        continue

# # copy files to subdirectories made
#     if choice == "4":
#         msg = functions.copy_target(sortdir)
#         continue
