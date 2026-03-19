import os,json
from datetime import datetime;
from core.injector import read_file, save_settings_settings
from core.module.gradient import log_message

def get_time():
    return datetime.now().strftime("%H-%M-%S")

def saver_info(filename, info):
    with open(filename, 'w', encoding='utf-8') as file:
        if isinstance(info, (list, dict)):
            file.write(json.dumps(info, indent=4, ensure_ascii=False))
        else:
            file.write(str(info))

def saver(method, info):
    filename = f"{method}-{get_time()}.txt"
    saver_info(filename, info)

def turn_on_or_off_save(choice):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    folder = os.path.join(desktop, "string")
    path = os.path.join(folder, "Settings.json")

    if choice == "on":
        save_settings_settings(path, "Yes")
        log_message("Сохранение отчета - включено")

    elif choice == "off":
        save_settings_settings(path, "Nope")
        log_message("Сохранение отчета - выключено")

def remove_static_gradient(one,two):
    
    path = os.path.join(os.path.dirname(__file__), "config", "Color.json")

    with open(path,'r',encoding='utf-8') as file:
        data = json.load(file)

        data["gone"] = one
        data["gtwo"] = two

        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    log_message("☑️ Сохранил цвета.")

def remove_static_color(one,two):

    path = os.path.join(os.path.dirname(__file__), "config", "Color.json")
    one = f"[{one}]"
    two = f"[{two}]"
    with open(path,'r',encoding='utf-8') as file:
        data = json.load(file)

        data["one"] = one
        data["two"] = two

        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    log_message("☑️ Сохранил цвета.")

def clear_color_gradient():
    path = os.path.join(os.path.dirname(__file__), "config", "Color.json")
    with open(path,'r',encoding='utf-8') as file:
        data = json.load(file)

        data["one"] = "[#808080]"
        data["two"] = "[#FFFFFF]"
        data["gone"] = "60, 60, 60"
        data["gtwo"] = "200, 200, 200"

        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    log_message("☑️ Убрал цвета.")




