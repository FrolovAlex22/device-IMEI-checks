# Проект device-IMEI-checks

## Описание

Телеграм бот для проверки номер IMEI. Проводит валидацию номера IMEI и делает
запрос к API сервиса imeicheck, и возвращает информацию об устройстве. Работа
бота доступна пользователям внесенным в белый список.
Пользователю нужно просто отправить IMEI номер


## Установка и запуск.
1. Склонируйте репозиторий:
   ```
   git clone git@github.com:FrolovAlex22/device-IMEI-checks.git
   ```
2. Перейдите в директорию проекта:
   ```
   cd device-IMEI-checks
   ```
3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
4. Запуск программы:
   ```
   python app.py
   ```

## Технологии:
[![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/Aiogram-blue)](https://aiogram.dev/)

### Автор:

Фролов Александр
email: frolov.bsk@yandex.ru
telegram: https://t.me/frolov_bsk