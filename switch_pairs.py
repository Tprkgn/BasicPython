def switch_pairs(example):
    newword=""
    for x in example:
        newword = newword + x
        
    return newword
example = "hello there"
print(switch_pairs(example))

