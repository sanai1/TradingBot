import sqlite3


class DBHeper:
    def __init__(self, db_file):
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()

    def get_name_sector(self):
        # получение названий секторов
        command = "select sector from info_stocks"
        '''
        # создание БД
        self.cursor.execute('create table info_stocks (
            sector text,
            name text,
            P_E integer )')
        
        # запросы для тестирования
        insert into info_stocks (sector, name, P_E) values ('Нефть/Газ', 'Татнефть', 8);
        insert into info_stocks (sector, name, P_E) values ('Металы и добыча', 'Распадская', 8);
        insert into info_stocks (sector, name, P_E) values ('Продовольствие', 'Белуга Групп', 6);
        insert into info_stocks (sector, name, P_E) values ('Строительство', 'ЛСР', 9);
        insert into info_stocks (sector, name, P_E) values ('Розничная торговля', 'Черкизово', 5);
        '''
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def get_name_stocks(self, name_sector):
        # получение названий компаний по названию сектора
        command = "select name from info_stocks where sector='" + name_sector + "'"
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def set_info(self, mas_info):
        # заполнение инфой с сайта
        command = "insert into info_stocks values ()" # желательно разобраться как заполнять БД массивом, не выполняя запрос циклом
        # TODO: создать метод заполнения БД инфой с сайта ДОХОДЪ (далее будем смотреть другие сайты)

    def close(self):
        self.connect.close()