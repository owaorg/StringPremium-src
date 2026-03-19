from importlib.util import spec_from_loader
from ntpath import exists
import os
import json

#from module.gradient import log_message

def read_file(path): #Принимает путь и читает только JSON файл и выплевывает что он прочитал
    with open(path, "r", encoding='utf-8') as file:
        js = json.load(file)

        return js

def save_settings_settings(path, flag): #Сохраняет файлы
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
        
    data["Save-Info"] = flag
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def save_name(username):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_path = os.path.join(desktop, "string")
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, "user.json")
    data = {
        "UserName": username
    }
    with open(file_path, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("[DEBUG-FUNC] Ваш никнейм был сохранен, перезапустите программу.")


def injector_color():
    path = os.path.join(os.path.dirname(__file__), "config", "Color.json") # Использование one,two = injector_color()

    js = read_file(path)
    
    one = js["one"]
    two = js["two"]

    return one,two

def injector_private_api(api): # Получение токенов
    path = os.path.join(os.path.dirname(__file__), "config", "API.json")

    apiska = read_file(path)

    if api == "dep":
        return apiska["dep"]
    elif api == "infinity":
        return apiska["infinity"]
    elif api == "zalupa":
        return apiska["xyina"]

def injector_settings(method):
    if method == "username":
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        folder = os.path.join(desktop, "string")
        path = os.path.join(folder, "User.json")
        os.makedirs(folder, exist_ok=True)
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as f:
                json.dump({}, f, indent=4)
        
        js = read_file(path)
        return js.get("UserName", "Нету")
    
    elif method == "save":
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        path = os.path.join(desktop, "string", "Settings.json")


        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path), exist_ok=True)

        if not os.path.exists(path):
            default_settings = {"Save-Info": "Yes"}
            with open(path, "w", encoding="utf-8") as f:
                json.dump(default_settings, f, indent=4)
            return "ok" 

        try:
            js = read_file(path)
            response = js.get("Save-Info", "No") 

            if response == "Yes":
                return "ok"
            else:
                return "false"
        except Exception:
            return "false"
        
def injectro_gradient_color():  # Для инжекта цветов RGB

    path = os.path.join(os.path.dirname(__file__), "config", "Color.json")
    result = read_file(path)

    gone_str = result["gone"]  
    gtwo_str = result["gtwo"]  
    one = tuple(int(x.strip()) for x in gone_str.split(','))
    two = tuple(int(x.strip()) for x in gtwo_str.split(','))
    

    return one, two
        


