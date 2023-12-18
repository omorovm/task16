## Для начала работы с программой необходимо выполнить в терминале следующие действия

> [!IMPORTANT]
> У вас должен быть установлен **Python** и **Visual Studio Code**. Так же необходимо создать новую папку перенести туда все файлы.


- [ ] Создать и активировать виртуальное окружение.

```
cd Desktop/{название папки}
python3 venv venv
. venv/bin/activate
```

- [ ] Установить необходимые библиотеки.

```
pip install -r requirements.txt
```

- [ ] Открыть Visual Studio Code

```
code .
```

## Далее необходимо изменить базовые настройки

Переходим в папку ```config``` и открываем файл ```settings.py```. Далее необходимо сменить настройки в ```DATABASE```

> 'ENGINE': 'django.db.backends.postgresql' если используете другую базу данных, то вместо ```postgresql``` пропишите свою

> 'NAME': 'databasename' необходимо создать базу данных и вписать ее наименование 

> 'USER': 'username' вписать имя пользователя

> 'PASSWORD': 'user_password' пароль пользователя

> 'HOST': 'localhost' оставляем без изменений

> 'PORT': 5432 оставляем без изменений

## Начинаем работу в Python shell

Для запуска необходимо прописать в терминале команду.

> ./manage.py shell

### Пример работы в shell

***Работа с моделью ManytoManyApp***

Импортируем модели приложения с которыми собираемся работать. 

```from ManytoManyApp.models import Student, Teacher```

- Создание и получение всех объектов модели.

```
student1 = Student.objects.create(name='first', age =15)
student2 = Student.objects.create(name='second', age =16)
student3 = Student.objects.create(name='third', age =17)
teacher1 = Teacher.objects.create(name='first', subject='math', expirience=2)
teacher2 = Teacher.objects.create(name='second', subject='bio', expirience=4)
all_stud = Student.objects.all()
all_tech = Teacher.objects.all()
```

- Фильтрация объектов по определенным условиям.

```
srud_f = Student.objects.filter(age__gt=15) поиск студентов старше 15
srud_f проверка
teach_f = Teacher.objects.filter(expirience__lt=4) поиск преподователей со стажем менее 4 лет
teach_f проверка
```

- Использование связанных моделей с помощью `related_name`.

```
teacher1.students.set([student1,student2]) обращаемся к связи и добавляем студентов
teacher1.students проверка (выведет связь)
teacher2.students.set((student1, student3))
teacher2.students.all() проверка (выведет связанных студентов)
student1.teachers.all() проверка обратной связи (выведет связанных учетелей)
```

- Использование агрегирующих функций (например, count, sum, avg) для получения ста-
тистики данных.

```
from django.db.models import Avg импортируем библиотеку для агрегации
student_age = Student.objects.aggregate(Avg('age')) получение среднего возраста студентов
student_age проверка
total_exp = sum(teacher.expirience for teacher in Teacher.objects.all()) общий опыт преподователей
total_exp проверка
st_count = Student.objects.filter(age__gt=15).count() количество студентов старше 15
st_count проверка
```


***Работа с моделью OnetoOneApp***

- Создание объектов модели.

```
from OnetoOneApp.models import Brain, Human
brain1 = Brain.objects.create(iq=110, weight=2)
human1 = Human.objects.create(sex='male', brain=brain1)
```

- Использование связанных моделей с помощью `related_query_name`.

```
brain1.human выдаст нам связанный объект а не связь как в related_name
```

- Обновдение модели.

```
brain1.iq = 150
brain1.save()
```
>[!NOTE]
> Чтобы проверить изменение необходимо через терминал зайти в базу данных и вывести все значения `select * from "OnetoOneApp_brain";`

- Получение объектов по id

```
brain_get = Brain.objects.get(pk=1)
```

- Удаление оъектов.

```
brain1.delete()
```