# Python code to calculate the factorial of a number 

#Another comment added in frontend branch
#Another comment added Done In main branch
#Another comment added Done in feature branch
#Latest comment in frontend branch
def calculate_factorial(number): 
    if number == 0 or number == 1: 
        return 1
    else: 
        return number * calculate_factorial(number - 1) 
  
# Prompt the user for a number 
user_number = int(input("Enter a non-negative integer: ")) 
  
# Check if the user entered a non-negative integer 
if user_number >= 0: 
    # Calculate the factorial using the function 
    result = calculate_factorial(user_number) 
  
    # Display the result 
    print(f"The factorial of {user_number} is: {result}") 
else: 
    # Handle the case where the user didn't enter a non-negative integer 
    print("Invalid input. Please enter a non-negative integer.") 

