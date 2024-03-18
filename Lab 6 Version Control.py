def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")
    user_inp = int(input("Please enter an option: "))
    return user_inp

def encode(pw):
    new = []
    for i in pw:
        i = int(i) + 3
        new.append(str(i))
    encoded = ''.join(new)
    return encoded

def main():
    while True:
        menu_sel = menu()
        if menu_sel == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!\n")
        
        

if __name__ == "__main__":
    main()
    
    
