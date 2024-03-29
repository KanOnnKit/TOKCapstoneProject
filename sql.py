CREATE_TABLE_STUDENT = """
    CREATE TABLE IF NOT EXISTS student(
        id INTEGER,
        name TEXT,
        age INTEGER,
        class_id INTEGER,
        year_enrolled INTEGER,
        graduating_year INTEGER,
        PRIMARY KEY(id),
        FOREIGN KEY(class_id) REFERENCES class(id)
    );
"""

CREATE_TABLE_CLASS = """
    CREATE TABLE IF NOT EXISTS class(
        id INTEGER,
        name TEXT,
        level TEXT,
        PRIMARY KEY(id)
    );
"""

CREATE_TABLE_SUBJECT = """
    CREATE TABLE IF NOT EXISTS subject(
        id INTEGER,
        name TEXT,
        level TEXT,
        PRIMARY KEY(id)
    );
"""

CREATE_TABLE_CCA = """
    CREATE TABLE IF NOT EXISTS cca(
        id INTEGER,
        name TEXT,
        PRIMARY KEY(id)
    );
"""

CREATE_TABLE_ACTIVITY = """
    CREATE TABLE IF NOT EXISTS activity(
        id INTEGER,
        name TEXT,
        start_date TEXT,
        end_date TEXT, 
        description TEXT,
        PRIMARY KEY(id)
    );
"""

CREATE_TABLE_STUDENTCCA = """
    CREATE TABLE IF NOT EXISTS studentcca(
        student_id INTEGER,
        cca_id INTEGER,
        role TEXT DEFAULT 'Member',
        PRIMARY KEY(student_id,cca_id),
        FOREIGN KEY(student_id) REFERENCES student(id),
        FOREIGN KEY(cca_id) REFERENCES cca(id)
    );
"""

CREATE_TABLE_STUDENTACTIVITY = """
    CREATE TABLE IF NOT EXISTS studentactivity(
        student_id INTEGER,
        activity_id INTEGER,
        category TEXT,
        role TEXT DEFAULT 'Member',
        award TEXT,
        hours INTEGER,
        PRIMARY KEY(student_id,activity_id),
        FOREIGN KEY(student_id) REFERENCES student(id),
        FOREIGN KEY(activity_id) REFERENCES activity(id)
    );
"""

CREATE_TABLE_STUDENTSUBJECT = """
    CREATE TABLE IF NOT EXISTS studentsubject(
        student_id INTEGER,
        subject_id INTEGER,
        PRIMARY KEY(student_id,subject_id),
        FOREIGN KEY(student_id) REFERENCES student(id),
        FOREIGN KEY(subject_id) REFERENCES subject(id)
    );
"""
