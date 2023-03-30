# Imports
from debug import debug

# This function gets input from the user.
# 

# userInput function:
def userInput(question="You: ", dataType="str", case="mixed"):
    # Keywords
    yes=("yes" or "y")
    no=("no" or "n")
    lower=("lower" or "lower case" or "lowercase")
    upper=("upper" or  "upper case" or "uppercase" or "higher" or "higher case" or "highercase")
    mixed=("mixed" or "mixed case" or "mixedcase")
    case=(lower or upper or mixed)
    stringType=("str" or "string")
    integerType=("int" or "str")
    decimalType=("dec" or "decimal")
    booleanType=("bool" or "boolean")
    types=(stringType or integerType or decimalType or booleanType)

    if dataType==stringType:
        answer: str=input(question)
        if case==lower:
            return answer.lower()
        elif case==upper:
            return answer.upper()
        elif case==mixed:
            return answer
        else:
            debug("Not lower, upper or mixed case.", "The Script did not use a correct case. ")
            return
    elif dataType==integerType:
        while True:
            try:
                answer: int=int(input(question))
                break
            except:
                print("Invalid answer. Please answer again.")
                continue
    elif dataType==decimalType:
        pass
    elif dataType==booleanType:
        while True:
            answer: str=input(question, "Respond with [y] for yes, or [n] for no.")
            if answer.lower()==yes:
                return True
            elif answer.lower==no:
                return False
            else:
                print("Invalid answer. Please answer again.")
                continue
    else:
        debug("Not a data type.", "The Script used an incorrect data type.")
        return
