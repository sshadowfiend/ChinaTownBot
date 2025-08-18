# 🤖 ChinaTown Bot - Telegram-бот для расчёта стоимости товаров из Китая

![GitHub](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Telegram Bot](https://img.shields.io/badge/Telegram_Bot-API-success?style=flat-square&logo=telegram)

## Техническое задание
1) Ключевая роль бота: помочь заказчику рассчитать итоговую стоимость своего заказа. Изначально, пользователь заходит на маркетплейс, смотрит цену в юанях, затем отправляет ее в бота, и тот по актуальному курсу валюты считает цену в рублях с учетом коммиссии магазина и доставки
2) Немало важной задачей было сделать так, чтобы бот мог дать ответы на все интересующие заказчика вопросы, например как разобраться в приложении маркетплейса, которое полностью на китайском языке, выбрать подходящий размер, цвет и т.д.
3) В случае, если у пользователя возникают вопросы, ответов на которые бот дать не может, бот вас перенаправит на менеджера, который вам поможет
4) Ну и последнее, нужно было встроить в него список отзывов

## 🌟 Основные функции

- 💰 Автоматический расчёт стоимости (товар + доставка + комиссия)
- 📊 Парсинг актуального курса юаня с Google
- ✍️ Система отзывов (интеграция с Telegram-каналом)
- 👨‍💻 Прямая связь с менеджером
- ❓ FAQ по работе с сервисом (с визуальными инструкциями)

## 🛠 Технологии

- Python 3.8+
- Библиотеки:
  - `telebot` (Telegram Bot API)
  - `BeautifulSoup4` (парсинг курса валют)
  - `requests` (HTTP-запросы)

## 🚀 Быстрый старт

1. Клонируйте репозиторий:
```bash
git clone https://github.com/sshadowfiend/ChinaTownBot.git
cd ChinaTownBot
```
2. Установите зависимости
```bash
pip install -r requirements.txt
```
3. Создайте файл tg_token.py с вашим Telegram API-ключом:
```bash
api_key = "ВАШ_TELEGRAM_BOT_TOKEN"
```
4. Запустите бота
```bash
python bot.py
```
## Пример работы 📸
![photo_2025-08-18_00-04-40](https://github.com/user-attachments/assets/eb074a16-1207-45e2-9f5a-8f9e3f1dcc60)
![photo_2025-08-18_00-04-57](https://github.com/user-attachments/assets/54288e00-d674-4963-a4ad-eac5cac53541)
![photo_2025-08-18_00-05-16](https://github.com/user-attachments/assets/0c761134-aa1a-46cf-a163-226b66a9d70a)
![photo_2025-08-18_00-05-45](https://github.com/user-attachments/assets/3e0c4f6d-d9ef-40e7-86dd-ecf7b2683aa6)



