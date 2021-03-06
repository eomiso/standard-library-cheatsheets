import imp
import inspect
import sys

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = 'example.py'

try:
    (name, suffix, mode, mtype) = inspect.getmoduleinfo(filename)

except TypeError:
    print(f"could not determine type of {filename}")
else:
    mtype_name = {imp.PY_SOURCE: 'source',
                  imp.PY_COPILED: 'compiled',
                  }.get(mtype, mtype)
    mode_description = {'rb': '(read-binary)',
                        'U': '(universal newline)',
                        }.get(mode, '')

    print('NAME     :', name)
    print('SUFFIX   :', suffix)
    print('MODE     :', mode, mode_description)
    print('MTYPE    :', mtype_name)
