# log_bug() documentation:
## How to use log_bug()
Call the log_bug function where you would've instead raised an exception or error, as this function will do that, and more. This function has 2 functions: description and log_dir. 
#### description
The description parameter is required. Write the error or exception that happened as a string in this parameter. 
#### logDir
The logDir parameter isn't required. Write the location of the directory that you would like to store 'debug_logs.txt'. Please make sure that it is a valid directory, and doesn't need root user permissions to write to (we would recommend using a directory inside of your home directory). Also don't use the location of 'debug_logs.txt' but instead use the location of the directory.
## How log_bug() works
The function gets the line and file that the function was ran at and stores them in 2 seperate variables. It then opens 'debug_logs.txt' in append mode as logs. It writes the value of the description parameter aswell as the file and line that the function was called to 'debug_logs.txt'. It then closes 'debug_logs.txt'. Finally, it raises an exception with the question parameter as its value.