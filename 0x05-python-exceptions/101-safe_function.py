#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        output = fct(*args)
    except Exception as stderror:
        sys.stderr.write("Exception: {}\n".format(stderror))
        output = None
    return output
