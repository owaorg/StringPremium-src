from rich.console import Console

from core.injector import injector_color, injector_settings
from core.module.system import get_pc_info
from core.main import data

one,two = injector_color()
archprocessor,python,processor,bulding = get_pc_info()
string = Console()

async def write_interface():

    username = injector_settings("username")

    banner = f'''{one}███████{two}╗{one}████████{two}╗{one}██████{two}╗ {one}██{two}╗{one}███{two}╗   {one}██{two}╗ {one}██████{two}╗ 
{one}██{two}╔════╝╚══{one}██{two}╔══╝{one}██{two}╔══{one}██{two}╗{one}██{one}{two}║{one}████{two}╗  {one}██{two}║{one}██{two}╔════╝ 
{one}███████{two}╗   {one}██{two}║   {one}██████{two}╔╝{one}██{two}║{one}██{two}╔{one}██{two}╗ {one}██{two}║{one}██{two}║  {one}███{two}╗
{two}╚════{one}██{two}║   {one}██{two}║   {one}██{two}╔══{one}██{two}╗{one}██{two}║{one}██{two}║╚{one}██{two}╗{one}██{one}{two}║{one}██{two}║   {one}██{two}║
{one}███████{two}║   {one}██{two}║   {one}██{two}║  {one}██{two}║{one}██{two}║{one}██{two}║ ╚{one}████{two}║╚{one}██████{two}╔╝
{two}╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝'''
    
    interface = f"""
{two}╭ {one}Пользователь    {two}∼   {username}     
{two}├ {one}Процессор       {two}∼   {processor}
{two}├ {one}Сборка          {two}∼   {bulding}
{two}├ {one}Архитектура     {two}∼   {archprocessor}
{two}├ {one}Версия Python   {two}∼   {python}
{two}╰ {one}Доступ до       {two}∼   {data[0] if data else "Нет данных"}
"""
    string.print(banner)
    string.print(interface)

