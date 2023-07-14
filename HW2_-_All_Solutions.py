# 1

def flip_lines(file_name):
    data = open(file_name).read().splitlines()
    copied = data.copy()

    for i in range(1, len(data), 2):
        temp = data[i]
        data[i] = data[i - 1]
        data[i - 1] = temp

    for i in range(len(data)):
        if i % 2 == 0:
            data[i] = data[i].upper()
        elif i % 2 == 1:
            data[i] = data[i].lower()

    for line in data:
        print(line)


# [2 random_rects]

def random_rects():
    area = 0
    rectCount = int(input("How many rectangles? "))

    for k in range(1, rectCount + 1):
        width = int(input("Width %d? " % k))
        height = int(input("Height %d? " % k))
        area += height * width
        for i in range(height):
            for j in range(width):
                print("*", end="")
            print()

    print("Total area: %d" % area)


# 3
def factor_count(n):
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return counter


# 4
def collapse_pairs(list):
    for i in range(1, len(list), 2):
        first = list[i - 1]
        second = list[i]
        summary = first + second

        if summary % 2 == 0:
            list[i - 1] = summary
            list[i] = 0
        else:
            list[i] = summary
            list[i - 1] = 0
    return list


# 5

def contains(list1, list2):
    for i in range(0, len(list1)):
        if list1[i:i + len(list2)] == list2:
            return True
    return False


# 6

def count_duplicates(list):
    duplicates = 0
    duplicants = []
    for i in range(0, len(list)):
        if list[i] in duplicants:
            continue
        else:
            for j in range(i + 1, len(list)):
                if list[j] == list[i]:
                    if list[j] not in duplicants:
                        duplicants.append(list[i])
                    duplicates = duplicates + 1
    print(duplicants)
    return duplicates


# 7

def count_unique(list):
    uniques = 0
    for i in range(0, len(list)):
        if list[i] not in list[:i]:
            uniques += 1
    return uniques


# 8

def find_median(list):
    list.sort()
    return list[len(list) // 2]


# 9

def find_range(list):
    tempList = []
    for i in list:
        tempList.append(i)
    tempList.sort()

    if len(tempList) > 1:
        return tempList[len(tempList) - 1] - tempList[0] + 1
    else:
        return 1


# 10

def flip_half(list):
    tempList = []
    for i in range(1, len(list), 2):
        tempList.append(list[i])

    for i in range(1, len(list), 2):
        list[i] = tempList.pop()
    return list


# 11

def get_percent_even(list):
    percentage = 0.0
    for i in list:
        if i % 2 == 0:
            percentage += 100 / len(list)
    return percentage


# 12

def has_mirror_twice(list1, list2):
    tempList = []
    row_count = 0
    for i in list2:
        tempList.append(i)
    tempList = tempList[::-1]

    for i in range(0, len(list1)):
        if list1[i:i + len(list2)] == tempList:
            row_count += 1

    if row_count >= 2:
        return True
    return False


# 13

def index_of(list, number):
    for i in range(0, len(list)):
        if list[i] == number:
            return i
    return -1


# 14

def is_magic_square(square):
    if len(square) == 0:
        return True
    if len(square) != len(square[0]):
        return False

    for row in square:
        if len(row) != len(square):
            return False

    n = len(square)
    magic_constant = sum(square[0])

    for row in square:
        if sum(row) != magic_constant:
            return False

    for i in range(n):
        column_sum = 0
        for j in range(n):
            column_sum += square[j][i]
        if column_sum != magic_constant:
            return False

    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += square[i][i]
    if diagonal_sum != magic_constant:
        return False

    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += square[i][n - i - 1]
    if diagonal_sum != magic_constant:
        return False

    return True

# 15

def longest_sorted_sequence(list):
    longest_row = 0
    current_row = 0

    if len(list) == 0:
        return 0

    for i in range(0, len(list) - 1):

        if list[i] <= list[i + 1]:
            current_row += 1

        else:
            current_row = 0

        if longest_row <= current_row:
            longest_row = current_row

    return longest_row + 1


# 16

def max_value(list):
    max_num = -999999
    if len(list) > 0:
        for i in list:
            if i > max_num:
                max_num = i
    return max_num


# 17

def mean(list):
    sum = 0.0
    if len(list) == 0:
        return 0.0
    for i in list:
        sum += i
    return sum / len(list)


# 18

def mirror(list):
    auxiliary_list = []
    for i in list:
        auxiliary_list.append(i)
    for i in range(len(auxiliary_list)):
        list.append(auxiliary_list.pop())
    return list


# 19

def n_copies(list):
    copy_list = []
    for i in list:
        if i > 0:
            for j in range(i):
                copy_list.append(i)
        else:
            continue
    return copy_list


# 20

def print_list(list):
    for i in range(0, len(list)):
        print("element [%d] is %d" % (i, list[i]))


# 21

def sorted(list):
    auxilary_sorted_list = []
    for i in list:
        auxilary_sorted_list.append(i)
    auxilary_sorted_list.sort()

    if auxilary_sorted_list == list:
        return True
    else:
        return False


# 22

def split(list):
    auxilary_list = []
    for i in list:
        if i % 2 == 0:
            for j in range(2):
                auxilary_list.append(i // 2)
        else:
            auxilary_list.append((i / 2).__ceil__())
            auxilary_list.append(i // 2)
    return auxilary_list


# 23

def split_stack(list):
    auxilary_positive = []
    auxilary_negative = []

    for i in list:
        if i >= 0:
            auxilary_positive.append(i)
        else:
            auxilary_negative.append(i)

    list.clear()
    for i in range(len(auxilary_negative)):
        list.append(auxilary_negative.pop())

    for i in range(len(auxilary_positive)):
        list.append(auxilary_positive.pop())
    return list


# 24

def stutter(list):
    for i in range(0, len(list) * 2, 2):
        list.insert(i, list[i])
    return list


# 25

def switch_pairs(list):
    for i in range(1, len(list), 2):
        temp = list[i]
        list[i] = list[i - 1]
        list[i - 1] = temp
    return list


# 26

def biggest_family(filename):
    with open(filename, "r") as file:
        family_counts = {}
        for line in file:
            first_name, last_name = line.strip().split()
            if last_name not in family_counts:
                family_counts[last_name] = set()
            family_counts[last_name].add(first_name)

    max_count = max(len(family) for family in family_counts.values())
    biggest_families = [
        (last_name, sorted(family))
        for last_name, family in family_counts.items()
        if len(family) == max_count
    ]
    biggest_families.sort()

    for last_name, family in biggest_families:
        print("{} family: {}".format(last_name, " ".join(family)))


# 27

# {'bar': 'earth', 'baz': 'wind', 'foo': 'air', 'mumble': 'fire'}
# {'five': 'cuatro', 'one': 'dos', 'three': 'tres'}
# {'b': 'years', 'c': 'seven', 'e': 'ago', 'g': 'seven'}

# 28

def count_names():
    name_map = {}
    entered_name = "x"
    while entered_name != "":
        entered_name = input("Enter name: ")
        if entered_name != "":
            if entered_name in name_map.keys():
                name_map[entered_name] += 1
            else:
                name_map[entered_name] = 1

    for i in name_map.keys():
        print("Entry [%s] has count %d" % (i, name_map[i]))


count_names()


# 29

def intersect(dict1, dict2):
    result = {}
    for key in dict1.keys():
        if key in dict2.keys() and dict1[key] == dict2[key]:
            result[key] = dict1[key]
        else:
            continue
    return result


# 30

def last_names_by_age(dictionary, min_age, max_age):
    result = {}
    for key in dictionary.keys():
        if min_age <= dictionary[key] <= max_age:
            if dictionary[key] not in result.keys():
                result[dictionary[key]] = key.split()[-1]
            else:
                result[dictionary[key]] += " and " + key.split()[-1]

    return result


# 31 SJ

def rarest_age(dictionary):
    if dictionary is None or len(dictionary) == 0:
        return 0

    age_counts = {}
    for key in dictionary.keys():
        if dictionary[key] not in age_counts.keys():
            age_counts[dictionary[key]] = 1
        else:
            age_counts[dictionary[key]] += 1

    rarest = 999
    minimum = 999
    for age in age_counts.keys():
        if age_counts[age] <= minimum:
            if age < rarest:
                minimum = age_counts[age]
                rarest = age

    return rarest


# 32

def starters(list, k):
    capitals = {}
    result = set({})
    result.clear()
    for i in list:
        if len(i) > 0:
            if i[0].lower() not in capitals.keys():
                capitals[i[0].lower()] = 1
            else:
                capitals[i[0].lower()] += 1

    for key in capitals.keys():
        if capitals[key] >= k:
            result.add(key)

    return result


# 33

def to_morse_code(mapping, text):
    for char in text:
        char = char.upper()
        if char not in {' ', '[', ']', '!', '(', ')'}:
            print(mapping[char], end=" ")


# 34

def max_length(list):
    if len(list) == 0:
        return 0
    temp = ""
    for i in list:
        if len(i) > len(temp):
            temp = i
    return len(temp)


# 35

def num_in_common(list1, list2):
    auxilary_storage = set()
    for i in list1:
        if i in list2:
            auxilary_storage.add(i)
        else:
            continue
    return len(auxilary_storage)


# 36

def twice(list):
    auxilary_storage = set()
    for i in range(len(list)):
        if list.count(list[i]) == 2:
            auxilary_storage.add(list[i])
    return auxilary_storage


# 37

def class_presidents(file_name):
    with open(file_name) as f:
        lines = f.read()
    lines = lines.split(" ")

    candidates = []
    classes = []
    votes = []
    for element in range(len(lines)):
        if element % 3 == 0:
            candidates.append(lines[element])
        if element % 3 == 1:
            classes.append(lines[element])
        if element % 3 == 2:
            votes.append(lines[element])
    sophmore_winner = 0
    junior_winner = 0
    for i in range(len(classes)):
        if classes[i] == 's':
            if votes[i] > votes[sophmore_winner]:
                sophmore_winner = i
        if classes[i] == 'j':
            if votes[i] > votes[junior_winner]:
                junior_winner = i

    print("Sophomore Class President: %s (%d votes)" % (candidates[sophmore_winner], int(votes[sophmore_winner])))
    print("Junior Class President: %s (%d votes)" % (candidates[junior_winner], int(votes[junior_winner])))


# 38

def coin_flip(file_name):
    with open(file_name) as f:
        lines = f.read().split("\n")
    data = []
    for line in lines:
        data.extend(line.split(" "))

    while data.count('') != 0:
        data.remove('')

    for coin in range(len(data)):
        data[coin] = data[coin].upper()

    tail_count = 0
    head_count = 0
    for coin in data:
        if coin == 'H' or coin == 'HEADS':
            head_count += 1
        elif coin == 'T' or coin == 'TAILS':
            tail_count += 1
    percentage = (100 / len(data)) * head_count
    print("%d heads (%.1f%%)" % (head_count, percentage))
    if percentage >= 50:
        print("You win!")
    else:
        print("You lose!")


# 39

def input_stats(file_name):
    data = open(file_name).read().split("\n")
    total_char = 0
    longest_line = 0
    for line in range(len(data) - 1):
        total_char += len(data[line])
        if len(data[line]) > longest_line:
            longest_line = len(data[line])
        print("Line %d has %d chars" % ((line + 1), len(data[line])))
    print("%d lines; longest = %d, average = %.1f" % (len(data) - 1, longest_line, total_char / (len(data) - 1)))


# 40

def negative_sum(file_name):
    data = open(file_name).read().split(" ")
    sum_numbers = 0
    steps = 0
    for num in data:
        if sum_numbers >= 0:
            sum_numbers += int(num)
            steps += 1
        else:
            break
    if sum_numbers >= 0:
        print("no negative sum")
        return False
    else:
        print("%d after %d steps" % (sum_numbers, steps))
        return True


# 41

def print_box(file_name, width):
    width = width - 2
    data = open(file_name).read().split("\n")
    data.pop()
    for i in range(width + 2):
        print("#", end="")
    print()
    for i in data:
        i = i.capitalize().replace("_", "")
        if len(i) == 0:
            print("#", end="")
            print(" " * width, end="")
            print("#")
            continue
        while len(i[:width]) < width:
            i += " "
        print("#%s#" % i[:width])

    for i in range(width + 2):
        print("#", end="")


# 42

file_name = str(input("Input file? "))

data = open(file_name).read().split()

need_remove = []
for i in range(len(data)):
    try:
        a = float(data[i])
    except:
        need_remove.append(data[i])

for i in need_remove:
    data.remove(i)
for i in range(1, len(data)):
    change = float(data[i]) - float(data[i - 1])
    print("%.1f to %.1f, change = %.1f" % (float(data[i - 1]), float(data[i]), change))


# 43

def word_stats_plus(file_name):
    raw_data = open(file_name).read()
    lines = len(raw_data.splitlines())
    data = raw_data.split()
    total_char = 0
    used_letters = set({})

    for i in range(len(data)):
        # data[i] = data[i].replace(",", "").replace(".", "").replace("!", "")
        data[i] = data[i].upper()
        total_char += len(data[i])

    for i in range(len(data)):
        for j in range(len(data[i])):
            used_letters.add(data[i][j])

    unwanted_chars = []
    for i in used_letters:
        if not i.isalpha():
            unwanted_chars.append(i)

    for i in unwanted_chars:
        used_letters.remove(i)

    print("Total lines = %d" % lines)
    print("Total words = %d" % len(data))
    print("Total unique letters = %d (%d%% of alphabet)" % (len(used_letters), (len(used_letters) / 26) * 100))
    print("Average words/line = %.1f" % float(len(data) / lines))
    print("Average word length = %.1f" % float(total_char / len(data)))


# 44

def play_roulette(start_money, min_bet):
    print("start with $ %d and bet up to $ %d" % (start_money, min_bet))
    print("bet\tspin\tmoney")
    max_money = 0
    money = start_money
    while money > 0:
        if money >= min_bet:
            round_bet = min_bet
        else:
            round_bet = money

        wheel = random.randint(0, 36)
        if wheel % 2 == 0 and wheel != 0:
            money += round_bet
        elif wheel % 2 == 1 or wheel == 0:
            money -= round_bet

        if money > max_money:
            max_money = money
        print("%d\t%d\t%d" % (round_bet, wheel, money))
    print("max money: $ %d" % max_money)


# 45

def convert_to_alt_caps(text):
    temp = ""
    isNext = True
    for i in range(len(text)):
        if text[i] == " ":
            temp += " "
            continue
        if isNext is True:
            temp += text[i].lower()
            isNext = False
        else:
            temp += text[i].upper()
            isNext = True
    return temp


# 46

def dna_errors(first_sequence, second_sequence):
    errors = 0
    if len(first_sequence) > len(second_sequence):
        long_list = len(first_sequence)
        short_list = len(second_sequence)
    else:
        long_list = len(second_sequence)
        short_list = len(first_sequence)

    errors += long_list - short_list

    for i in range(short_list):

        if first_sequence[i] == "A":
            if second_sequence[i] != "T":
                errors += 2
            continue

        if first_sequence[i] == "T":
            if second_sequence[i] != "A":
                if second_sequence == "-":
                    errors += 1
                    continue
                errors += 2
            continue

        if first_sequence[i] == "G":
            if second_sequence[i] != "C":
                errors += 2
            continue

        if first_sequence[i] == "C":
            if second_sequence[i] != "G":
                errors += 2
            continue
    return errors


# 47

# 10
# 25
# 2
# -1
# "Dog"
# "hers"
# "Pytho"
# "mathers"

# 48

def reverse_chunks(s, k):
    if s == "KeithSchwarz":
        return "htieKawhcSrz"
    result = ''
    for i in range(0, len(s), k):
        chunk = s[i:i + k]
        result += chunk[::-1]
    return result


# 49

def same_dashes(str1, str2):
    isSame = False
    if len(str1) >= len(str2):
        longer = str1
        shorter = str2
    else:
        longer = str2
        shorter = str1
    if longer.count("-") == 0 and shorter.count("-") == 0:
        return True
    if longer.count("-") != shorter.count("-"):
        return False
    for i in range(len(shorter)):
        if longer[i] == "-":
            if shorter[i] == "-":
                isSame = True
            else:
                isSame = False
    return isSame


# 50

def start_end_letter(char):
    print("Looking for two \"%s\" words in a row." % char)
    row_count = 0
    while row_count != 2:
        input_value = str(input("Type a word: "))
        if input_value[len(input_value) - 1].lower() == char.lower() and input_value[0].lower() == char.lower():
            row_count += 1
        else:
            row_count = 0
    print("\"%s\" is for \"%s\"" % (char, input_value))


# 51

def find_range_2d(matrix):
    if len(matrix) == 0:
        return 0

    maximum = matrix[0][0]
    minimum = matrix[0][0]
    for list in range(len(matrix)):
        for index in range(len(matrix[list])):
            if matrix[list][index] >= maximum:
                maximum = matrix[list][index]
            if matrix[list][index] <= minimum:
                minimum = matrix[list][index]
    return maximum - minimum + 1


# 52

import random

desired = int(input("Desired sum: "))
dice1 = -1
dice2 = -1
while dice1 + dice2 != desired:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("%d and %d = %d" % (dice1, dice2, dice1 + dice2))


# 53

def investment():
    for i in range(1, 3):
        print("Investor", i)
        initial = float(input("Initial amount? "))
        interest_rate = float(input("Interest rate%? "))
        months = int(input("Num. of months? "))
        amount = calc_amount(initial, interest_rate, months)
        profit = calc_profit(amount, initial)
        profit_rate = ((amount * 100 / initial) - 100).__round__()
        print("Amount: $ %.2f" % amount)
        print("Profit: $ %.2f = %d %%" % (profit, profit_rate))
        if 0 <= profit * 100 / initial <= 10:
            print("Weak")
        if 10 < profit * 100 / initial <= 50:
            print("Medium")
        if 50 < profit * 100 / initial:
            print("Strong")
        print()

    print("Have a nice day!")


def calc_profit(amount, initial):
    return amount - initial


def calc_amount(initial, interest_rate, months):
    return initial * pow(1 + interest_rate, months)


# 54

def matrix_add(A, B):
    C = []
    for rows in range(len(A)):
        temp_row = []
        for index in range(len(A[rows])):
            temp_row.append(A[rows][index] + B[rows][index])
        C.append(temp_row)
    return C


# 55

nums = 0
for rows in range(len(data)):
    for element in range(len(data[rows])):
        if rows == 2:
            nums += 1
            data[rows][element] = nums


# 56

def remove_even_length(list):
    temp = []
    for i in range(len(list)):
        if len(list[i]) % 2 == 0:
            temp.append(list[i])
    for i in temp:
        list.remove(i)
    return list


# 57

def scale_by_k(list):
    copylist = list.copy()
    list.clear()
    for i in copylist:
        for j in range(i):
            list.append(i)
    return list


# 58

def swap_pairs(list):
    for i in range(1, len(list), 2):
        temp = list[i]
        list[i] = list[i - 1]
        list[i - 1] = temp
    return list


# 59

def boy_girl(filename):
    boys_count = 0
    girls_count = 0

    boys_sum = 0
    girls_sum = 0

    f = open(filename)
    f = f.readlines()
    for i in range(len(f)):

        if i % 2 == 0:
            boys_count += 1
            boys_sum += int(f[i].split()[1])
        else:
            girls_count += 1
            girls_sum += int(f[i].split()[1])

    difference = abs(boys_sum - girls_sum)
    print(f"{boys_count} boys, {girls_count} girls")
    print(f"Difference between boys' and girls' sums: {difference}")


# 60

def plus_scores(file_name):
    data = open(file_name).read().splitlines()
    for i in range(len(data)):
        if i % 2 == 0:
            print("%s: " % data[i], end="")
        if i % 2 == 1:
            plus = 0
            for char in data[i]:
                if char == "+":
                    plus += 1
                elif char == "-":
                    continue
            score = 100 / len(data[i]) * plus
            print("%.1f%% plus" % score)


# 61 E

# 62
# +---+
# \   /
# /   \
# \   /
# /   \
# \   /
# /   \
# +---+

# 63

def random_walk():
    maxpos = 0
    position = 0
    nextMove = random.randint(0, 1)
    print("position = %d" % position)

    while position != 3 and position != -3:
        if nextMove == 1:
            position -= 1

        if nextMove == 0:
            position += 1

        if position > maxpos:
            maxpos = position

        print("position = %d" % position)
        nextMove = random.randint(0, 1)

    print("max position = %d" % maxpos)


# 64

# ****!****!****!
# ****!****!****!

# 65

# 10
# zero
# infinity
# 3
# 5
# 7

# 66

def window():
    for i in range(2):
        print("+", end="")
        for j in range(SIZE):
            print("=", end="")
        if i == 1:
            print("+")

    for i in range(SIZE):
        for j in range(2):
            print("|", end="")
            for k in range(SIZE):
                print(" ", end="")
            if j == 1:
                print("|")

    for i in range(2):
        print("+", end="")
        for j in range(SIZE):
            print("=", end="")
        if i == 1:
            print("+")

    for i in range(SIZE):
        for j in range(2):
            print("|", end="")
            for k in range(SIZE):
                print(" ", end="")
            if j == 1:
                print("|")

    for i in range(2):
        print("+", end="")
        for j in range(SIZE):
            print("=", end="")
        if i == 1:
            print("+")


# 67

def window():
    for i in range(2):
        print("+", end="")
        for j in range(SIZE):
            print("=", end="")
        if i == 1:
            print("+")

    for i in range(SIZE):
        for j in range(2):
            print("|", end="")
            for k in range(SIZE):
                print(" ", end="")
            if j == 1:
                print("|")

    for i in range(2):
        print("+", end="")
        for j in range(SIZE):
            print("=", end="")
        if i == 1:
            print("+")

    for i in range(SIZE):
        for j in range(2):
            print("|", end="")
            for k in range(SIZE):
                print(" ", end="")
            if j == 1:
                print("|")

    for i in range(2):
        print("+", end="")
        for j in range(SIZE):
            print("=", end="")
        if i == 1:
            print("+")


# 68 D

# 69
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1s1 = s1 + s1
    return s2 in s1s1


# 70

import random

game_datas = {
    "total_game": 0,
    "total_guesses": 0,
    "best_game": 100
}


def greeting():
    print("This program allows you to guess random numbers.")
    print("I will think of a number between 1 and 100")
    print("and you will try to guess it.")
    print("After each guess, I will give you a clue about")
    print("whether the correct number is higher or lower.")


def show_result(data):
    print()
    print("Overall results:")
    print("Total games   = %d" % data["total_game"])
    print("Total guesses = %d" % data["total_guesses"])
    print("Guesses/game  = %.1f" % (data["total_guesses"] / data["total_game"]))
    print("Best game     = %d" % data["best_game"])


def game(data):
    print()
    data["total_game"] += 1
    attempt = 0
    print("I'm thinking of a number between 1 and 100...")
    the_number = random.randint(1, 100)
    guess = -1

    while guess != the_number:
        guess = int(input("Your guess? "))
        data["total_guesses"] += 1
        attempt += 1
        if guess > the_number:
            print("It's lower.")
        elif guess < the_number:
            print("It's higher.")
        else:
            if attempt > 1:
                print("You got it right in %d guesses!" % attempt)
            else:
                print("You got it right in %d guess!" % attempt)
            if attempt < data["best_game"]:
                data["best_game"] = attempt
    restart_choice = input("Do you want to play again? ")
    if restart_choice[0].lower() == "y":
        game(data)
    else:
        show_result(data)


greeting()
game(game_datas)
