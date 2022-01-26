numbers = (4, 6, 8, 10, 12, 14, 16)
desired_sum = 20


def find(array, value):
    for i in range(0, len(array)):
        if array[i] == value:
            return i
    return -1


for i in range(0, len(numbers)):
    second_index = find(numbers, desired_sum - numbers[i])
    if second_index >= 0:
        print("[" + str(i) + ", " + str(second_index) + "]")
        break
