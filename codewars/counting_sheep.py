def count_sheep1(arr):
    return len([s for s in arr if s is True])


def count_sheep2(arr):
    return arr.count(True)


sheep = [True, False, True, True, True]

print('count_sheep1', count_sheep1(sheep))
print('count_sheep2', count_sheep2(sheep))
