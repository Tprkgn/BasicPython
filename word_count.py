def word_count(word):
    count = 0
    list = word.split()
    for x in list:
        count += 1
    return count
word = "bu beş harfli bir cümledir."
print(word_count(word))