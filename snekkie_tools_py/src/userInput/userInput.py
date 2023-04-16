# IMPORTS
from decimal import Decimal

# DOCUMENTATION
# strUserInput() function:
# This function gets input from the user in the form of a string.
# 
# It has two parameters:
# - question
# This parameter is printed to the CLI before the function asks the user
# for input. If you have already printed the question you are asking then
# you don't need to use this parameter.
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
#
# intUserInput() function:
# This function get 
#
#
# decUserInput() function:
# This function get input from the user in the form of a decimal.
# This function has one parameter:
# - question
# This parameter is printed to the CLI before the function asks the user
# for input. If you have already printed the question you are asking then
# you don't need to use this parameter.
#
#
# floatUserInput() function:
# This function get input from the user in the form of a float.
#
# This function has one parameter:
# - question
# This parameter is printed to the CLI before the function asks the user
# for input. If you have already printed the question you are asking then
# you don't need to use this parameter.
#

# boolUserInput() function:
#
# userInput() function:
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

# KEYWORDS
# Data type keywords:
str_kw = ("str" or "string")  # This constant defines the keywords for strings
int_kw = ("int" or "integer")  # This constant defines the keywords for integers
dec_kw = ("dec" or "decimal")  # This constant defines the keywords for decimals
float_kw = ("float")  # This constant defines the keywords for floats
bool_kw = ("bool" or "boolean")  # This constant defines the keywords for booleans
# Case keywords:
low_kw = ("low" or "lower" or "lowercase" or "lower case")  # This constant defines the keywords for lowercase strings
up_kw = ("up" or "upper" or "uppercase" or "upper case")  # This constant defines the keywords for uppercase strings
title_kw = ("title" or "titlecase" or "title case")  # This constant defines the keywords for titlecase strings
# Boolean Keywords:
yes_kw = ("y" or "yes")  # This constant defines the keywords for 'yes'
no_kw = ("n" or "no")  # This consatnt defines the keywords for 'no'


def strUserInput(question=None, case=None):
    global low_kw, up_kw, title_kw  # We need these later
    while True:  # Starts a loop
        try:  # Tries to get the user to input a valid string:
            if question:  # If the question parameter has a value:
                print(question)  # Output the value of the question parameter
            answer = input("You: ")  # Asks the user for a valid string
        except UnicodeError:  # Handle unicode error:
            print("There was a unicode error. Please try again.")  # Tells user what's wrong
            continue  # Restarts the loop
        except:  # If another error occured
            print("Something went wrong. Please try again.")  # Tells the user that an error has occured
            continue  # Restarts the loop
        finally:  # After all errors from trying to get the user's input have been handled:
            if case:  # If the case parameter has a value:
                if case == low_kw:  # If the user's response should be lowercase:
                    return answer.lower()  # returns the user's response in lowercase
                elif case == up_kw:  # If the user's response should be uppercase:
                    return answer.upper()  # Returns the user's response in uppercase
                elif case == title_kw:  # If the user's response should be in titlecase:
                    return answer.title()  # Returns the user's response in titlecase
                else:  # If the case parameter has an invalid value:
                    raise SyntaxError("Case parameter has an invalid value")  # Raises an error about it
            else:  # If the case parameter is empty
                return answer  # Returns the user's response exactly how they wrote it


def intUserInput(question=None):
    while True:  # Starts a loop
        try:  # Tries to get the user to input a valid integer
            if question:  # If the question parameter has a value:
                print(question)  # Prints the value of the question parameter
            answer = int(input("You: "))  # Asks the user to input a valid ineteger
        except TypeError:  # Handle type error:
            print("Please input an integer.")  # Tells the user to input an integer
            continue  # Restarts the loop
        except UnicodeError:  # Handles unicode error:
            print("There was a unicode error. Please try again.")  # Tells the user what happened
            continue  # Restarts the loop
        except:  # If another error occured:
            print("Something went wrong. Please try again.")  # Tells the user that an error occured
            continue  # Restarts the loop
        finally:  # After all errors have been handled:
            return answer  # returns the user's response


def decUserInput(question=None):
    while True:  # Starts a loop
        try:  # Tries to get the user to input a valid decimal
            if question:  # If the question parameter has a value:
                print(question)  # Outputs the value of the question parameter
            answer = Decimal(input("You: "))  # Asks the user to input a valid decimal
        except TypeError:  # Handles type error:
            print("Please input a decimal.")  # Tells the user to input a valid decimal
            continue  # Restarts the loop
        except UnicodeError:  # Handles unicode error:
            print("There was a unicode error. Please try again.")  # Tells the user what happened
            continue  # Restarts the loop
        except:  # If any other error happened:
            print("Something went wrong. Please try again.")  # Tells the user that an error occured
            continue  # Restarts the loop
        finally:  # After all errors have hopefully been solved
            return answer  # Returns the user's response


def floatUserInput(question=None):
    while True:  # Starts a loop
        try:  # Tries to get the user to input a float:
            if question:  # If  the question parameter has a value
                print(question)  # Outputs the value of the question parameter
            answer = float(input("You: "))  # Asks the user to input a valid float
        except TypeError:  # Handles type error:
            print("Please input a float.")  # Tells the user that they need to input a valid float
            continue  # Restarts the loop
        except UnicodeError:  # Handles unicode error:
            print("There was a unicode error. Please try again.")  # Tells the user what happened
            continue  # Restarts the loop
        except:  # Handles other errors:
            print("Something went wrong. Please try again.")  # Tells the user that an error occured
            continue  # Restarts the loop
        finally:  # After all errors have hopefully been handled:
            return answer  # Returns the user's response


def boolUserInput(question=None):
    global yes_kw, no_kwm  # We need these
    while True:  # Starts a loop
        try:  # Tries to ask the user to input a valid boolean
            if question:  # If the question parameter has a value:
                print(question)  # Outputs the value of the question parameter
            answer = input("Input yes or no: ")  # Asks the user to input  yes or no
        except UnicodeError:  # Handles unicode error:
            print("There was a unicode error. Please try again.")  # Tells the user what happened
            continue  # Restarts the loop
        except:  # Handles other errors:
            print("Something went wrong")  # Tells the user that an error occured
            continue  # Restarts the loop
        finally:  # After all (but one error that will be handled later) have been handled:
            if answer == yes_kw:  # If the user has inputted yes:
                return True  # Returns true
            elif answer == no_kw:  # If the user has inputted no:
                return False  # Returns false
            else:  # If the user inputted something other than yes or no:
                print("Invalid answer. Please try again.")  # Tells the user that they haven't responded properly
                continue  # Restarts the loop


def userInput(question=None, dataType=None, case=None):
    global str_kw, int_kw, dec_kw, float_kw, bool_kw  # We need these
    if dataType == str_kw:  # If the user's answer is meant to be returned as a string:
        answer = strUserInput(question, case)  # Gets the user to input a valid string
        return answer  # Returns the user's response
    elif dataType == int_kw:  # If the user's answer is meant to be returned as an integer:
        answer = intUserInput(question)  # Gets the user to input a valid integer
        return answer  # Returns the user's response
    elif dataType == dec_kw:  # if the user's response is meant to be returned as a decimal:
        answer = decUserInput(question)  # Gets the user to input a valid decimal
        return answer  # Returns the user's response
    elif dataType == float_kw:  # If the user's response is meant to be returned as a float:
        answer = floatUserInput(question)  # Gets the user to input a valid float
        return answer  # Returns the user's response
    elif dataType == bool_kw:  # If the user's response is meant to be returned as a boolean
        answer = boolUserInput(question)  # Gets the user to input a boolean value
        return answer  # Returns the boolean value that the user has inputted
    elif dataType == None:  # If the dataType parameter doesn't have a value
        answer == strUserInput(question)  # Gets the user to input a valid string
        return answer  # Returns the user's response
    else:  # If the dataType function has an invalid value:
        raise SyntaxError("Parameter dataType has an invalid value")  # Raises an error about it
