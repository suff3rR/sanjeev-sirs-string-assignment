if __name__ == "__main__" :
    while True:
        num = input("Please enter a numeric digit.")
        if (num.count("-") <=1 and num.count(".") <=1 ) and (num[0]=='-' or num[0].isdigit()) and num.replace("-", "",1).replace(".", "",1).isdigit()   : 
            num = float(num)
            if (num>0):
                    print(f"{num} is positive.")
            elif(num==0):
                    print(f"0 is neither positive nor negative")
            else: 
                    print(f"{num} is negative")
        else: 
                print(f"{num} is not a real number") 
