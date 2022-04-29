import sqlite3

import sql

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

uri = "Database_for_capstone.db"

TABLES = {
    "student": ["id","Name","Age","Year_enrolled","Graduating_year","class_id"],
    "cca": ["id","Name"],
    "activity": ["id","Name","Start_date","End_date","Description"],
    "subject": ["id","Name","Level"],
    "class": ["id","Name","Class"],
    "studentcca": ["Student_id","Cca_id","Role"],
    "studentactivity": ["Student_id","Activity_id","Category","Role","Award","Hours"],
    "studentsubject": ["Student_id","Subject_id"],
}

def init():    
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
    data = []
    for col in TABLES[table_name][1:]:
        data.append(values[col])
    c.execute(f'''
                  INSERT INTO {table_name} ({",".join(TABLES[table_name][1:])})
                  VALUES({",".join(["?"]*(len(TABLES[table_name])-1))});
                  ''', (tuple(data)))
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
            Flag = False
            raise KeyError()
    if Flag == True:
        conn = sqlite3.connect(uri)
        conn.set_trace_callback(print)
        c = conn.cursor()
        print((TABLES[junction_table][0],match[TABLES[junction_table][0]],TABLES[junction_table][1],match[TABLES[junction_table][1]]))
        c.execute(f'''
                  DELETE FROM {junction_table}
                  WHERE ({TABLES[junction_table][0]} = ? AND {TABLES[junction_table][1]} = ?);
                  ''', (match[TABLES[junction_table][0]],match[TABLES[junction_table][1]]))
        conn.commit()
        conn.close()


def add_relation(junction_table,values):
    conn = sqlite3.connect(uri)
    data = []
    for col in TABLES[junction_table]:
        data.append(values[col])
    c = conn.cursor()
    c.execute(f'''
INSERT INTO {junction_table} ({",".join(TABLES[junction_table])})
VALUES({",".join(["?"]*(len(TABLES[junction_table])))})
''',(tuple(data)))
    conn.commit()
    conn.close()

    
def edit_entry(table_name,primary_key: int, kwvalues: dict):
    conn = sqlite3.connect(uri)
    c = conn.cursor()
    for key,value in kwvalues.items():
        c.execute(f'''
                  UPDATE {table_name} SET
                  {key} = ?
                  WHERE "id" = ?
                  ''', (value,primary_key))
    conn.commit()
    conn.close()
        

def find_entry(table,primary_key,pk_columnname): #returns entry
    outputdict = {}
    conn = sqlite3.connect(uri)
    c = conn.cursor()
    cursor = c.execute(f'''
              SELECT * FROM {table}
              WHERE {pk_columnname} = ?;
              ''',(primary_key,))
    data = cursor.fetchall()

    for row in data:
        counter = 0
        for column in TABLES[table][1:]:
                outputdict[column] = row[counter]
                counter+= 1
        
    conn.commit()
    conn.close()

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
    conn.commit()
    conn.close()
    return outputlist

def get_all_primary_keys_and_values(table_name): #dictionary
    outputlist = []
    outputdict = {}
    conn = sqlite3.connect(uri)
    c = conn.cursor()
    cursor = c.execute(f'''
                       SELECT * FROM {table_name};
                       ''')
    data = cursor.fetchall()
    print(data)
    for line in data:
        counter = 0
        for column in TABLES[table_name][1:]:
            outputdict[column] = line[counter]
            counter+= 1
        outputlist.append(outputdict)
    conn.commit()
    conn.close()
    return outputlist

