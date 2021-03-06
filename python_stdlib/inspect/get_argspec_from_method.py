# Method and Function Arguments

import inspect
import example

arg_spec = inspect.getargspec(example.module_level_function)

print('NAMES    :', arg_spec[0])
print('*        :', arg_spec[1])
print('**       :', arg_spec[2])
print('defaults :', arg_spec[3])

args_with_defaults = arg_spec[0][-len(arg_spec[3]):]
print(args_with_defaults)
print("args & default : ", zip(args_with_defaults, arg_spec[3]))
