import sqlite3

import sql

DB_URI = "Database_for_capstone.db"
TABLES = {
    "student": ["id", "name", "age", "class_id", "year_enrolled", "graduating_year"],
    "cca": ["id", "name"],
    "activity": ["id", "name", "start_date", "end_date", "description"],
    "subject": ["id", "name", "level"],
    "class": ["id", "name", "level"],
    "studentcca": ["student_id", "cca_id", "role"],
    "studentactivity": ["student_id", "activity_id", "category", "role", "award", "hours"],
    "studentsubject": ["student_id", "subject_id"],
}


def init_db():
    conn = sqlite3.connect(DB_URI)
    c = conn.cursor()
    c.execute(sql.CREATE_TABLE_STUDENT)
    c.execute(sql.CREATE_TABLE_CCA)
    c.execute(sql.CREATE_TABLE_ACTIVITY)
    c.execute(sql.CREATE_TABLE_SUBJECT)
    c.execute(sql.CREATE_TABLE_CLASS)
    c.execute(sql.CREATE_TABLE_STUDENTCCA)
    c.execute(sql.CREATE_TABLE_STUDENTACTIVITY)
    c.execute(sql.CREATE_TABLE_STUDENTSUBJECT)
    conn.commit()
    conn.close()


def add_entry(table_name, values):
    conn = sqlite3.connect(DB_URI)
    c = conn.cursor()
    data = []
    for col in TABLES[table_name][1:]:
        data.append(values[col])
    c.execute(
        f'''
            INSERT INTO {table_name} ({",".join(TABLES[table_name][1:])})
            VALUES({",".join(["?"] * (len(TABLES[table_name]) - 1))});
        ''',
        tuple(data)
    )
    conn.commit()
    conn.close()


def remove_entry(table_name, primary_key):
    conn = sqlite3.connect(DB_URI)
    c = conn.cursor()
    c.execute(
        f'''
            DELETE from {table_name}
            WHERE "id" = ?
        ''',
        (primary_key,)
    )
    conn.commit()
    conn.close()


def remove_relation(junction_table, match):  # match would contain Two diff types of id
    for key in match.keys():
        if key not in TABLES[junction_table]:
            raise KeyError(f"Key {key} not found in table {junction_table}")

    conn = sqlite3.connect(DB_URI)
    c = conn.cursor()
    c.execute(
        f'''
            DELETE FROM {junction_table}
            WHERE ({TABLES[junction_table][0]} = ? AND {TABLES[junction_table][1]} = ?);
        ''',
        (match[TABLES[junction_table][0]], match[TABLES[junction_table][1]])
    )
    conn.commit()
    conn.close()


def add_relation(junction_table, values):
    conn = sqlite3.connect(DB_URI)
    data = []
    for col in TABLES[junction_table]:
        data.append(values[col])
    c = conn.cursor()
    c.execute(
        f'''
            INSERT INTO {junction_table} ({",".join(TABLES[junction_table])})
            VALUES({",".join(["?"] * (len(TABLES[junction_table])))})
        ''',
        tuple(data)
    )
    conn.commit()
    conn.close()


def edit_entry(table_name, primary_key: int, kwvalues: dict):
    conn = sqlite3.connect(DB_URI)
    c = conn.cursor()
    for key, value in kwvalues.items():
        c.execute(
            f'''
                UPDATE {table_name} SET
                {key} = ?
                WHERE "id" = ?
            ''',
            (value, primary_key)
        )
    conn.commit()
    conn.close()


def find_entry(table, pk_column_name, primary_key):  # returns entry
    output_list = []
    conn = sqlite3.connect(DB_URI)
    c = conn.cursor()
    cursor = c.execute(
        f'''
            SELECT * FROM {table}
            WHERE {pk_column_name} = ?;
        ''',
        (primary_key,)
    )
    data = cursor.fetchall()

    for row in data:
        output_dict = {}
        counter = 0
        for column in TABLES[table]:
            output_dict[column] = row[counter]
            counter += 1
        output_list.append(output_dict)

    conn.commit()
    conn.close()

    return output_list


def get_all_primary_keys(table_name):
    output_list = []
    conn = sqlite3.connect(DB_URI)
    c = conn.cursor()
    cursor = c.execute(
        f'''
            SELECT "id" FROM {table_name};
        '''
    )
    data = cursor.fetchall()
    for line in data:
        output_list.append(line[0])
    conn.commit()
    conn.close()
    return output_list


def get_all_primary_keys_and_names(table_name):  # dictionary
    output_list = []
    conn = sqlite3.connect(DB_URI)
    c = conn.cursor()
    cursor = c.execute(
        f'''
        SELECT "id","name" FROM {table_name};
        '''
    )
    data = cursor.fetchall()
    for line in data:
        row_dict = {}
        counter = 0
        for column in ["id", "name"]:
            row_dict[column] = line[counter]
            counter += 1
        output_list.append(row_dict)
    conn.close()
    return output_list
