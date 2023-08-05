"""A demostration of positional and keyword arguments in functions
and function calls"""


# This function is defined with one positional argument and one keyword argument
# The second (message )parameter has been defined with a default value which 
# is displayed if it is ommited in the function call
def shirt(size, message = 'Learn Python Now!'):
    """Prints a message and size of shirt ordered"""
    print(f'The message on this shirt is "{message}" and it\'s a size {size}')

#  This function call ommits the message argument so the default is supplied
shirt(12)

# It can be called in multiple ways
# This function call explicitly provides a keyword pair for both arguments. 
# When called like this the argument position doesn't matter
shirt(message="I'd Java not", size=10)

# When the keyword pair is not exlpicitly provided then python pair the arguments
# positional. It becomes important to make sure thet the arguments are provided in 
# right order or else the code will not work as exoected
shirt('blunder', 6)

# Positional arguments must come before keyword argument or an error will be raised
# shirt(message='Try it', 9)

