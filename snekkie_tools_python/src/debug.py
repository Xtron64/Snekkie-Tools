# IMPORTS
from inspect import currentframe, getframeinfo  # This is required so that we can log the file and line that the function was called at
# DOCUMENTATION
# The log_bug function logs a bug to 'debug_logs.txt'
# the log_bug function has two parameters:
#
# - description
# This parameter is required. Explain what error occured
# (or you think occured) as a string in this parameter.
# The contents of parameter are saved to 'debug_logs.txt',
# along with which file this function was ran in, and which
# line it was ran at.
#
# - message
# This parameter isn't required. If you want to tell the
# user anything then write it in a string here. It will be
# printed to the CLI.


def log_bug(description, message=None):
    frameinfo = getframeinfo(currentframe())  # Gets current file and line
    line = frameinfo.lineno  # Stores the line in a variable
    file = frameinfo.filename  # Stores the location of the file in a variable
    log = (f"\n{description}\n File: {file}\n Line: {line}.\n")  # Puts the description, the file location and the line number (that the function was called at) in a variable
    with open("debug_logs.txt", "a") as logs:  # Opens 'debug_logs.txt' in append mode as logs
        logs.write(log)  # Writes the thing I explained earlier to 'debug_logs.txt'
        logs.close()  # Closes 'debug_logs.txt'
    if message:  # If the message parameter has a value:
        print(message)  # Outputs the value to the user
