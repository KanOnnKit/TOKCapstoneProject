import sqlite3

import sql

url = "https://replit.com/@KOH-HONG-LEE-LI/TOKCapstoneProject-3#Database_for_capstone.db"

TABLES = {
    "student": ["id","Name","Age","Year_enrolled","Graduating_year"],
    "cca": ["id","Name"]
    "activity": ["id","Name","Start_date","End_date","Description"]
    "subject": ["id","Name","Level"]
    "class": ["id","Name","Class"]
    "studentcca": ["Student_id","Cca_id","Role"]
    "studentactivity": ["Student_id","Activity_id","Category","Role","Award","Hours"]
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

def add_entry(table_name,values):
    conn = sqlite3.connect(url)
    c = conn.cursor()
    for key,value in values:
        c.execute(f'''
                  INSERT INTO {table_name}(
                  ?)
                  VALUES(?)
                  '''(key,values);)
        
    
    
def remove_entry(table_name,primary_key):
    conn = sqlite3.connect(url)
    c = conn.cursor()
    c.execute(f'''
              DELETE from {table_name}
              WHERE "id" = ?
              ''',(primary_key,))
    conn.commit()
    conn.execute()
    
def remove_relation(junction_table, match): # match would contain Two diff types of id
    Flag = True
    for key in match.keys():
        if key not in TABLES[junction_table]:
            raise KeyError()
            Flag = False
    if Flag = True:
        conn = sqlite3.connect(url)
        c = conn.cursor()
        c.execute('''
                  DELETE FROM {junction_table}
                  WHERE ? = ?
                  AND ? = ?;
                  ''', (TABLES[junction_table][0],match[TABLES[junction_table][0]],TABLES[junction_table][1],match[TABLES[junction_table][1]]))


def edit_entry(table_name,primary_key: int, kwvalues: dict):
    conn = sqlite3.connect(url)
    c = conn.cursor()
    for key,value in kwvalues.items():
        c.execute(f'''
                  UPDATE {table_name} SET
                  ? = ?
                  WHERE "id" = ?
                  ''', (key,value,primary_key))
        c.commit()
        c.execute()
        

def find_entry(table,primary_key):
    conn = sqlite3.connect(url)
    c = conn.cursor()
    cursor = c.execute(f'''
              SELECT "id" FROM {table}
              WHERE "id" = ?;
              ''',(primary_key,))
    data = cursor.fetchall()

    for row in data:
        counter = 0
        for column in TABlES[table]:
            print(f'{column}:, {row[counter]}')
            counter+= 1
    conn.commit()
    conn.execute()

def get_all_primary_keys(table_name):
    conn = sqlite3.connect(url)
    c = conn.cursor()
    cursor = c.execute(f'''
              SELECT "id" FROM {table_name};
              ''')
    data = cursor.fetchall()
    for line in data:
        print(line[0])
    conn.execute()
    conn.commit()

def get_all_primary_keys_and_values(table_name):
    conn = sqlite3.connect(url)
    c = conn.cursor()
    cursor = c.execute(f'''
                       SELECT * FROM {table_name};
                       ''')
    data = cursor.fetchall()
    for line in data:
        counter = 0
        for column in TABlES[table]:
            print(f'{column}:, {row[counter]}')
            counter+= 1
    conn.execute()
    conn.commit()
    
        
        
    





