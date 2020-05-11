import importlib


def getModuleClass(commandToExecute: dict):
    module = importlib.import_module(commandToExecute["moduleName"])
    my_class = getattr(module, commandToExecute["className"])
    classObj = my_class()
    return classObj
