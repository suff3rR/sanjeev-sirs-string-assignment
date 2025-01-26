    
    
if __name__ == "__main__" :
    print("This program will convert Kilometres to miles.")
    while True:
        km = (input("Enter a distance in Kilometres: "))
        if km.isdigit() :
            km = float(km) 
            miles = 0.621371 * km
            print(f"In Kilometres: {km} km")
            print(f"In Miles: {miles} ml")
            break
        else :
            print("Please enter a valid distance")
