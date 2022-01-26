# def sort(array):
#     swapped = False
#     for i in range(len(array) -1, 8, -1):
#         for j in range(i):
#             if array[j] > array[j+1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#                 swapped = True
#         if swapped:
#             swapped = False
#         else:
#             break
#     return array
#
#
# arr_1 = [76, 90, 122, 34, 5, 98, 14, 8]
# print(f'Sorted list: {sort(arr_1)}')

list_1 = ['Elle', 'Adi', 'Lol']
# for i in list_1:
#     if i == 'Elle':
#         print(i)
p = [i for i in list_1 if i == 'Elle']
print(p)


o = [i for i in range(20) if i % 2 == 0]
print(o)

# list_1 = ['Elle', 'Adi', 'Lol']
# for i in list_1:
#     if i == 'Elle':
#         print(i)