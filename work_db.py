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
    db.commit()
    cursor.close()
    db.close()
    logger.info('Соединение с SQLite закрыто')


def create_table():
    db, cursor = connect_db()
    # запрос на создание таблицы пользователей
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                            id integer PRIMARY KEY NOT NULL,
                                            numbers_papers text
                                        ); """
    # запрос на создание таблицы записок
    sql_create_papers_table = """ CREATE TABLE IF NOT EXISTS papers (
                                                id integer PRIMARY KEY AUTOINCREMENT,
                                                text_paper text
                                            ); """
    if (db is not None) and (cursor is not None):
        try:
            cursor.execute(sql_create_users_table)
            cursor.execute(sql_create_papers_table)
            logger.info('Созданы таблица пользователей и таблица бумажек')

        except sqlite3.Error as error:
            logger.error(f'Ошибка при попытке создать таблицы - {error}')

        finally:
            close_db(db, cursor)


def check_id_users():
    db, cursor = connect_db()
    if (db is not None) and (cursor is not None):
        try:
            # Проверяем есть ли такой пользователь
            cursor.execute(f'SELECT id FROM users;')
            answer = cursor.fetchall()
            logger.info('Получены данные id из табл пользователей')
            return answer

        except sqlite3.Error as error:
            logger.error(f'Ошибка при попытке получить пользователей из табл - {error}')

        finally:
            close_db(db, cursor)
    pass


def add_user(user_id):
    db, cursor = connect_db()
    if (db is not None) and (cursor is not None):
        try:
            # запрос на добавление записи в табл пользователей
            sql_add_user = f'''
            INSERT INTO users(id)
            VALUES ({user_id})
            '''
            cursor.execute(sql_add_user)
            logger.info('Добавлен новый пользователь в табл')

        except sqlite3.Error as error:
            logger.error(f'Ошибка при попытке добавить пользователя в табл - {error}')

        finally:
            close_db(db, cursor)
