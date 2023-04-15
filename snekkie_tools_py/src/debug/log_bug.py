# IMPORTS
from inspect import currentframe, getframeinfo  # This is required so that we can log the file and line that the function was called at


# DOCUMENTATION
# The log_bug function logs a bug to 'debug_logs.txt'
# the log_bug function has two parameters:
#
# - description
# This parameter is the full description of what error occured.
# This parameter is logged to 'debug_logs.txt'. 
# It also is raised as an error.
#
# - logDir
# Put the directory of where you want to store 'debug_logs.txt'.
# Please make sure that it is a valid directory, 
# you wouldn't want a function used to help with debugging to cause another bug.
# Also, don't set the value of this parameter to the location of the file,
# but instead use the directory that it is saved in.
# This parameter is optional.
def log_bug(description, logDir=None): 
    frameinfo = getframeinfo(currentframe())  # Gets current file and line
    line = frameinfo.lineno  # Stores the line in a variable
    file = frameinfo.filename  # Stores the location of the file in a variable
    log = (f"\n{description}\n File: {file}\n Line: {line}.\n")  # Puts the description, the file location and the line number (that the function was called at) in a variable
    with open(f"{logDir}/debug_logs.txt", "a") as logs:  # Opens 'debug_logs.txt' in append mode as logs
        logs.write(log)  # Writes the thing I explained earlier to 'debug_logs.txt'
        logs.close()  # Closes 'debug_logs.txt'
    raise Exception(description)  # Raises an exception so that the interpreter knows that something's wrong

