
def is_all_vowels(s):
    list=[]
    count=0
    for i in s:
        list.append(str(i))
    vowels=["a", "e", "i", "o", "u","A","E","I","O","U"," "]
    
    for i in list:
        for j in vowels:
            if i==j:
                count=count+1

    if count==len(s):
        return True
    else:
        return False




def main():
    s="oink"
    print(is_all_vowels(s))
main()  