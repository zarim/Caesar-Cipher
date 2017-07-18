#Zari McFadden = 1/27/17
#P1216 - Caesar Cipher
#Write a program that prompts a user for a string and an encryption key.
#The encryption key is the cipher shift amount.  Your program will function as
#both an Caesar Cipher encrypter and decrypter.


def main():                                         #define main
    A = []                                          #create an empty list for A
    A1 = []                                         #create an empty list for A1
    S = []
    
    for letter in range(65, 91):                    #append the letters to A
        A.append(chr(letter))

    e = int(input("Enter an encryption key: "))     #user enters encryption key

    s = input("Enter a string: ")                   #user enters a string
    s1 = s.upper()                                  #uppercase letters in string
    
    if e < 0:                                       #if encryption key is neg                        
        for i in range(e, len(A)+e):                #shift alphabet down
            A1.append(A[i])
            
        print(A1)                                   #print shifted alphabet

        A = ''.join(A)                              #turn A into a string
        
        for char in s1:                             #search char in string
            if char in A:                           #if char in A
                y = A.find(char)                    #find index of char in A
                S.append(A1[y])                     #append new letter to S

            else:
                S.append(char)                      #append spaces/ other char

            s2 = ''.join(S)                         #turn S into a string

        
    else:
        
        for i in range(e, len(A)):                  #if encrytion key is positive
            A1.append(A[i])                         #shift alphabet up
        for x in range(e):
            A1.append(A[x])

        print(A1)

        A = ''.join(A)                              #turn A into a string

        for char in s1:                             #search char in string
            if char in A:                           #if char in A
                y = A.find(char)                    #find index of char in A
                S.append(A1[y])                     #append new letter to S

            else:
                S.append(char)                      #append spaces/ other char

            s2 = ''.join(S)                         #turn S into a string

    print(s2)                                       #print new string


main()                                              #call main


