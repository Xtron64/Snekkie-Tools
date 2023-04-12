# IMPORTS
import decimal

# DOCUMENTATION
# This function gets input from the user.
#
# It has three parameters:
# - question
# This parameter is printed to the CLI before the function asks the user
# for input. If you have already printed the question you are asking then 
# you don't need to use this parameter.
#
# - dataType
# This parameter defines what type the user's input will be returned as.
# By default it is set to None, but this function will return the user's 
# input as a string, as that is the default type that Python uses.
# You can still set dataType to "str" or "string" if you prefer explicit 
# code over implicit code. If you want the user's input to be returned 
# as an integer instead, then set dataType to "int" or "integer". 
# If you want the user's input to be returned as a decimal, then set
# dataType to "dec" or "decimal". If you would like the user's input
# to be returned as a float then set datType to "float". If you would 
# like the user's input as a boolean, then set dataType to "bool" or
# "boolean".
#
# - case
# This parameter defines what case the answer will be returned as, assuming
# that the dataType parameter is set to "str" or "string". If the answer
# is being returned as a string, but this parameter is empty (case=None),
# then the answer will be returned exactly how the user wrote it. If you
# want the user's answer to be returned in lowercase set case to "low" or
# "lower" or "lowercase" or "lower case". If you would like the user's answer
# to be returned as uppercase then set case to "up" or "upper" or "uppercase"
# or "upper case". If you would like the user's answer to be returned as 
# titlecase, then set case to "title" or "titlecase" or "title case". This
# parameter should only be used if you want the user's response to be returned
# as a string, or else it will be useless.

def userInput(question=None, dataType=None, case=None):
    # KEYWORDS
    # Data type keywords:
    str_kw=("str" or "string") # This constant defines the keywords for strings
    int_kw=("int" or "integer") # This constant defines the keywords for integers
    dec_kw=("dec" or "decimal") # This constant defines the keywords for decimals
    float_kw=("float") # This constant defines the keywords for floats
    bool_kw=("bool" or "boolean") # This constant defines the keywords for booleans
    # Case keywords:
    low_kw=("low" or "lower" or "lowercase" or "lower case") # This constant defines the keywords for lowercase strings
    up_kw=("up" or "upper" or "uppercase" or "upper case") # This constant defines the keywords for uppercase strings
    title_kw=("title" or "titlecase" or "title case") # This constant defines the keywords for titlecase strings
    # Boolean Keywords:
    yes_kw=("y" or "yes") # This constant defines the keywords for 'yes'
    no_kw=("n" or "no") # This consatnt defines the keywords for 'no'
    # NOT KEYWORDS ANYMORE
    if question: # Checks if the question parameter has a value
        print(question) # Prints the value of the question parameter
    if datatype: # Checks if the dataType parameter has a value
        if dataType==str_kw: # If the type is meant to be a string: 
            while True: # Starts a loop
                try: # Tries to get a valid string from the user
                    answer=input("You: ") # Asks them for the valid string
                    break # Breaks if successful
                except: # In case the user hasn't inputted a valid string
                    print("You have inputted an invalid string.") # Tells them to input a valid string
                    continue # Continues the loop to get them to input a valid string
                if case: # Checks if the case parameter has a value
                    if case==low_kw: # If the case is meant to be lowercase:
                        return answer.lower() # Then it returns the answer in lowercase
                    elif case==up_kw: # If the case is meant to be uppercase:
                        return answer.upper() # Then it returns the answer in uppercase
                    elif case==title_kw: # If the case is meant to be titlecase:
                        return answer.title() # Then it returns the answer in titlecase
                else: # If the case parameter doesn't have a value:
                    return answer # Returns the answer exactly how the user inputted it
        elif dataType==int_kw: # If the type is meant to be an integer:
            while True: # Starts a loop
                try: # Tries to get the user to input a valid integer:
                    answer=int(input("You: ")) # Asks the user to input a valid integer
                    break # Breaks the loop if successful
                except: # If unsuccessful:
                    print("You haven't inputted a valid integer.") # Tells the user that they have't inputted a valid integer
                    continue # Continues the loop
                return answer # Returns the user's answer (as an integer)
        elif dataType==dec_kw: # If the type is meant to be a decimal:
            while True: # Starts a loop
                try: # Tries to get a valid decimal from the user:
                    answer=Decimal(input("You: ")) # Asks the user for a valid decimal
                    break # Breaks the loop if successful
                except: # If unsuccessful:
                    print("You haven't inputted a valid decimal.") # Tells the user that they haven't inputted a valid decimal
                    continue # Continues the loop
                return answer # Returns the user's answer (as a decimal)
        elif dataType==float_kw: # If the type is meant to be a float:
            while True: # Starts a loop
                try: # Tries to get the user to input a valid float:
                    answer=float(input("You: ")) # Asks the user to input a valid float
                    break # Breaks the loop if successful
                except: # If unsuccessful:
                    print("You haven't inputted a valid float.") # Tells the user that they haven't inputted a valid float
                    continue # Continues the loop
                return answer # Returns the user's answer (as a float)
        elif dataType==bool_kw: # If the type is meant to be a boolean:
            while True: # Starts a loop
                try: # Tries to get the user to input a valid float:
                    answer=input("Input [Y/y] for yes, or input [N/n(] for no: ") # Asks the user to input either y (yes) or n (no)
                    if answer==yes_kw: # If the user's answer is yes:
                        return True # Returns True
                    elif answer==no_kw: # If the user's answer is no:
                        return False # Returns False
                    else: # If the user's answer is neither yes or no:
                        print("You haven't inputted a valid answer.") # Tells them to input a valid answer
                        continue # Continues the loop
                except: # If the user didn't input a valid string:
                    print("You haven't inputted a valid answer.") # Tells them to input a valid string
                    continue # Continues the loop
    else: # If the dataType parameter is empty (None):
        while True: # Starts a loop
            try: # Tries to get the user to input a valid string:
                answer=input("You: ") # Asks the user for a valid string
                break # Breaks the loop if successful
            except: # If unsuccessful:
                print("You have inputted an invalid string.") # tells the user to input a valid string
                continue # Continues the loop
            if case: # If the case parameter has a value:
                if case==low_kw: # If the case is meant to be lowercase:
                    return answer.lower() # returns the user's answer in lowercase
                elif case==up_kw: # If the case is meant to be uppercase:
                    return answer.upper() # Returns the user's answer in uppercase
                elif case==title_kw: # If the case is meant to be in titlecase:
                    return answer.title() # Returns the user's answer in titlecase
            else: # If the case parameter is empty (None):
                return answer # returns the answer exactly how the user inputted it


