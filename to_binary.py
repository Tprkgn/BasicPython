def to_binary(number):
    list=[]
    isfinish=True
    divr=number
    txt =""
    while isfinish:
        list.append(divr%2)
        divr = int(divr/2)
        if divr<1:
            break
    for i in range(len(list)-1,-1,-1):
        txt = txt+str(list[i])
    return txt

def main():
    number= 199
    print(to_binary(number))
main()
