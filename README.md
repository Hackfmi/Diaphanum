Diaphanum
=========

Проектът, чрез който Студентски Съвет към СУ ще може да бъде ръководен прозрачно и отворено.


Да си нагласим средата
--------------------

Преди да започнем, ако нямате инсталиран гит на машината - кво да играя. Пълен минус.


Python Stuff
------

Добре, трябва да имате тези две неща.

- [Python2.7 (Windows)](http://www.python.org/ftp/python/2.7.5/python-2.7.5.amd64.msi)
- [PIP (Windows)](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip)  # Thanks to Fil :)

Ако сте на Linux пък живота ви е лесен:

    apt-get install python-pip

или

    yum -y install python-pip

според зависи.


------------------------------

Django
--------
Сега, по съществената част:

- Kлонирайте [Diaphanum](git@github.com:Hackfmi/Diaphanum.git) (в линукс: git clone git@github.com:Hackfmi/Diaphanum.git)
- Стигнете до директорията чрез терминал и напишете: **pip -r requirements.txt**
- За всеки случай сега напишете pip freeze и нещата, които ще ви излязат трябва да са същите като тези в requirements.txt

- Сега сте готови, като единственото нещо което трябва да направите е да си добавите db-то.

ДъБъ-ту:
---------

Ако забелязвате в .gitignore има споменато **local_settings.py**, а па в setting.py

    try:
        from local_settings import *
    except ImportError:
        pass

Именно в local_settings.py селектирате вашата база данни. **КАТО**
- Тя няма да се качва в Git и ще си стой само на вашата машина
- Пример, за това как трябва да изглежда local_settings, може да видите в **example_local_settings.py**

Относно базите данни за хакатона сме избрали да ползваме postgresql9.2 (за това и имаме psycopg2==2.5.1 в requirements.txt). Как да си оправите db-то и да го свържите с Django ще обясним по-надолу (надявам се).


Финал:
-------

Ако сте изпълнили всички стъпки горе, може да отворите терминал и да стигнете до hackfmi директорията. Драснете едно **python manage.py runserver** за да се уверим, че всичко е потръгнало както трябва.

Също така ударете едно **python manage.py** и трябва да имате **[south]** и **[reversion]**. Ако имате, това значи че сме си свършили работата по нагласянето на средата.



Битката, в която много смели войни ще паднат:
--------

Ако напишете **python manage.py syncdb** ще даде грешка ако нямате въведена база данни - "викайте f1" за помощ. Ако пък ви потръгне от първия път - вие сте **шампиони**.

**ПОМНЕТЕ syncdb ще напишете само веднъж, защото ще ползваме миграции със South..(който е бил на Django лекцията знае)**




Как да си нагласите POSTGRE-то
--------------------------


*** WINDOWS ***

1) Сваляте [PostgreSQL 9.2](http://www.filehorse.com/download-postgresql-64/) може разбира се и 32-битов
2) По време на инсталация ще бъдете запитани за **парола**. Трябва да я запомните (например **hackfmi** е добър вариант)
3) И когато всичко свърши отваряте онова грозновато cmd и пишете:

    psql -U postgres

Ще ви попита за паролата (оная важната - пробвай с hackfmi ако се чудиш). След това ако всичко мине добре:

    CREATE ROLE [nickname] LOGIN password '[password]';  # да, пишете паролата в **кавички**
    CREATE DATABASE [db_name] ENCODING 'UTF8' OWNER [nickname];

После local_settings.py файла трябва да е:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '[db_name]',
        'USER': '[nickname]',
        'PASSWORD': '[password]',
        'HOST': '',
        'PORT': '5432',  # това е default на Postgre, може и да не го пишете
    }
}
```


*** LINUX ***

1) Сваляте и си слагате [PostgreSQL 9.2](http://www.postgresql.org/download/)
2) Когато всичко свърши, отваряте терминал и:

    sudo su - postgres
    createuser -s -U postgres --interactive

Ще ви пита за роля, пишете си username-а - [nickname].

Изключвате терминала. Включвате терминала.

     createdb [db_name]

След това local_settings.py трябва да придобие вида:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '[db_name]',
        'USER': '[nickname]',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
```



