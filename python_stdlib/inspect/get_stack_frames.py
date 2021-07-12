import inspect

"""
currentframe() returns the frame at the top of the
stack(for the current location). getargvalues() returns
a tuple with argument names, the names of the variable
arguments, and a dictionary with local values from the frame.
"""


def recurse_currentframe(limit):
    local_variable = '.' * limit
    print(limit, inspect.getargvalues(inspect.currentframe()))
    if limit <= 0:
        return
    recurse_currentframe(limit - 1)
    return


def recurse_stack(limit):
    local_variable = '.' * limit
    if limit <= 0:
        for frame, filename, line_num, func, source_code, source_index \
                in inspect.stack():
            #print(source_code, source_index)
            print(
                f"{filename}[{line_num}]\n -> {source_code[source_index].strip()}")
            print(inspect.getargvalues(frame))
            print()
        return
    recurse_stack(limit-1)
    return


if __name__ == "__main__":
    recurse_currentframe(3)
    print()
    recurse_stack(3)
