# Пульт охраны банка
Пульт управления для охранников банка, помогает следить за всеми, кто находится внутри хранилища.

## Как установить
- Получите права доступа к базе данных сотрудников.
- Заполните эти данные в файл по пути /project/settings.py
- Для изоляции проекта рекомендуется развернуть виртуальное окружение:
**для Linux и MacOS**
```
python3 -m venv env
source env/bin/activate
```
**для Windows**
```
python -m venv env
venv\Scripts\activate.bat
```
- Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Использование
- Запуск пульта:
```
python main.py
```
- Панель пульта находится по адрессу: http://127.0.0.1:8000/
- На главной странице, находится вывод активных карт доступа:
![active_cards](https://github.com/viktorshish/django-orm-watching-storage/assets/108957333/0a499a3a-ab19-42a5-99cb-0a1f9562d43d)
- При выборе любого сотрудника, выводится информация по всем посещениям хранилища:
![visits_card](https://github.com/viktorshish/django-orm-watching-storage/assets/108957333/92f66788-ae33-40aa-8a36-437dd49c2451)
- Кнопка **Список пользователей в хранилище** показывает кто сейчас находится в хранилище.
![card_in_storage](https://github.com/viktorshish/django-orm-watching-storage/assets/108957333/ccef657f-68d1-45d1-b832-653568880c22)

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
