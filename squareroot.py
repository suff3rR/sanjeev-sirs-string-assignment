#solution 1
while True:
    num = input("Enter a number : ")
    if(num.isdigit()):
        num = int(num)
        sr  = num **(1/2)
        print(f"The square root of {num} is {sr}")
        break
    else : 
        print("Please Enter a numeric digit. ")
