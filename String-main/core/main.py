
import argparse
from rich.console import Console
import os

from core.module.helper import write_helper
from core.module.clear import clear_screen_string
from core.module.gradient import log_message
from core.injector import injector_color

one, two = injector_color()
string = Console()

data = []

async def perform_auth():
    from core.injector import injector_settings
    from core.module.sub import main as sub_main

    status_user = injector_settings("username")
    if status_user == "Нету" or not status_user:
        log_message(f"{two}❌ Ошибка: Вы не авторизованы.")
        log_message(f"{one}Используйте: {two}string --auth <username>")
        os._exit(0)

    log_message(f"{two}🥷 Облачная Авторизация...")
    expiry_date = sub_main() 

    if expiry_date: 
        data.append(expiry_date)
    else:
        os._exit(0)
    
async def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--api-phone")
    parser.add_argument("--api-people")
    parser.add_argument("--api-mail")
    parser.add_argument("--api-vin")
    parser.add_argument("--api-pass")
    parser.add_argument("--api-snils")
    parser.add_argument("--api-inn")
    parser.add_argument("--api-vk")
    parser.add_argument("--api-ip")
    parser.add_argument("--auth")
    parser.add_argument("--remove", action="store_true")

    parser.add_argument("--public-proxy")
    parser.add_argument("--private-proxy")

    parser.add_argument("--api-tg")

    parser.add_argument("--api")

    parser.add_argument("--phone")
    parser.add_argument("--whois")
    parser.add_argument("--version", action="store_true")
    parser.add_argument("--ip")
    parser.add_argument("--save", choices=["on", "off"], help="Включить или выключить сохранение")
    parser.add_argument("--thelp", action="store_true", help="Создать текстовый файл с мануалом")
    parser.add_argument("--mdhelp", action="store_true", help="Создать md файл с мануалом")
    parser.add_argument("--shelp", action="store_true", help="Показать справку в терминале")

    parser.add_argument("--g1") #Градик
    parser.add_argument("--g2") #Градик

    parser.add_argument("--c1") #Цвет текста
    parser.add_argument("--c2") #Цвет текста

    parser.add_argument("--lon")
    parser.add_argument("--lat")

    args = parser.parse_args()

    if args.auth:
        from core.injector import save_name
        save_name(args.auth)
        os._exit(0)

    await perform_auth()
    clear_screen_string()
    from core.module.interface import write_interface
    await write_interface()

    if args.api_phone and args.api == "depsearch":
        log_message(f"🔎 Сбор информации о номере: {args.api_phone}\n")
        from core.search.api.depsearch import search_depsearch
        await search_depsearch(args.api_phone)

    elif args.api_phone and args.api == "infinity":
        log_message(f"🔎 Сбор информации о номере: {args.api_phone}\n")
        from core.acd import automatic_method_search_api
        await automatic_method_search_api("infinity", "number", args.api_phone)

    elif args.api_mail and args.api == "infinity":
        log_message(f"🔎 Сбор информации о email: {args.api_email}\n")
        from core.acd import automatic_method_search_api
        await automatic_method_search_api("infinity", "email", args.api_email)

    elif args.phone:
        log_message(f"🔎 Сбор информации о номере: {args.phone}\n")
        from core.search.osint.number import number_logic
        await number_logic(args.phone)

    elif args.thelp:
        write_helper("thelp")
    
    elif args.mdhelp:
        write_helper("mdhelp")
    
    elif args.shelp:
        write_helper("shelp")

    elif args.save:
        from core.settings import turn_on_or_off_save
        turn_on_or_off_save(args.save)

    elif args.whois:
        log_message(f"🌐 Сбор информации о домене: {args.whois}\n")
        from core.search.osint.whois import search_domen
        await search_domen(args.whois)

    elif args.version:
        log_message("Версия String 0.2-Beta")

    elif args.ip:
        log_message(f"🌍 Сбор информации о IP: {args.ip}\n")
        from core.acd import automatic_method_search_api
        await automatic_method_search_api("depsearch", args.ip)

    elif args.api_people:
        log_message(f"👤 Сбор информации о ФИО: {args.api_people}\n")
        from core.acd import automatic_method_search_api
        await automatic_method_search_api("depsearch", args.api_people)

    elif args.api_mail and args.api == "depsearch":
        log_message(f"📧 Сбор информации о почте: {args.api_mail}\n")
        from core.acd import automatic_method_search_api
        await automatic_method_search_api("depsearch", args.api_mail)

    elif args.api_vin:
        log_message(f"🚗 Сбор информации о VIN: {args.api_vin}\n")
        from core.acd import automatic_method_search_api
        await automatic_method_search_api("depsearch", args.api_vin)

    elif args.api_pass:
        log_message(f"🔑 Сбор информации о пароле: {args.api_pass}\n")
        from core.acd import automatic_method_search_api
        await automatic_method_search_api("depsearch", args.api_pass)

    elif args.api_snils:
        log_message(f"🪪 Сбор информации о СНИЛС: {args.api_snils}\n")
        from core.acd import automatic_method_search_api
        await automatic_method_search_api("depsearch", args.api_snils)

    elif args.api_inn:
        log_message(f"📑 Сбор информации о ИНН: {args.api_inn}\n")
        from core.acd import automatic_method_search_api
        await automatic_method_search_api("depsearch", args.api_inn)

    elif args.api_vk:
        log_message(f"📱 Сбор информации о ВК: {args.api_vk}\n")
        from core.acd import automatic_method_search_api
        await automatic_method_search_api("depsearch", args.api_vk) 

    elif args.api_ip:
        log_message(f"🌍 Сбор информации о IP: {args.api_ip}\n")
        from core.acd import automatic_method_search_api
        await automatic_method_search_api("depsearch", args.api_ip) 

    elif args.auth:
        from core.injector import save_name
        save_name(args.auth)

    elif args.g1 and args.g2: 
        from core.settings import remove_static_gradient
        remove_static_gradient(args.c1, args.c2)

    elif args.c1 and args.c2: 
        from core.settings import remove_static_color
        remove_static_color(args.c1, args.c2)

    elif args.remove:
        from core.settings import clear_color_gradient
        clear_color_gradient()

    elif args.lat and args.lon:
        from core.search.osint.cords import decoder_geo
        await decoder_geo(args.lat, args.lon)

    elif args.public_proxy:
        from core.search.osint.proxy import check_proxy
        log_message(f"🔌 Проверка публичного прокси: {args.public_proxy}\n")
        await check_proxy("http", args.public_proxy)

    elif args.private_proxy:
        from core.search.osint.proxy import check_proxy
        log_message(f"🔌 Проверка приватного прокси: {args.private_proxy}\n")
        await check_proxy("private", args.private_proxy)

    else:
        string.print(f"{one}Кажется, вы ошиблись... Нет такого значения.")
