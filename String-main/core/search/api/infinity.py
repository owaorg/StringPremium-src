import aiohttp, asyncio, json
from rich.console import Console

from core.injector import injector_color, injector_private_api
from core.module.gradient import api

string = Console()
one, two = injector_color()

async def search_infinity(method, request):
    async with aiohttp.ClientSession() as session:

        if method == "number":
            url = f"https://infinity-check.online/find?phone={request}&token={injector_private_api('infinity')}"
        elif method == "email":
            url = f"https://infinity-check.online/find?email={request}&token={injector_private_api('infinity')}"
        else:
            print(f"❌ Неподдерживаемый метод: {method}")
            return
        try:
            async with session.get(url, timeout=5) as response:
                data = await response.json()
                results = data.get('results', [])
                
                if not results:
                    string.print(f"[{one}] Результатов по данному запросу не найдено.[/{one}]")
                    return

                for i, entry in enumerate(results, 1):
                    print()
                    api(f"Запись No{i}", "Infinity") 
                    
                    for key, value in entry.items():
                        if value:
                            clean_key = key.replace('_', ' ').capitalize()
                            string.print(f" {clean_key}{two}: {one}{value}")
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
            log_message(f"⚠️ Непредвиденный сбой: {type(e).__name__}")