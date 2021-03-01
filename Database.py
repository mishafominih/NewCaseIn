import psycopg2
from datetime import date


class Base:
    TableName: str

    def __str__(self):
        return None


class Person(Base):
    TableName = "Person"

    def __init__(self, Telephone: int, Name: str, TelegramId:int, Post: str, PostId: int, DataStart: date,
                 Salary: int, City: str, Office: str, Talk: bool):
        self.TELEPHONE = Telephone
        self.NAME = Name
        self.TELEGRAMID = TelegramId
        self.POST = Post
        self.POSTID = PostId
        self.DATASTART = DataStart
        self.SALARY = Salary
        self.CITY = City
        self.OFFICE = Office
        self.TALK = Talk

    def __str__(self):
        return f"{self.TELEPHONE}, '{self.NAME}', '{self.TELEGRAMID}', '{self.POST}', '{self.POSTID}', '{self.DATASTART}'," \
               f" {self.SALARY}, '{self.CITY}', '{self.OFFICE}', '{self.TALK}'"


class Post(Base):
    TableName = "Post"
    def __init__(self, Id:int, level:str):
        self.ID = Id
        self.LEVELS = level

    def __str__(self):
        return f"'{self.ID}', '{self.LEVELS}'"


class Record(Base):
    TableName = 'Leaderboard'
    def __init__(self, PersonId: int, QuestId: int, Score: int, Show: bool):
        self.PERSONID = PersonId,
        self.QUESTID = QuestId,
        self.SCORE = Score,
        self.SHOW = Show
    def __str__(self):
        return f"{self.PERSONID}, '{self.QUESTID}', '{self.SCORE}', '{self.SHOW}'"


class Database:

    def __init__(self):
        DATABASE_URL = "postgres://nfyacexnxvpjkx:ad1f5d141c7e2274f31f5d354834bd2fcfb6e86e7a6bb3e" \
                       "c84001990d2dda6e9@ec2-99-80-200-225.eu-west-1.compute.amazonaws.com:5432" \
                       "/daco8ehnjpa65j"
        self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        self.cur = self.conn.cursor()

    # основная функция.
    def MakeRequest(self, request: str):
        self.cur.execute(request)
        try:
            return self.cur.fetchall()
        except:
            return None

    def AddData(self, base: Base):
        self.MakeRequest(f'''INSERT INTO {base.TableName} VALUES ({base.__str__()}) ON CONFLICT DO NOTHING;''')

    def GetAllData(self, tableName: str):
        return self.MakeRequest("SELECT * FROM " + tableName)

    def Save(self):
        self.conn.commit()

    def __del__(self):
        self.conn.close()