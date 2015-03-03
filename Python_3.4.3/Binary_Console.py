#Program that displays a range of numbers in Binary.
#Created by Tony Dougal

#-=-=-=-= Variables =-=-=-=-
intx = 0                                                                            #variable converted into binary
count = 1                                                                           #variable used to number binary lists
prompt = ""                                                                         #variable used to answer the prompt
rangecap = 0                                                                        #variable used to end the output of binary #'s
rangelow = 0                                                                        #variable used to begin the output of binary #'s
binary = 0                                                                          #variable converted into an integer value
#-=-=-=-=-=-=-=-=-=-=-=-=-=-

while True:                                                                         #loop until break
    print("")                                                                       #spacing
    print("1: Convert a single integer to binary.")                                 #Prompt to input string (prompt)
    print("2: Convert a single strand of binary to its integer value.")             #
    print("3: Convert a range of integers to binary.")                              #
    print("4: Exit the program.")                                                   #
    prompt = input(str(": "))                                                       #input string (prompt)

    if prompt == "1":                                                               #if string (prompt) = "1"
        print("")                                                                   #spaceing 
        print("Please enter an integer.")                                           #prompt to enter integer (intx)
        intx = int(input(": "))                                                     #input integer (intx)
        binary = int(bin(intx)[2: ])                                                #integer (binary) = the binary # for integer (intx)
        print("")                                                                   #spacing
        print(binary)                                                               #display integer (binary)
        print("")                                                                   #spacing
        input("Press ENTER to continue")                                            #pause                                                                   
        
    elif prompt == "2":                                                             #if string (prompt) = "2"
        print("")                                                                   #spacing
        print("Please enter a strand of binary.")                                   #prompt to enter integer (binary)
        binary = input(": ")                                                        #input integer (binary)
        intx = 0                                                                    #redeclare integer (intx) 
        for digit in binary:                                                        #for each digit in integer (binary)
            intx = intx * 2 + int(digit)                                            #
        print("")                                                                   #spacing
        print(intx)                                                                 #display integer (intx)
        print("")                                                                   #spacing
        input("Press ENTER to continue.")                                           #pause 
        
    elif prompt == "3":                                                             #if string (prompt) = "3"
        print("")                                                                   #spacing
        print("Enter your low range.")                                              #prompt to enter integer (rangelow)
        rangelow = int(input(": "))                                                 #input integer (rangelow)
        count = rangelow                                                            #count = rangelow
        print("")                                                                   #spacing
        print("Enter your high range.")                                             #prompt to enter integer (rangecap)
        rangecap = int(input(": "))                                                 #input integer (rangecap)
        while True:                                                                 #loop until break                   
            if rangelow > rangecap:                                                 #if int (rangelow) is greater than int (rangecap)
                print("")                                                           #spacing
                input("Press ENTER to continue.")                                   #pause                
                break                                                               #break             
            else:                                                                   #else
                binary = int(bin(rangelow)[2: ])                                    #integer (binary) = the binary value of int (rangelow)
                print(count, " - ", binary)                                         #print int (count) and int (binary) 
                rangelow += 1                                                       #add 1 to int (rangelow)    
                count += 1                                                          #add 1 to int (count)
                
    elif prompt == "4":                                                             #if string (prompt) = "4"
        break                                                                       #end the loop
                           
    else:                                                                           #if string (prompt)
        print("")                                                                   #spacing
        print("Error 1: Please enter an integer 1, 2, or 3")                        #display error message
