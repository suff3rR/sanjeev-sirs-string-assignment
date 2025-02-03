## Q1: Remove the 2nd letter of string 
if __name__ == "__main__" :
    s = input("Enter something: ")
    for x in range(0,len(s)):
        if x == 2 :
            continue
        print(s[x], end='')