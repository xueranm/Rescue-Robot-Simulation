#===============================================================================
# P4_Utility.py
# Created by < Xueran Ma > - < 5/23/2016 >
# Version 0.1
# Derived in part from Dave Kieras' design and implementation of EECS 381 Proj 4
#===============================================================================

class BadLineError(Exception):
    '''
    This exception is thrown any time that an error occurs such that the entire command line
    needs to be output along with the error statement, such as in the following exchange:
    Time 0 > garbage in
    Unrecognized command: garbage in
    '''
    pass


class BadMsgError(Exception):
    '''
    This exception is thrown any time that a message needs to get passed to the exception-handling
    code, which is done as was shown in lecture.
    '''
    pass