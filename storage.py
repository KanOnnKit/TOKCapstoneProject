import sqlite3

import sql

uri = "Database_for_capstone.db"

TABLES = {
    "student": ["id","Name","Age","Year_enrolled","Graduating_year"],
    "cca": ["id","Name"],
    "activity": ["id","Name","Start_date","End_date","Description"],
    "subject": ["id","Name","Level"],
    "class": ["id","Name","Class"],
    "studentcca": ["Student_id","Cca_id","Role"],
    "studentactivity": ["Student_id","Activity_id","Category","Role","Award","Hours"],
    "studentsubject": ["Student_id","Subject_id"],
}

def init(uri):    
    conn = sqlite3.connect(uri)
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
    conn = sqlite3.connect(uri)
    c = conn.cursor()
    c.execute(f'''
                  INSERT INTO {table_name} (Name,Age,Year_enrolled,Graduating_year)
                  VALUES(:Name,:Age,:Year_enrolled,:Graduating_year);
                  ''', (values))
    conn.commit()
    conn.close()
        
    
    
def remove_entry(table_name,primary_key):
    conn = sqlite3.connect(uri)
    c = conn.cursor()
    c.execute(f'''
              DELETE from {table_name}
              WHERE "id" = ?
              ''',(primary_key,))
    conn.commit()
    conn.close()
    
def remove_relation(junction_table, match): # match would contain Two diff types of id
    Flag = True
    for key in match.keys():
        if key not in TABLES[junction_table]:
            raise KeyError()
            Flag = False
    if Flag == True:
        conn = sqlite3.connect(uri)
        c = conn.cursor()
        c.execute('''
                  DELETE FROM {junction_table}
                  WHERE ? = ?
                  AND ? = ?;
                  ''', (TABLES[junction_table][0],match[TABLES[junction_table][0]],TABLES[junction_table][1],match[TABLES[junction_table][1]]))
        conn.commit()
        conn.close()


def edit_entry(table_name,primary_key: int, kwvalues: dict):
    conn = sqlite3.connect(uri)
    c = conn.cursor()
    for key,value in kwvalues.items():
        c.execute(f'''
                  UPDATE {table_name} SET
                  ? = ?
                  WHERE "id" = ?
                  ''', (key,value,primary_key))
        c.commit()
        c.execute()
        

def find_entry(table,primary_key): #returns entry
    outputdict = {}
    conn = sqlite3.connect(uri)
    c = conn.cursor()
    cursor = c.execute(f'''
              SELECT * FROM {table}
              WHERE "id" = ?;
              ''',(primary_key,))
    data = cursor.fetchall()

    for row in data:
        counter = 0
        for column in TABLES[table]:
                outputdict[column] = row[counter]
                counter+= 1
        
    conn.commit()
    conn.execute()

    return outputdict

def get_all_primary_keys(table_name):
    outputlist = []
    conn = sqlite3.connect(uri)
    c = conn.cursor()
    cursor = c.execute(f'''
              SELECT "id" FROM {table_name};
              ''')
    data = cursor.fetchall()
    for line in data:
        outputlist.append(line[0])
    conn.execute()
    return outputlist

def get_all_primary_keys_and_values(table_name,uri): #dictionary
    outputdict = {}
    conn = sqlite3.connect(uri)
    c = conn.cursor()
    cursor = c.execute(f'''
                       SELECT * FROM {table_name};
                       ''')
    data = cursor.fetchall()
    for line in data:
        counter = 0
        for column in TABLES[table_name]:
            outputdict[column] = line[counter]
            counter+= 1
    conn.execute()
    conn.commit()
    return outputdict

