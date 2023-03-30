# Imports
import inspect

# This function exists to help with debugging.
# The function gets a description of the error, gets what line the code 
# was executed at, and writes both of those things to debug_logs.txt. It
# also prints a message to the standard output about what happened.

# Debug function:
def debug(error_description, error_message):
    with open('debug_logs.txt', 'a') as debug_logs:
        line=("line "+str(inspect.currentframe().f_back.f_lineno))
        line=''.join(line)
        error=("\n"+error_description+" "+line+"\n")
        error=''.join(error)
        debug_logs.write(error)
        print(error_message)
