# Куда пойти — Where to go

Сайт показывает самые интересные места в Москве. 

[Демка сайта](http://swatlprus.pythonanywhere.com/).

## Подготовка к запуску

Для запуска сайта вам понадобится Python 3.8+ версии. Скачайте код с GitHub. Создайте виртуальное окружение. Затем установите зависимости.

Чтобы скачать код с Github, используйте команду:
```shell
git clone https://github.com/Padking/where-to-go.git
```
Для создания виртуального окружения используйте команду (Linux):
```shell
python3 -m venv venv
```
Для устаонвки зависимостей, используйте команду:
```shell
pip3 install -r requirements.txt
```
## Настройка переменных окружения

Пример .env файла
```
SECRET_KEY=django-insecure-*9+eu5va4qprh3l8@\cdscdsfdsdssssn+%s0
DEBUG=False
ALLOWED_HOSTS='*'
```
SECRET_KEY - секретный Django-ключ
DEBUG - Включить или выключить режим Debug (На проде всегда режим False)
ALLOWED_HOSTS - Адрес хоста, где размещается сайт (Указывать в виде строки)

## Как запустить

Команда для запуска проекта локально (Linux):

```shell
python3 manage.py runserver
```
Переходите по данному адресу, где увидите карту Москвы
```
http://127.0.0.1:8000/
```

## Добавление мест с помощью кода

Команда под Linux:
```shell
python3 manage.py load_place http://адрес/файла.json
```

Примеры JSON файлов можно взять [здесь](https://github.com/devmanorg/where-to-go-places/tree/master/places)

## Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).