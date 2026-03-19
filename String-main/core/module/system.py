import platform

def get_pc_info():
    #Получение информации о системеы
    archprocessor = platform.machine()
    python = platform.python_version()
    processor = platform.processor()
    bulding = platform.platform()

    return archprocessor,python,processor,bulding