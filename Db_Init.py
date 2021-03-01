from Database import Person, Database, Post
from datetime import date


def init():
    Person1 = Person(89045461183, 'Завьялов Артём Борисович', None, 'ВЕДУЩИЙ ИНЖЕНЕР-КОНСТРУКТОР', 0, date(28, 2, 21),
                     57000, 'Санкт-Петербург', 'АО «Центральное конструкторское бюро машиностроения»', False)
    Person2 = Person(89502073539, 'Чебыкина Юлия Владимировна', None, 'ИНЖЕНЕР-ТЕХНОЛОГ 3 КАТЕГОРИИ', 1, date(12, 7, 20),
                     70000, 'Санкт-Петербург', 'АО «Центральное конструкторское бюро машиностроения»', False)
    Post1 = Post(0, """1. Инженер-технолог 3 категории - 3 года
    2. Инженер-технолог 2 категории - 5 лет
    3. Инженер-технолог 1 категории - 4 года
    4. Начальник цеха - 5 лет""")
    Post2 = Post(1, """1. ИНЖЕНЕР-КОНСТРУКТОР 3 категории
    2. ИНЖЕНЕР-КОНСТРУКТОР 2 категории
    3. ИНЖЕНЕР-КОНСТРУКТОР 1 категории
    4. ведущий ИНЖЕНЕР-КОНСТРУКТОР 
    5. главный (генеральный) ИНЖЕНЕР-КОНСТРУКТОР""")


    db = Database()
    db.MakeRequest("""CREATE TABLE IF NOT EXISTS Person
    (TELEPHONE TEXT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    TELEGRAMID TEXT,
    POST TEXT NOT NULL,
    POSTID INT NOT NULL,
    DATASTART DATE NOT NULL,
    SALARY INT NOT NULL,
    CITY TEXT NOT NULL,
    OFFICE TEXT NOT NULL,
    TALK BOOL NOT NULL); """)

    db.MakeRequest("""CREATE TABLE IF NOT EXISTS Post
    (ID INT PRIMARY KEY,
    LEVELS TEXT NOT NULL);""")

    db.MakeRequest("""CREATE TABLE IF NOT EXISTS Quests (
    ID INT PRIMARY KEY,
    QUEST jsonb);""")

    db.MakeRequest("""CREATE TABLE IF NOT EXISTS LEADERBOARD (
    PERSONID INT UNIQUE,
    QUESTID INT,
    SCORE INT,
    SHOW BOOL);""")

    db.AddData(Person1)
    db.AddData(Person2)
    db.AddData(Post1)
    db.AddData(Post2)

    db.Save()
