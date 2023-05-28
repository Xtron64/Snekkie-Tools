'''

'''
from inspect import currentframe, getframeinfo  # This is required so that we can log the file and line that the function was called at
import os


'''
DOCUMENTATION
The log_bug function logs a bug to 'debug_logs.txt'. This function only works on Linux, and I refuse to add Windows or MacOS support, I would be fine with adding BSD support, or support forany other FOSS operating systems. The log_bug function has two parameters:
    - description:
    This parameter is the full description of what error occured. This parameter is logged to 'debug_logs.txt'. It also is raised as an error.
    - logDir:
    Put the directory of where you want to store 'debug_logs.txt'. Please make sure that it is a valid directory, you wouldn't want a function used to help with debugging to cause another bug. Also, don't set the value of this parameter to the location of the file, but instead use the directory that it is saved in. This parameter is optional.
'''
def log_bug(description, logDir=None) -> None: 
    '''

    '''
    frameinfo = getframeinfo(currentframe())  # Gets current file and line
    line = frameinfo.lineno  # Stores the line in a variable
    file = frameinfo.filename  # Stores the location of the file in a variable
    log = (f"\n{description}\n File: {file}\n Line: {line}.\n")  # Puts the description, the file location and the line number (that the function was called at) in a variable
    if logDir:  # If the logDir parameter has a value:
        dir_exists = os.path.exists(logDir)  # This variable checks if the value of 'logDir' is a valid directory
        if dir_exists:  # If the value of 'logDir' is a valid directory:
            with open(f"{logDir}/debug_logs.txt", "a") as logs:  # Opens 'debug_logs.txt' in append mode as logs in the directory given in 'logDir'
                logs.write(log)  # Writes the thing I explained earlier to 'debug_logs.txt'
                logs.close()  # Closes 'debug_logs.txt'
        else:  # If the value of 'logDir' isn't a valid directory:
            raise Exception("Invalid directory to store 'debug_logs.txt'.")  # Raises an exception about it
    else:  # If the logDir parameter doesn't have a value:
        home = os.getenv("HOME")  # Gets the location of the home directory
        with open(f"{home}/debug_logs.txt", "a") as logs:  # Opens 'debug_logs.txt' in append mode as logs in the home directory
            logs.write(log)  # Writes the thing I explained earlier to 'debug_logs.txt'
            logs.close()  # Closes 'debug_logs.txt'
    raise Exception(description)  # Raises an exception so that the interpreter knows that something's wrong
