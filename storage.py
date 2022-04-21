import sqlite3

import sql

url = ""

def init(url):    
    conn = sqlite3.connect(url)
    c = conn.cursor()
    c.execute(sql.CREATE_TABLE_STUDENT)
    conn.commit()
    conn.close()

def replace_relation(table_name, primary_key, foreign_key, new_foreign_key):
    conn = sqlite3.connect(url)
    c = conn.cursor()
    c.execute(f'''
          UPDATE {table_name} SET
          foreign_key = new_foreign_key,
          WHERE "student"."id" = primary_key;
          ''')
    conn.commit()
    conn.close()

def add_entry(**kwargs):
    conn = sqlite3.connect(url)
    c = conn.cursor()
    for key,value
    
    
def remove_entry(table_name,primary_key):
    conn = sqlite3.connect(url)
    c = conn.cursor()
    c.execute('''
              DELETE from "student"
              WHERE "student"."id" = ?
              ''',(primary_key,))
    conn.commit()
    conn.execute()
    
def remove_relation(junction_table, match):
    for key in match.keys():
        if key not in TABLES["StudentCCA"]:
            raise KeyError()
    conn = sqlite3.connect(url)
    c = conn.cursor()
    c.execute(f'''
              DELETE FROM {junction_tabe}
              WHERE Student_id = :student_id
              AND CCA_id = :cca_id;
              ''', match)


def edit_entry(primary_key: int, kwvalues: dict):
    conn = sqlite3.connect(url)
    c = conn.cursor()
    for key,value in kwvalues.items():
        c.execute('''
                  UPDATE "student" SET
                  ? = ?
                  WHERE "student"."id" = ?
                  ''', (key,value,primary_key))
        c.commit()
        c.execute()
        

def find_entry(primary_key):
    conn = sqlite3.connect(url)
    c = conn.cursor()
    c.execute('''
              SELECT "id" FROM "student"
              WHERE "id" = ?;
              ''',(primary_key,))

    conn.commit()
    conn.execute()

def get_all_primary_keys(self):
    conn = sqlite3.connect(url)
    c = conn.cursor()
    c.execute('''
              SELECT "id" FROM "STUDENT";
              ''')
    conn.execute()
    conn.commit()
    





