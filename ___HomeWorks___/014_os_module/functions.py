import os
import shutil


def show_menu(msg):
    while True:
        print('\n' + msg + '\n\n1. Check directory contents\n2. Remove subdirectories'
              '\n3. Sort files (make subdirs and copy files)\n'
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


def remove_dirs(sortdir):
    dirs = chk_dirs(sortdir)
    full_path = os.path.join(os.getcwd(), sortdir)
    if dirs:
        msg = f'Removed {len(dirs)} directories with content...'
        for dirname in dirs:
            print(dirname)
            shutil.rmtree(os.path.join(full_path, dirname))
    else:
        msg = 'No directories to remove!!!'
    return msg


def calc_targets(sortdir):
    target_move = []
    files = []

    filetree = os.walk(sortdir)
    for dirpath_, dirs_, files_ in filetree:
        if dirpath_ == sortdir:
            files = files_
    for filename in files:
        extension = os.path.splitext(filename)[1]
        target_move.append(['sorted_' + extension[1:len(extension)], filename])
    return target_move


def make_dirs(sortdir):
    err_num = 0
    files, exts = chk_files(sortdir)
    if not len(files):
        return f'"../{sortdir}" directory is empty!!!'
    else:
        for extension in exts:
            dirname = 'sorted_' + extension[1:len(extension)]
            print(dirname, end='')
            try:
                os.makedirs(os.path.join(sortdir, dirname))
            except:
                print(' directory creation failed, makedirs error!!!')
                err_num += 1
                continue
            else:
                print(' directory created...')
                continue
        if err_num:
            msg = f'Failed to create {err_num} directories, try use option 2!!! ', False
        else:
            msg = f'{len(exts)} directories created,  ', True
        return msg


def copy_files(sortdir):
    target_move = calc_targets(sortdir)

    os.chdir(sortdir)
    err_num = 0
    file_num = 0
    for dirname, file in target_move:
        print(f'"{file}" to "{dirname}" ', end='')
        try:
            shutil.copy2(file, dirname)
        except:
            err_num += 1
            print('copying failed!!!')
            continue
        else:
            file_num += 1
            print('copied...')
            continue
    os.chdir('../')
    if err_num:
        msg = f'failed to copy {err_num} files, try use option 2!!!'
    else:
        msg = f'{file_num} files successfully copied. '
    return msg
