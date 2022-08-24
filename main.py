ARRAY = ['String', '123', '--', 'This is long string', 'ABC']
arr2 = []

if __name__ == '__main__':
    for i in range(len(ARRAY)):
        if len(ARRAY[i]) <= 3:
            arr2.append(ARRAY[i])
    print(f'Исходный массив: {ARRAY}.')
    print(f'Новый массив: {arr2}')
