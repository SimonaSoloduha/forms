# forms
WEB приложение для создания, редактирования и заполнения форм

### Система состоит из двух частей

### Первая часть - сайт data на котором есть редактор форм (как в гугл формах, можно добавлять/редактировать/удалять поля).
Набор типов полей формы ограничен до: input, textarea, select.

### Вторая часть - отдельный сайт site на котором можно заполнить созданную форму, заполнение происходит через API первого сайта (data).
Также, на втором сайте есть страница с отображение сохраненных данных.        


## Запуск проекта:

Откройте консоль

Перейдите в папку, в которой будет храниться проект

cd <путь до папки>

Склонируйте проект
git clone https://github.com/SimonaSoloduha/forms

## Перейдите в папку проекта
cd forms

## Создайте виртуальное окружение venv
python3 -m venv venv

## Активируйте виртуальное окружение venv
source venv/bin/activate

## Установите необходимые пакеты:

cd data_form
pip3 install -r requirements.txt
(Все используемые библиотеки представлены в файле requirements.txt)

## При необходимости обновите pip и отдельно установить следующие пакеы: 

python3 -m pip install django
pip3 install djangorestframework
python3 -m pip install requests 

# Запустите миграции 

python3 manage.py migrate  

# Запустите проект через консоль 

python3 app.py runserver 


* Для создания и редактирования форм перейдите на сайт: 
http://127.0.0.1:8000/data/

* Для заполнения созданых форм перейдите на сайт: 
http://127.0.0.1:8000/site/ 

* Для завершения работы ввеите в консоли "Contril + C"
