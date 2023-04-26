'''
Напишите программу, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d O
utput: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


'''
import string

# s = input('Введите строку: ')
# list_of_chars = list(s)
# letter_to_count = dict()
# for c in list_of_chars:
#     if c in letter_to_count:
#         letter_to_count[c] = letter_to_count[c] + 1
#     else:
#         letter_to_count[c] = 0
#     count_of_repeats = letter_to_count[c]
#     print(f'{c}_{count_of_repeats}' if count_of_repeats > 0 else c, end=' ' )


'''
Задача №27. Решение в группах Пользователь вводит текст(строка). 
Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов. 
Определите, сколько различных слов содержится в этом тексте. 
Input: She sells sea shells on the sea shore 
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells 
Output: 13
'''

# str_split = (
#     "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells").lower().split()
# str_cnt = {}
# for i in str_split:
#     str_cnt[i] = str_cnt.get(i, 0) + 1
# print(f"Number of words in the text is : {len(str_cnt)}")
# print(str_cnt)

# import string
# str_split = (
#     "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells").lower()
# for ch in string.punctuation: # все знаки пунктуации
#     str_split=str_split.replace(ch, ' ')
# str_cnt = set(str_split)
# print(f"Number of words in the text is : {len(str_cnt)}")

'''
Задача №29. Решение в группах Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
“Задана последовательность неотрицательных целых чисел. 
Требуется определить значение наибольшего элемента последовательности, 
которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
Однако 2 друга оказались не такими смышлеными. 
Никто из ребят не смог до конца сделать это задание. 
Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
За помощью товарищи обратились к Вам, студентам.

'''

# n = 1
# max_number = -1
# while n != 0:
#     if n > max_number:
#         max_number = n
#     n = int(input('Введите число: '))
# print(max_number if max_number != 0 else "Вы ничего не ввели")
