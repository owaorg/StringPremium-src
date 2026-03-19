String V1.2

String - Премиальный Инструмент для анализа данных как с открытых так и закрытых источников. Пожалуйста, учтите тот факт что он идет как есть, в данной версии вырезаны многие URL/API, этот билд всего лишь показывает что String реально существует.

String1.2/
│
├── main.py                          # Entry point - запуск CLI
│   └── main()                       # Асинхронный запуск core.main.main()
│
└── core/
    │
    ├── main.py                      # Главная логика CLI
    │   ├── perform_auth()           # Авторизация пользователя
    │   └── main()                   # Парсинг аргументов и маршрутизация
    │
    ├── injector.py                  # Загрузка конфигов
    │   ├── read_file()              # Чтение JSON файлов
    │   ├── save_settings_settings() # Сохранение настроек
    │   ├── save_name()              # Сохранение username
    │   ├── injector_color()         # Получение цветов
    │   ├── injector_private_api()   # Получение API токенов
    │   ├── injector_settings()      # Получение настроек (username, save)
    │   └── injectro_gradient_color()# Получение RGB цветов для градиента
    │
    ├── settings.py                  # Настройки сохранения
    │   ├── get_time()               # Текущее время
    │   ├── saver_info()             # Сохранение данных в файл
    │   ├── saver()                  # Сохранение с именем файла
    │   ├── turn_on_or_off_save()    # Вкл/выкл сохранения
    │   ├── remove_static_gradient() # Установка градиента
    │   ├── remove_static_color()    # Установка цветов
    │   └── clear_color_gradient()   # Сброс цветов
    │
    ├── acd.py                       # API роутер
    │   └── automatic_method_search_api()  # Маршрутизация API запросов
    │
    ├── config/                      # JSON конфигурации
    │   ├── API.json                 # API токены (dep, infinity)
    │   └── Color.json               # Цвета (one, two, gone, gtwo)
    │
    ├── module/                      # Утилиты и модули
    │   │
    │   ├── clear.py                 # Очистка консоли
    │   │   └── clear_screen_string()    # Очистка экрана (cls)
    │   │
    │   ├── gradient.py              # Цветной вывод
    │   │   ├── log_message()        # Вывод с градиентом
    │   │   └── api()                # Вывод API с градиентом
    │   │
    │   ├── helper.py                # Справка
    │   │   ├── write()              # Запись в файл
    │   │   └── write_helper()       # Создание help.txt/md/вывод
    │   │
    │   ├── interface.py             # Интерфейс баннер
    │   │   └── write_interface()    # Вывод баннера и информации
    │   │
    │   └── system.py                # Системная информация
    │       └── get_pc_info()        # Получение info о ПК
    │
    └── search/                      # Поиск
        │
        ├── api/                     # Платные API
        │   │
        │   ├── depsearch.py         # DepSearch API
        │   │   ├── ipquery()        # Запрос к API
        │   │   └── search_depsearch()   # Поиск по базам
        │   │
        │   └── infinity.py          # Infinity API
        │           └── search_infinity()  # Поиск по номеру/email
        │
        └── osint/                   # Бесплатные OSINT
            │
            ├── cords.py             # Координаты
            │   └── decoder_geo()    # Декодирование LAT/LON в адрес
            │
            ├── ip.py                # IP информация
            │   ├── ipquery()        # Запрос к ipquery.io
            │   └── search_ip()      # Вывод информации об IP
            │
            ├── number.py            # Номер телефона
            │   ├── phonenumbers_lookup()  # Парсинг номера
            │   ├── search_number()  # Запрос к voxlink
            │   └── number_logic()   # Основная логика
            │
            ├── proxy.py             # Проверка прокси
            │   └── check_proxy()     # Проверка работоспособности
            │
            └── whois.py             # Домены
                ├── analyze_vt()     # Анализ VirusTotal
                ├── analyze_freak()  # Анализ WhoIsFreaks
                └── search_domen()