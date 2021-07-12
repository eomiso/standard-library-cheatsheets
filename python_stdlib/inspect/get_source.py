import pprint
import inspect
import example

print(inspect.getsource(example.A.get_name))
print(inspect.getsource(example))

# If you need the lines of source split up, it can be easier to use
# getsourcelines() instead of getsource().
# May be good for json files
pprint.pprint(inspect.getsourcelines(example.A.get_name))
