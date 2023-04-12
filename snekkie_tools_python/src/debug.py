# IMPORTS
from inspect import currentframe, getframeinfo

# DOCUMENTATION
# The log_bug function logs a bug to 'debug_logs.txt'
def log_bug(logData, logMessage=None):  
    frameinfo = getframeinfo(currentframe())
    line=frameinfo.lineno
    file=frameinfo.filename
    log=(f"\n{logData}. File: {file}. Line: {line}.\n")
    with open("debug_logs.txt", "a") as logs:
        logs.write(log)
        logs.close()
    if logMessage:
        print(logMessage)
    print(log)
    
