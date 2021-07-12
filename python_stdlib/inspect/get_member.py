import inspect

import example

for name, data in inspect.getmembers(example):
    if '__builtins__' in name:
        continue
    print(f"{name}: {repr(data)}")
