# with open('text_files/python.png', 'rb', ) as file:
#     data = file.read()
#     with open('text_files/python_copy.png', 'wb') as wfile:
#         wfile.write(data)
with open('text_files/python.png', 'rb', ) as file:
    with open('text_files/python_copy.png', 'wb', ) as wfile:
        data = file.read(1024)
        while len(data) > 0:
            wfile.write(data)
            data = file.read(4096)