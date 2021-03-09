# 8-16. Imports: Using a program you wrote that has one function in it, 
# store that function in a separate file. Import the function into your 
# main program file, and call the function using each of these approaches:

# import module_name 
# from module_name import function_name 
# from module_name import function_name as fn 
# import module_name as mn 
# from module_name import *

"""import module_name """

import printing_functions_8_15
print("import module_name")

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions_8_15.print_models(unprinted_designs, completed_models)

print(completed_models)
print("--------------------------")

""" from module_name import function_name  """
from printing_functions_8_15 import print_models
print("from module_name import function_name")

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)

print(completed_models)
print("--------------------------")

"""from module_name import function_name as fn """
from printing_functions_8_15 import print_models as p_f
print("from module_name import function_name as fn")

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

p_f(unprinted_designs, completed_models)

print(completed_models)
print("--------------------------")

"""import module_name as mn """
print("import module_name as mn")
import printing_functions_8_15 as p_f

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

p_f.print_models(unprinted_designs, completed_models)

print(completed_models)
print("--------------------------")

# """from module_name import *"""
print("from module_name import *")
from printing_functions_8_15  import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)

print(completed_models)
print("--------------------------")


