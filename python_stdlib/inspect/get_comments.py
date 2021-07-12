# it is also possible to get preceding comments

import inspect
import example

print(inspect.getcomments(example.B.do_something))

# the return value is always the first comment in the value
print(inspect.getcomments(example))
