'''
sys: We need to import sys for printf to work.
'''
import sys


def printf(*strings) -> None:
    '''
    This function emulates the behaviour of the printf function in C.
    '''
    for string in strings:
        frame = sys._getframe(1)
        locals_dict = frame.f_locals
        evaluated_string = string.format(**locals_dict)
        print(evaluated_string)
        return None
