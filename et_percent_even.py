def get_percent_even(a):
    ev_count=0.0
    for i in a:
        if i%2==0:
            ev_count+=1.0
    if ev_count>0:
        return (ev_count/len(a))*100
    else:
        return 0.0



def main():
    a=[6, 4, 9, 11, 5]
    print(get_percent_even(a))
main()