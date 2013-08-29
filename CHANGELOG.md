# Changelog

## 0.1.0 (26.08.2013)

### Функционалности за първа версия

* Системата съдържа публичен архив за всички студентски проекти, подадени до момента
* Login в системата с роля администратор в /admin/ панела
* Нови потребители се създават от администаторът през админ панела
* Потребителите имат страница със собствен профил
* Профилите съдържат всички проекти на даденият студент, както и техният статус до момента
* Форма за кандидатстване за нов проект от логнат в системата студент
* В зависимост от статусът {Неразгледа, Върнат за Корекции}, даден студент може да нанася промени чрез форма за редактиране към всеки проект
* Един проект поддържа следните статуси
  * Неразгледан - Току-що паденен формуляр автоматично получава статус „Неразгледан“. Формуляр с такъв статус очаква да бъде прегледан от Проектен коодинатор
  * Върнат за корекция - Формулярът е разгледан от Проектния координатор, който е оставил коментари за пропуските в Проектния формуляр и е променил статуса му от „Неразгледан“ на „Върнат за корекция“. Формулярът очаква нанасяне на промени от Потребителя, който го е подал и след корекциите автоматично получава статус „Неразгледан“.
  * Предстои да бъде разгледан на СИС xx.xx.xxxx (дата) - Формулярът е разгледан от Проектния координатор, няма нужда от корекции и е насрочен за разглеждане на съответното заседание.
  * Разгледан на СИС хх.хх.хххх и Одобрен - Формулярът е бил обсъден на засесание на СС и е одобрен за предаване към Администрацията на СУ. Открива се ново поле във формуляра, в което Проектния координатор може да добави входящ номер и дата от Доклад за проекта внесен в Администрацията.
  * Разгледан на СИС хх.хх.хххх и Одобрен - Формулярът е бил обсъден на засесание на СС и е одобрен за предаване към Администрацията на СУ. Открива се ново поле във формуляра, в което Проектния координатор може да добави входящ номер и дата от Доклад за проекта внесен в Администрацията.
  * Разгледан на СИС хх.хх.хххх и Неодобрен - Формулярът е бил обсъден на засесание на СС и не е одобрен за предаване към Администрацията на СУ. Открива се поле, в което Проектния координатор добавя коментар относно това, защо проектът не е бил одобрен.
* Системата поддържа архив на всички проекти, който може да се достъпи на ```/projects/archive/```
* Всеки проект, може да бъде разгледан детайли по неговото ```id``` на ```/projects/archive/review/:id/```