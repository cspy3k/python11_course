import os
import shutil


def show_menu(msg):
    while True:
        print('\n' + msg + '\n\n1. Check directory contents\n2. Remove subdirectories\n3. Sort files (copy to subdirs)\n'
              'Press <enter> or type "exit" to stop execution: ', end='')
        data = input()
        if data.lower() == 'exit' or data == '':
            quit()
        if len(data) == 1 and data in "123":
            break
        msg = 'Input error!!!'
        print('\n\n\n\n\n\n\n\n')
        continue
    print('\n\n\n\n\n\n\n\n')
    return data


def chk_files(sortdir):
    files = []
    exts = []
    filetree = os.walk(sortdir)
    for dirpath_, dirs_, files_ in filetree:
        if dirpath_ == sortdir:
            files = files_
    for filename in files:
        exts.append(os.path.splitext(filename)[1])

    exts = list(set(exts))
    return files, exts


def chk_dirs(sortdir):
    dirs = []
    filetree = os.walk(sortdir)
    for dirpath_, dirs_, files_ in filetree:
        if dirpath_ == sortdir:
            dirs = dirs_
    return dirs


def make_dirs(sortdir):
    return


def remove_dirs(sortdir):
    dirs = chk_dirs(sortdir)
    full_path = os.path.join(os.getcwd(), sortdir)
    if dirs:
        msg = f'Removed {len(dirs)} directories with it\'s content...'
        for dirname in dirs:
            print(dirname)
            shutil.rmtree(os.path.join(full_path, dirname))
    else:
        msg = 'No directories to remove!!!'
    return msg


def calc_targets(sortdir):
    target_move = []
    target_dir = []
    target_file = []

    dirpath = []
    dirs = []
    files = []

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
        # exts.append(extension)
        target_dir.append('sorted_' + extension[1:len(extension)])
        target_file.append(filename)
        a = 'sorted_' + extension[1:len(extension)]
        b = filename

        target_move.append([a, b])
    # exts = list(set(exts))

    # print(exts)
    print(target_dir)
    print(target_file)
    # target_move.append(target_dir)
    # target_move.append(target_file)
    print(target_move)

    return


def copy_target(sortdir):
    calc_targets(sortdir)

    return "TEST"