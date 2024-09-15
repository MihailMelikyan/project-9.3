first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(elem_1) -len(elem_2)) for elem_1,elem_2 in zip(first,second) if len(elem_1) != len(elem_2))
print(list(first_result))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_result))



