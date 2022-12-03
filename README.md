<p align="center"><img src="https://user-images.githubusercontent.com/86917587/205442678-038f1e15-cc09-4f74-8462-86b0757f3eab.svg" width="50"></p>
<h1><p align="center">NNCImage</p></h1>

***

   Аналог Pinterest. Сайт написанный на __Django__, для размещения изображений на определённую тематику. 
На сайте реализована возможность добавления изображений с тайтлом и описанием. Система комментариев под каждым постом. Добавление и редактирование профиля. Создание 

   Для проверки работы сайта можно воспользоваться готовой [Базой данных](https://disk.yandex.ru/d/S9eO1qiQkU-0yA) PostgreSQL

*** 
# Запуск проекта 

1) Клонировать или скачать проект
3) Создать виртуальное окружение в папке проекта: 

        python3 -m venv venv

4) Требования к установке приложения: 

        pip install -r requirements.txt

5) Databse migrate: 

        python manage.py migrate

6) Запустите сервер: 

        python mysite/manage.py runserver

7) Откройте ссылку: http://127.0.0.1:8000/




***

<h1> Требования </h1>

- Python -- 3.10.4
- Django -- 4.1.1
- Pillow -- 9.2.0
- PostgreSQL -- 14

***
# Пример начальной страницы

<p  align="center"><img src="https://user-images.githubusercontent.com/86917587/205442668-444d0ff5-b39d-49a6-88cc-736a28e01572.png" width="800"></p>

