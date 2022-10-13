file_1_lists = []

with open('1.txt', 'r', encoding='utf-8') as file_list:
    lines = file_list.readlines()
    for line in lines:
        file_include = line.strip()
        file_1_lists.append(file_include)
print(file_1_lists)

from os import path
full_name = path.basename(r'C:\Users\Dmitrii\Desktop\Netology\Homeworks\Writer_to_file\1.txt ')
name_1 = path.splitext(full_name)[0]

print("Файл номер " + str(name_1))
number_of_elements_1 = len(file_1_lists)
print("Количество строк " + str(number_of_elements_1))


file_2_lists = []

with open('2.txt', 'r', encoding='utf-8') as file_list:
    lines = file_list.readlines()
    for line in lines:
        file_include = line.strip()
        file_2_lists.append(file_include)
print(file_2_lists)

from os import path
full_name = path.basename(r'C:\Users\Dmitrii\Desktop\Netology\Homeworks\Writer_to_file\2.txt ')
name_2 = path.splitext(full_name)[0]
print("Файл номер " + str(name_2))
number_of_elements_2 = len(file_2_lists)
print("Количество строк " + str(number_of_elements_2))


file_3_lists = []
with open('3.txt', 'r', encoding='utf-8') as file_list:
    lines = file_list.readlines()
    for line in lines:
        file_include = line.strip()
        file_3_lists.append(file_include)
print(file_3_lists)
from os import path
full_name = path.basename(r'C:\Users\Dmitrii\Desktop\Netology\Homeworks\Writer_to_file\3.txt ')
name_3 = path.splitext(full_name)[0]
print("Файл номер " + str(name_3))
number_of_elements_3 = len(file_3_lists)
print("Количество строк " + str(number_of_elements_3))

# fl = file_1_lists + file_2_lists + file_3_lists
# print("финальный список " + str(fl))

fl_1 = [number_of_elements_1, file_1_lists]
print(fl_1)
fl_2 = [number_of_elements_2, file_2_lists]
print(fl_2)
fl_3 = [number_of_elements_3, file_3_lists]
print(fl_3)

full_list = [fl_1, fl_2, fl_3]

a = full_list
a.sort()
print("New sorted list A is % s" % (a))


with open('output.txt', 'w', encoding='utf-8') as filehandle:
    for listitem in a:
        filehandle.write('%s\n' % listitem)




        # recipes = {recipes_name: []}
        # number_eng = cook_book_list.readline()
#         for i in range(int(number_eng)):
#             eng = cook_book_list.readline()
#             ingredient_name, quantity,measure = eng.split(' | ')
#             num_eng = {"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure.strip()}
#             recipes[recipes_name].append(num_eng)
#
#         cook_book_list.readline()
#         cook_book.append(recipes)
#
# print(cook_book)