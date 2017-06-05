"""
this is a doc string
"""
# import numpy # run pip3.6 install numpy

# print(dir(numpy ))
# print(numpy.__file__)

def test_func():
    """this is a doc inside funciton"""
    return 1

print('The letter "r" at the beginning'
        + r'of the string escapes special characters like this \n one' # note r before the opening '
        + 'it measn "raw" string')

# in the terminal:
# import more_funcs.mf as mf
# mf.__doc__
# mf.test_func.__doc__
