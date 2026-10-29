print("=" * 40)
print(" RAIL FENCE CIPHER")
print("=" * 40)
print("1. Encryption")
print("2. Decryption")
choice = int(input("\nEnter your choice (1 or 2): "))


if choice == 1:
    plain_text = input("\nEnter the Plain Text: ")
    Key = int(input("Enter the key: "))
    
   
    if Key <= 1 or Key > len(plain_text):
        print("Invalid Key!")
        exit()
        
    
    rail_matrix = [["" for i in range(len(plain_text))] for j in range(Key)]
    
    row = 0
    moving_down = True
    
    for column in range(len(plain_text)):
        rail_matrix[row][column] = plain_text[column]
        if row == 0:
            moving_down = True
        elif row == Key - 1:
            moving_down = False
            
        if moving_down:
            row += 1
        else:
            row -= 1
            
    print("\nRail Fence Pattern\n")
    
    for rail in rail_matrix:
        print("".join(rail))
        
    Cipher_text = ""
    for i in range(Key):
        for j in range(len(plain_text)):
            if rail_matrix[i][j] != "":
                Cipher_text += rail_matrix[i][j]
                
    print("\nCipher Text:", Cipher_text)


elif choice == 2:
    Cipher_text = input("\nEnter the Cipher Text: ")
    Key = int(input("Enter the key: "))
    
    if Key <= 1 or Key > len(Cipher_text):
        print("Invalid Key!")
        exit()
        
    rail_matrix = [["" for i in range(len(Cipher_text))] for j in range(Key)]
    
    row = 0
    moving_down = True
    
    for column in range(len(Cipher_text)):
        rail_matrix[row][column] = "*"
        
        if row == 0:
            moving_down = True
        elif row == Key - 1:
            moving_down = False
            
        if moving_down:
            row += 1
        else:
            row -= 1
            
    index = 0
    for i in range(Key):
        for j in range(len(Cipher_text)):
            if rail_matrix[i][j] == "*":
                rail_matrix[i][j] = Cipher_text[index]
                index += 1
                
    print("\nRail Fence Pattern\n")
    
    for rail in rail_matrix:
        print("".join(rail))
        
    row = 0
    moving_down = True
    plain_text = ""
    
    for column in range(len(Cipher_text)):
        plain_text += rail_matrix[row][column]
        
        if row == 0:
            moving_down = True
        elif row == Key - 1:
            moving_down = False
            
        if moving_down:
            row += 1
        else:
            row -= 1
            
    print("\nPlain Text:", plain_text)

else:
    print("Invalid choice! Please Select either 1 or 2")
