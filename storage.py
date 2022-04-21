import sqlite3

import sql

url = "https://replit.com/@KOH-HONG-LEE-LI/TOKCapstoneProject-3#Database_for_capstone.db"

TABLES = {
    "student": ["id","Name","Age","Year_enrolled","Graduating_year"],
    "cca": ["id","Name"]
    "activity": ["id","Name","Start_date","End_date","Description"]
    "subject": ["id","Name","Level"]
    "class": ["id","Name","Class"]
    "studentcca": ["Student_id","Cca_id"]
    "studentactivity": ["Student_id","Activity_id"]
    "studentsubject": ["Student_id","Subject_id"]
}
def init(url):    
    conn = sqlite3.connect(url)
    c = conn.cursor()
    c.execute(sql.CREATE_TABLE_STUDENT)
    c.execute(sql.CREATE_TABLE_CCA)
    c.execute(sql.CREATE_TABLE_ACTIVITY)
    c.execute(sql.CREATE_TABLE_SUBJECT)
    c.execute(sql.CREATE_TABLE_CLASS)
    conn.commit()
    c.execute(sql.CREATE_TABLE_STUDENTCCA)
    c.execute(sql.CREATE_TABLE_STUDENTACTIVITY)
    c.execute(sql.CREATE_TABLE_STUDENTSUBJECT)
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
    
def remove_relation(junction_table, match): # match would contain Two diff types of id
    for key in match.keys():
        if key not in TABLES[junction_table]:
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
    





