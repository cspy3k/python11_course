# int_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(int_lst)
#
# new_lst = []
# for x in int_lst:
#     new_lst.append(x ** 2)
#
# print(new_lst)
#
# cars = [
#     {
#         'make': 'Mercedec',
#         'model': 'S500',
#         'color': 'black'
#     },
#     {
#         'make': 'BMW',
#         'model': 'M5',
#         'color': 'red'
#     },
#     {
#         'make': 'AUDI',
#         'model': 'A7',
#         'color': 'white'
#     }
# ]
#
# def return_dictionary(car):
#     make, model, color = car['make'], car['model'], car['color']
#     return {
#         color: {
#             'make': make,
#             'model': model
#             }
#             }
#
# new = map(return_dictionary, cars)
# for color in new:
#     print(color)
###################################

# data1 = [100, 200, 300, 400, 500]
# data2 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# data3 = [0, 1, 2, 3, 4, 5, 6]
#
# combinations = zip{data1: data2}
# print(list(combinations))

print(list(zip({'a': 1, 'b': 2}, {'c': 3, 'd': 4 })))

