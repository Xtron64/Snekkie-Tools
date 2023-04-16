# userInput() documentation:
## How to use userInput()
Call the userInput function where you would've called the input function instead. This function has three parameters: question, dataType and case. 
#### question
The question parameter is printed to the CLI before the user is asked to give input. As the name implies, the value of this parameter should be the question that you are asking the user, given as a string. Don't use the print function to ask the question as the userInput function will do that for you.
#### dataType
This parameter is used to evaluate what type the user's input should be returned as. If you want the user's input to be returned as a string, set the value of dataType to "str" or "string". If you want the user's input to be returned as an integer, set dataType to "int" or "integer". If you want the user's input to be returned as a decimal, set dataType to "dec" or "decimal". If you would like the user's input to be returned as a float, set dataType to "float". If you would like the user's input to be returned as a boolean, then set dataType to "bool" or "boolean".
#### case
This parameter is only used if you set dataType to "str" or "string". As the name implies, this parameter evaluates what case the user's input should be returned in. If you would like the user's input to be returned in lowercase, set case to "low", "lower" or "lowercase" or "lower case". If you would like the user's input to be returned in uppercase, set case to "up", "upper", "uppercase" or "upper case". If you would like the user's input to be returned in titlecase, set case to "title", "titlecase" or "title case". If you want the user's input to be returned exactly how they inputted it, then keep case set to None.
## How userInput() works
If you would like to know how the userInput function works, then we recommend looking at the code yourself, it is written in Python, which is a very readable langauge with clear syntax, and every line has comments which explain what those lines do, or they rephrase what those lines mean to be more readable for humans.
## Variations of userInput()
The userInput function has many variations based off of what type the user's input is returned as. There are 5 variations of userInput: strUserInput, intUserInput, decUserInput, floatUserInput and boolUserInput.
#### strUserInput
As the name implies, the strUserInput function returns the user's input as a string. It has two parameters: question and case. 