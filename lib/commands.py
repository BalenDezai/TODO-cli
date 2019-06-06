#   this module is for the handling of command arguments and the commands


def command_interpreter(sysargs=[]):
    arr_result = []
    while len(sysargs) >=2:
        arr_result.append(sysargs.pop(1))
    return arr_result
