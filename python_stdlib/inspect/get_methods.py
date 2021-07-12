import inspect
from pprint import pprint

import example

# inspect.getmembers(object[, predicate])
pprint(inspect.getmembers(example.A, inspect.isfunction))
