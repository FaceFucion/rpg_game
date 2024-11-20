def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Функция двоичного поиска
def binary_search(val, arr):
    first = 0
    last = len(arr) - 1
    result_ok = False
    pos = -1

    while first <= last and not result_ok:
        middle = (first + last) // 2
        if val == arr[middle]:
            pos = middle
            result_ok = True
        elif val > arr[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print(f"Элемент найден на позиции {pos}.")
    else:
        print("Элемент не найден.")

# Исходный неотсортированный список
unsorted_list = [34, 7, 23, 32, 5, 62]
print("Неотсортированный список:", unsorted_list)

# Сортировка списка
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

# Поиск элемента в отсортированном списке
search_element = 23
binary_search(search_element, sorted_list)