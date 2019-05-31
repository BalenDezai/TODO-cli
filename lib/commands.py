#   this module is for the handling of command arguements and the commands


def commandInterpreter(sysargs=[]):
    if len(sysargs) == 2:
        arrResult = []
        arrResult.append(sysargs[1])
        return arrResult