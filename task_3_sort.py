"""
На языке Python предложить алгоритм,
который быстрее всего(по процессорным тикам)
отсортирует данный ей массив чисел. Массив может быть любого размера
со случайным порядком чисел(в том числе и отсортированным).
Объяснить, почему вы считаете, что функция соответствует заданным критериям.
"""


def quick_sort(arr):
    # Если длинна массива меньше/равно 1 то его и возращаем (уже отсортирован)
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]  # Выбираем опорный элемента с середины массива
    left = [x for x in arr if x < pivot]  # добавляем в начало
    middle = [x for x in arr if x == pivot]  # опорный элеменет(середина)
    right = [x for x in arr if x > pivot]  # конец массива
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    test_list1 = [4, 1, 22, 45, 213, 4, 9, 0, 11, 21, 56]
    print(quick_sort(test_list1))
    print()
    test_list2 = [1, 3, 4, 1, 2, 9, 5, 7, 3, 55, 3, 1, 3]
    print(quick_sort(test_list2))