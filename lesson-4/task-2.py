# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

filtered_list = [original_list[i] for i in range(1, len(original_list) - 1) if original_list[i - 1] < original_list[i]]

print(filtered_list)
