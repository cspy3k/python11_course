import os

files = os.walk('needs_sorting')

# if not os.path.isdir('images'):
#     os.mkdir('images')
# if not os.path.isdir('music'):
#     os.mkdir('music')
# if not os.path.isdir('text'):
#     os.mkdir('text')

for folder in ['images', 'text', 'music']:
    if not os.path.isdir(folder):
        os.mkdir(folder)

# for dirs, dirnames, filenames in files:
#     for name in fn:
#         file_path = os.path.splitext(name)[1]
#         if os.path.splitext(name)[1] == '.png' or os.path.splitext(name)[1] == '.jpg':
#             os.rename(f'needs_sorting/{name}', f'../img/{name}')

for dirs, dirnames, filenames in files:
    for name in fn:
        file_path = os.path.splitext(name)[1]
        if file_path == '.png' or file_path == '.jpg':
            os.rename(f'needs_sorting/{name}', f'../img/{name}')
