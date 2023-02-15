import os
import shutil

# a = [[0, 1, 2, 3, 4],[10, 11, 12, 13, 14]]
# print(a)
# a[1].append(100)
# print(a)
print(os.getcwd())
sortdir = 'needs_sorting'
full_path = os.path.join(os.getcwd(), sortdir)
print(full_path)
print(os.path.basename(full_path))
print(os.path.dirname(full_path))

target_move = []
target_dir = []
target_file = []

dirpath = []
dirs = []
files = []
exts = []
ext_files = []
filetree = os.walk(sortdir)
for dirpath_, dirs_, files_ in filetree:
    if dirpath_ == sortdir:
        dirs = dirs_
        files = files_
for filename in files:
    # print(filename)
    # target_file.append(filename)
    # print(os.path.splitext(filename[1]))
    # a = [os.path.splitext(filename[1])]
    extension = os.path.splitext(filename)[1]
    exts.append(extension)
    target_dir.append('sorted_' + extension[1:len(extension)])
    target_file.append(filename)
    a = 'sorted_' + extension[1:len(extension)]
    b = filename

    target_move.append([a, b])
exts = list(set(exts))

print(exts)
print(target_dir)
print(target_file)
# target_move.append(target_dir)
# target_move.append(target_file)
print(target_move)

os.chdir(sortdir)
for dir, file in target_move:
    print(dir, file)
    shutil.copy2(file, dir)
#    full_file = os.path.join(full_path, file)
#    full_dir = os.path.join(full_path, dir)
#    print(full_file)
#    print(full_dir)
#    shutil.copy2(full_file, full_dir)
os.chdir('../')
print(os.getcwd())
#
