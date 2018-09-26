print ("This is a program that applies collatz conjecture on every integer you enter")
print ("Hello there! Can you please enter your name?")
user = input ()
print ("Welcome!",user)
while True:
    def collatz(number): # a function is defined with "number" as the single parameter
        if number % 2 == 0: # a condition for an even number integer
            print (number // 2) # the number is divided by 2 and result is displayed
            return number // 2

        elif number % 2 == 1: # a condition for an odd number integer
            result = 3 * number + 1 # the equation is applied to the number and diplays result
            print (result)
            return result
    try: # a try clause is created to handle ValueError
            
        print ("Enter any positive integer of your choice")
        value = int (input ()) # asks user to input a number

        if value < 0: # checks for negative if a value was entered 
            print ("Sorry,",user,", the collatz conjecture only deals with positive integers")
            break # program ends
                    
        while value != 1: """ if number entered is positive then the program
                            checks if it is 1 and continues to apply
                            the collatze conjecture until the "1" is gotten,
                            then the program ends"""
        value = collatz (value)

        
    except ValueError:
        print ("Please enter a valid integer")

    close = input ("\nWould you like to exit?\n 1.Yes\t 2. No\n Choice:")
    if close == "2": # conditions for quitting the program
        continue
    
    elif close == "1":
        print ("Thank you for your time,",user,", do have a nice day")
        break
