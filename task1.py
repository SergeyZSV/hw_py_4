# Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.
import random


def sort_numbers(numbers: list):
    for i in range(0, len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp


with open('file_task1.txt', 'w') as file:
    for i in range(1, 10):
        file.write(str(random.randint(1, 100)) + '\n')

with open('file_task1.txt', 'r') as file:
    number_list = file.readlines()

for k in range(0, len(number_list)):
    number_list[k] = int(number_list[k])

print(f'Исходный список: {number_list}')
sort_numbers(number_list)
print(f'Отсортированный список: {number_list}')

with open('file_task1.txt', 'a') as file:
    file.writelines('\nSorted list \n | | | \n V V V \n')
    for number in number_list:
        file.writelines(str(number) + '\n')