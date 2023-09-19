from loguru import logger
import sqlite3
import os


def create_db():
    try:
        # создание файла БД
        db = sqlite3.connect(os.getenv('NAME_DB'))
        cursor = db.cursor()
        logger.info('База данных создана и успешно подключена к SQLite')

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        cursor.fetchall()
        cursor.close()

    except sqlite3.Error as error:
        logger.error(f'Ошибка при подключении к sqlite - {error}')

    finally:
        if db:
            db.close()
            logger.info('Соединение с SQLite закрыто')


def connect_db():
    try:
        db = sqlite3.connect(os.getenv('NAME_DB'))
        cursor = db.cursor()
        logger.info('Соединение с SQLite открыто')
        return db, cursor

    except sqlite3.Error as error:
        logger.error(f'Ошибка при подключении к sqlite - {error}')
        return None, None


def close_db(db, cursor):
    cursor.close()
    db.close()
    logger.info('Соединение с SQLite закрыто')


def create_table():
    db, cursor = connect_db()

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                            id integer PRIMARY KEY,
                                            numbers_papers text
                                        ); """
    sql_create_papers_table = """ CREATE TABLE IF NOT EXISTS papers (
                                                id integer PRIMARY KEY,
                                                text_paper text
                                            ); """
    if (db is not None) and (cursor is not None):
        try:
            cursor.execute(sql_create_users_table)
            cursor.execute(sql_create_papers_table)
            logger.info('Созданы таблица пользователей и таблица бумажек')

        except sqlite3.Error as error:
            logger.error(f'Ошибка при попытке создать таблицы - {error}')
            return
        finally:
            close_db(db, cursor)

'''
def add_user(id_user):
    db, cursor = connect_db()
    if (db is not None) and (cursor is not None):
        try:
            # Проверяем есть ли такой пользователь
            cursor.execute(f'SELECT id FROM users;')
            is_users = cursor.fetchall()
'''
