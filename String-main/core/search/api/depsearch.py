import aiohttp
import asyncio 
import json

from rich.console import Console
from aiohttp import TCPConnector, Fingerprint

string = Console()

from core.injector import injector_color, injector_private_api
from core.module.gradient import log_message, api

one,two = injector_color()

async def ipquery(session, sem, url):
    async with sem:
        try:
            async with session.get(url, timeout=4) as response:
                if response.status == 200:
                    data = await response.json()
                    results = data.get('results', [])
                    
                    for i, entry in enumerate(results, 1):
                        api(f"Запись No{i}", "DepSearch")
                        for key, value in entry.items():
                            string.print(f"{key}{two}: {one}{value}")

                        print()
                    return data
                
                else:
                    log_message(f"⚠️ Ошибка DepSearch API: {response.status}")

        except asyncio.TimeoutError:
            log_message("⏳ Время ожидания истекло (Timeout)")
            
        except aiohttp.ClientConnectorError:
            log_message("🌐 Ошибка узла: проверьте подключение или DNS")
            
        except aiohttp.ContentTypeError:
            log_message("🧩 API прислал не JSON (возможно, бан или капча)")
            
        except aiohttp.ClientError as e:
            log_message(f"📡 Ошибка запроса aiohttp: {e}")
            
        except json.JSONDecodeError:
            log_message("📄 Ошибка декодирования JSON")
            
        except Exception as e:
            log_message(f"⚠️ Непредвиденный сбой")       

async def search_depsearch(requests):
    token = injector_private_api("dep")
    url = f"https://api.depsearch.sbs/quest={requests}&token={token}&lang=ru"
    sem = asyncio.Semaphore(5)
    FINGERPRINT_HEX = "a9e0d39d6782bc8c1424f5cab116d254c07341fd9de5aa518fdc469a7703e622"
    fp = Fingerprint(bytes.fromhex(FINGERPRINT_HEX))
    connector = TCPConnector(ssl=fp) 

    async with aiohttp.ClientSession(connector=connector) as session:
        ipqw = await ipquery(session, sem, url)

        from core.injector import injector_settings
        save = injector_settings("save")

        if save == "ok":
            from core.settings import saver
            saver("api-depsearch", ipqw)
            log_message("☑️ Информация сохранена!")