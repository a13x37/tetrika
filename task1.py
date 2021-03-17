def task(array):
    listed_array = list(array)
    try:
        index = listed_array.index('0')
        return index
    except ValueError:
        return 'Ошибка! В заданном массиве нет нулей.'


print(task("111111111111111111111111100000000"))
