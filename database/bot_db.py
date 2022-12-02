import sqlite3
from random import choice


def create_sql():
    global db, cursor
    db = sqlite3.connect('mentorsGeekTech.sqlite3')
    cursor = db.cursor()

    if db:
        print('База данных подключена!')
    db.execute('''CREATE TABLE IF NOT EXISTS mentors_info
               (id INTEGER PRIMARY KEY ,
               mentor_name TEXT,
               mentor_number INTEGER ,
               mentor_group TEXT,
               mentor_age INTEGER,
               mentor_part TEXT,
               mentor_username TEXT)''')
    db.commit()


async def insert_sql(state):
    async with state.proxy() as data:
        cursor.execute('''INSERT INTO mentors_info
        VALUES (?,?,?,?,?,?,?)''', tuple(data.values()))
        db.commit()

 
async def random_sql(message):
    results = cursor.execute("SELECT * FROM mentors_info").fetchall()
    random_mentor = choice(results)
    await message.answer(f"Number: {random_mentor[2]}"
                         f"\nName: {random_mentor[1]}"
                         f"\nGroup: {random_mentor[3]}"
                         f"\nDepartment: {random_mentor[5]}"
                         f"\nAge: {random_mentor[4]}"
                         f"\nUsername: {random_mentor[6]}")


async def all_sql():
    return cursor.execute("SELECT * FROM mentors_info").fetchall()


async def delete_sql(mentor_id):
    cursor.execute("DELETE FROM mentors_info WHERE id = ? ", (mentor_id,))
    db.commit()


async def get_all_usernames():
    return cursor.execute("SELECT mentor_username FROM mentors_info").fetchall()
