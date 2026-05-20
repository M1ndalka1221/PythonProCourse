# 1. Рядки (Strings):

def length_of_string(user_input):
    return len(user_input)

users_string = input("Enter a string: ")
print(length_of_string(users_string))

def combined_string(string1, string2):
    return string1 + string2

users_first_string = input("Enter a first string: ")
users_second_string = input("Enter a second string: ")

print(combined_string(users_first_string, users_second_string))

# 2. Числа (Int/float):

def squared_sum(number):
    return number * number

print(squared_sum(3))


def sum_numbers(number1, number2):
    return number1 + number2

print(sum_numbers(5, 7))


def division_numbers(number1: int, number2: int):
    return divmod(number1, number2)

print(division_numbers(9, 2))

# 3. Списки (Lists):

def average_value_of_list(nums):
    sum_of_numbers = 0
    for num in nums:
        sum_of_numbers  += num
    return sum_of_numbers / len(nums)


print(average_value_of_list([1, 2, 3, 4, 5]))


def common_elements_of_list(list1, list2):
    return [item for item in list1 if item in list2]

print(common_elements_of_list([1, 2, 3, 4, 5], [1, 3, 5]))

# 4. Словники (Dictionaries):

def keys_of_dict(dictionary1):
    for key in dictionary1.keys():
        print(key)

my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
keys_of_dict(my_dictionary)


def sum_of_dicts(dictionary1, dictionary2):
    return dictionary1 | dictionary2

my_dictionary1 = {'a': 1, 'b': 2}
my_dictionary2 = {'b': 3, 'c': 4}

print(sum_of_dicts(my_dictionary1, my_dictionary2))

# 5. Множини (Sets):

def union_of_sets(set1, set2):
    return set1.union(set2)

my_set1 = {1, 2, 3, 4, 5}
my_set2 = {5, 6}

print(union_of_sets(my_set1, my_set2))


def subset_of_sets(set1, set2):
    return set1.issubset(set2)

print(subset_of_sets(my_set1, my_set2))

# 6. Умовні вирази та цикли:

def is_even(num):
    if num % 2 == 0:
        return f"{num} is even."
    else:
        return f"{num} is odd."


my_number = 6
print(is_even(my_number))


def even_list(list1):
    new_list = []
    for item in list1:
        if item % 2 == 0:
            new_list.append(item)
    return new_list

my_list = [1, 2, 3, 4, 5]
print(even_list(my_list))

# 7. Лямбда-функція:

result = lambda num: f"{num} is even" if num % 2 == 0 else f"{num} is odd"
print(result(5))
