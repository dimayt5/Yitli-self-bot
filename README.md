# Yitli-self-bot

# !Внимание! 
О проблеме с командой help в курсе я сам виноват что неуследил за этим.

# Как использовать?
Для начала установить Python под вашу систему. !ВНИМАНИЕ! ОБЯЗАТЕЛЬНО НАЖМИТЕ ГАЛОЧКУ "ADD TO PATH" Если вы пользователь linux то ничего не делайте.

Потом запустите фаил setup.bat(способ для Windows 7 - 11). Откройте терминал и введите pip install discord.py==1.7.3 и pip install requests(способ для linux)
!Внимание! Если у вас был discord.py раньше введите pip list и если версия discord.py 2.0 введите pip unistall discord.py и введите pip install discord.py==1.7.3(новая версия discord.py неподдерживает селф ботов).

# Как запустить?
Запустите фаил config.py в вашем текстовом редакторе или блокноте.
Введите токен в Login ---> token.
После этого придумайте префикс например ! % ? и напишите в Login ---> prefix.
И для команды copy которая копирует эмодзи сервера введите ID в таком пункте config.py Login ---> id основной учётной записи к примеру 990509736975794186 ведь туда будут присылатся эмодзи.
Ну и как всё закончили запустите фаил bot.bat(способ для Windows 7 - 11).
Откройте терминал и введите cd <путь/к/запускаемому/файлу/> в директории нашего Self-bot возьмите путь и нажмите ENTER и пропишите python3 bot.py(если не правильно то извините я не пользуюсь линуксом)

# ВНИМАНИЕ!
Self-bot запрешён discord ToS https://discord.com/terms! Пожалуйста испольлуйте твинк/вторая учётная запись(если есть ненужная)


# Как поставить на хостинг?
Итак чтобы поставить на хостинг вам нужно выбратся с ним! Рекомендую Heroku https://www.heroku.com/ или Repl-it https://replit.com/

# Способ для Heroku
Создайте новую ПРИВАТНУЮ репозиторию. Потом засуньте файлы которые перечислены: bot.py Procfile config.py requirements.txt.
Потом зарегестрируйтесь на сайте https://www.heroku.com/ (Для пользователей России используйте впн) и создайте новое приложение с любым названием.
И постаётся только привязать ваш аккаунт гитхаб к Heroku и после этого нажмите Deploy Branc(както так). Если не поняли смотрите в ютубе про этот хостинг.

# Способ для реплита
Чтобы поставить на реплит вам нужно тоже на нём зарегестрироватся. Потом создаёте новое приложение например sjkfskdfjdjkfgdkfgkdf(на реплите могут все увидеть ваш код).
Потом загружаете 2 ФАЙЛА из папки именно config.py и keep_alive.py.
После этого из bot.py копируете всё и вставляете в main.py(реплит настроен только под main.py).
Из файла config.py удалите токен так как его могут взять и делать всякую фигню. Создайте секретку в каталоге Tools. Создаёте переменную token и в 2 ячейку вставляете токен. И импортните import keep_alive и удалите из файла строчку "token=Login.token" и добавте из файла replit.txt место 4 последних строк кода там где старт токена.
И зарегестрируйтесь на сайте https://uptimerobot.com/ и создайте новый монитор (посмотрите в ютубе).
# Если у вас возникли вопросы или вы непоняли то ищите в ютубе.
