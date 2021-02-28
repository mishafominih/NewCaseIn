from Database import Person, Database
from datetime import date


def init():
    Person1 = Person(89045461183, 'Завьялов Артём Борисович', 'ВЕДУЩИЙ ИНЖЕНЕР-КОНСТРУКТОР', date(28, 2, 21),
                     57000, 'Санкт-Петербург', 'АО «Центральное конструкторское бюро машиностроения»', False)
    Person2 = Person(89502073539, 'Чебыкина Юлия Владимировна', 'ИНЖЕНЕР-ТЕХНОЛОГ 3 КАТЕГОРИИ', date(12, 7, 20),
                     70000, 'Санкт-Петербург', 'АО «Центральное конструкторское бюро машиностроения»', False)

    db = Database()
    db.MakeRequest("""CREATE TABLE IF NOT EXISTS Person
    (TELEPHONE TEXT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    POST TEXT NOT NULL,
    DATASTART DATE NOT NULL,
    SALARY INT NOT NULL,
    CITY TEXT NOT NULL,
    OFFICE TEXT NOT NULL,
    TALK BOOL NOT NULL); """)

    db.MakeRequest("""CREATE TABLE IF NOT EXISTS Post
    (NAME TEXT NOT NULL,
    LEVELS TEXT NOT NULL);""")

    db.AddData(Person1)
    db.AddData(Person2)
    db.Save()
