def swap(a,b):
    temp = a
    a = b
    b = temp
    
if __name__ == "__main__" :
    x = 5
    y = 10
    print("Before swap:")
    print(f"x = {x} , y = {y}")
    x,y = y,x
    #we are adding this line to branch1 on github
    print("After swap:")
    print(f"x = {x} , y = {y}")


