def list_of_coners(size: int):
    lst = [1]
    step = 2
    index = 0
    for i in range(3, size + 1, 2):
        for j in range(index, index + 4):
            lst.append(lst[j] + step)
        step += 2
        index += 4
    return lst


size = 1001
lst = list_of_coners(size)
print(' + '.join(map(str, lst)))
print(f'Сумма диагоналей размерности {size}: {sum(lst)}')
