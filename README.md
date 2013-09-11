<h1>Diaphanum</h1>


Проектът, чрез който Студентски Съвет към СУ ще може да бъде ръководен прозрачно и отворено.



<h2>Да си нагласим средата</h2>


<h3>Python</h3>

Ако имате желанието да се включите и да помогнете, трябва да започнете с тези две неща:

- [Python2.7 (Windows)](http://www.python.org/ftp/python/2.7.5/python-2.7.5.amd64.msi)
- [PIP (Windows)](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip)

Ако сте на Linux би трябвало да имате вече Python2.7. Ако нямате сложете си, сложете си и PIP:

    sudo apt-get install python-pip

или

    yum -y install python-pip



<h3>Django</h3>

Сега, вече трябва да имате Python. Следващата стъпка е да си сложите Framework-а.

- Kлонирайте [Diaphanum](https://github.com/Hackfmi/Diaphanum)
- Стигнете до директорията чрез терминал и напишете: ```pip install -r requirements.txt```

Ако ви изкара следната грешка -

```
Traceback (most recent call last):
  File "/var/www/mydir/virtualenvs/dev/bin/pip", line 5, in <module>
    from pkg_resources import load_entry_point
ImportError: No module named pkg_resources
```

Трябва да пуснете ```ez_setup.py``` в ```Scripts``` папката на инсталацията на Python. За да го направите, следният код върши работа:
```curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py | python```


- Ако горната команда ви се скара, че pg_config не е в PATH и използвате debian-базиран linux изпълнете: **sudo apt-get install libpq-dev python-dev**

За Windows, проблемът с pg_config се решава като изтеглите от тук - http://stickpeople.com/projects/python/win-psycopg/ - exe-то за Python 2.7 и го инсталирате.
След това ```pip install -r requirements.txt``` ще мине като песен !

<h3>Databases</h3>

За да може да направите, каквото и да е било, ви трябват някакви данни.

Ако отворите .gitignore има споменато **local_settings.py**, а в setting.py

    try:
        from local_settings import *
    except ImportError:
        pass

Ще си направите файл local_settings.py (в hackfmi/) и в него ще селектирате база данни. **КАТО**
- Тя няма да се качва в Git и ще си стои само на вашата машина
- Пример, за това как трябва да изглежда **local_settings**, може да видите в **example_local_settings.py**

<h5> От тук ще опишем два варианта </h5>

***PostgreSQL***
Ние (хората, които са участвали в проекта, ползваме **postgresql9.2**. За да си сложите такава база данни, направете следното:


***ЗА WINDOWS***

- Сваляте [PostgreSQL 9.2](http://www.filehorse.com/download-postgresql-64/) може разбира се и 32-битов

<b></b>

    psql -U postgres

Ще ви попита за паролата (оная важната - пробвай с hackfmi ако се чудиш). След това ако всичко мине добре:

    CREATE ROLE [nickname] LOGIN password '[password]';  # да, пишете паролата в кавички
    CREATE DATABASE [db_name] ENCODING 'UTF8' OWNER [nickname];

После ***local_settings.py*** файла трябва да е:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '[db_name]',
        'USER': '[nickname]',
        'PASSWORD': '[password]',
        'HOST': '',
        'PORT': '',
    }
}
```



***ЗА LINUX***

**Вариант 1:**
- Сваляте и си слагате [PostgreSQL 9.2](http://www.postgresql.org/download/)
- Когато всичко свърши, отваряте терминал:

```
sudo su - postgres
createuser -s -U postgres --interactive
``` 
    
**Вариант 2 (когато вариант 1 не сработи):**
- По време на писането на това README тази команда инсталира Postgresql 9.1:

```
sudo apt-get install postgresql
```
След което:
```
sudo su - postgres
createuser -s -U postgres -W
```


**И в двата варианта** ще ви пита за роля, пишете си username-а (за улеснение), след което пишете парола. След това, създайте база

    createdb [db_name]

После ***local_settings.py*** трябва да придобие вида:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '[db_name]',
        'USER': '[nickname (ролята от createuser)]',
        'PASSWORD': '[password (паролата от createuser)]',
        'HOST': '',
        'PORT': '',
    }
}
```


--------------

***SQLite***

Ако пък искате първо простo да разгелдате за какво става въпрос и до къде е стигнал проекта, може да ползвате SQLite.

Създайте си някъде на машината файл (например създайте в директорията на проекта файл и го именувайте ***mydb***).
После ***local_settings.py*** придобива вида:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '[FULL_PATH_TO_THE_FILE_YOU_CREATED]',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
```




<h3>Напълнете си базата с данни</h3>

За да може реално да "разцъквате" из сайта и да виждате някаква информация остава още една стъпка:
В основната пакпка има файл, който се казва ```new_data.json``` , съдържа fixture данни за по-лесно тестване.
Отворете терминал в директорията на проекта

    python manage.py syncdb --all
    python manage.py migrate --fake
    python manage.py loaddata new_data.json

------------

    python manage.py runserver
