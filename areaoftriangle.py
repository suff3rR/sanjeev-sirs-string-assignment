def main():    
    while True:    
        h = input("Enter height of the triangle: ")
        b = input("Enter base of the triangle: ")
        if(h.isdigit() and b.isdigit()) :
            h = float(h)
            b = float(b)
            area = (0.5) * h * b
            print(f"The area of the triangle is : {area}")
            break
        else :
            print("Please enter a valid height and base.")

main()

