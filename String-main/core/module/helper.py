from rich.console import Console
from core.injector import injector_color

one,two = injector_color()

string = Console()
help_text = f"""{two}╭── {two}📃 {two}Управление справкой ─────
{two}├ {one}string {one}--thelp   
{two}├ {one}string {one}--mdhelp  
{two}╰ {one}string {one}--shelp   

{two}╭── {two}🌐 OSINT Анализ ─────
{two}├ {one}string {one}--phone {two}+7218743456    
{two}├ {one}string {one}--whois {two}string.com     
{two}├ {one}string {one}--ip    {two}127.8.8.8      
{two}├ {one}string {one}--lat {two}38.0{one} --lon {two}31.0{one}  
{two}├ {one}string {one}--public-proxy {two} 164.90.151.28:3128
{two}╰ {one}string {one}--private-proxy {two} proxy:port:login:password

{two}╭── {two}🔎 Поиск по Базам ─────
{two}├ {one}string {one}--api-number   {two}+7218743456 {one}--api {two}infinity/depsearch        
{two}├ {one}string {one}--api-people   {two}Питонов Пваха Стрингович     
{two}├ {one}string {one}--api-mail     {two}pwaexho@string.com {one}--api {two}infinity/depsearch                 
{two}├ {one}string {one}--api-vin      {two}1FAFP53U7YG164887            
{two}├ {one}string {one}--api-pass     {two}string123                    
{two}├ {one}string {one}--api-snils    {two}541-251-383 52               
{two}├ {one}string {one}--api-inn      {two}37507352790                  
{two}├ {one}string {one}--api-vk       {two}https://vk.com/string        
{two}╰ {one}string {one}--api-ip       {two}8.8.8.8                      

{two}╭── {two}⚙️ Настройки ─────
{two}├ {one}string {one}--save    {two}on/off                    
{two}├ {one}string {one}--g1      {two}1,1,1,1 {one}--g2 {two}1,1,1,1 
{two}├ {one}string {one}--с1      {two}#E0FFFF {one}--с2 {two}#E0FFFF  
{two}╰ {one}string {one}--remove                            """

md = """
# Руководство по использованию String

**Введение**  
STRING — профессиональный премиальный инструмент для получения информации с разных источников, начиная с платных заканчивая платными. Он сможет автоматизировать рутинную работу и сберечь ваши денежные средства.

**Руководство**  
`string --thelp` — Создает текстовый файл с этим мануалом  
`string --mdhelp` — Создает md файл с этим мануалом  
`string --shelp` — Выводит данный мануал в терминал

*Внимание, символы `<>` никак не нужно вводить. Они нужны для того, чтобы пользователи не путались.*

---

**OSINT Анализ**  
`string --phone <+7218743456>`  
`string --whois <string.com>`  
`string --ip <127.8.8.8>`  

---

**API Анализ**  
`string --api-number <+7218743456>`  
`string --api-people <Питонов Пваха Стрингович>`  
`string --api-mail <pwar@string.com>`  
`string --api-vin <1FAFP53U7YG164887>`  
`string --api-pass <string123>`  
`string --api-snils <541-251-383 52>`  
`string --api-inn <37507352790>`  
`string --api-ip <127.8.8.8>`  
`string --api-vk <https://vk.com/string>`
`string --api-ip < 8.8.8.8 >`
---

**Настройка (По желанию)**  
`string --save <on/off>` — Сохранение информации в файл
"""

def write(file,wr):
    with open(file, "w", encoding="utf-8") as file:
        file.write(wr)

def write_helper(method):
    if method == "thelp":
        write("help.txt", help)

    elif method == "mdhelp":
        write("help.md", md)

    elif method == "shelp":
        string.print(help_text)