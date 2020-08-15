#################################################################################################################################################
#The __init__.py files are required to make Python treat directories containing the file as packages.                                           #
#This prevents directories with a common name, such as string, unintentionally hiding valid modules that occur later on the module search path. #
#################################################################################################################################################
# content of __init__.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
