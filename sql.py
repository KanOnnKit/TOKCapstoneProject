CREATE_TABLE_STUDENT = """
CREATE TABLE IF NOT EXISTS student(
    id INTEGER,
    Name TEXT,
    Age INTEGER,
    Class_id INTEGER,
    Year_enrolled INTEGER,
    Graduating_year INTEGER,
    PRIMARY KEY(id)
    FOREIGN KEY(class_id) REFERENCES class(id)
);"""

CREATE_TABLE_CLASS = """
CREATE TABLE IF NOT EXISTS class(
    id INTEGER,
    Name TEXT,
    Level TEXT,
    class_id INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(class_id) REFERENCES class(id)
);"""

CREATE_TABLE_SUBJECT = """
CREATE TABLE IF NOT EXISTS subject(
    id INTEGER,
    Name TEXT,
    Level TEXT,
    PRIMARY KEY(id)
);"""

CREATE_TABLE_CCA = """
CREATE TABLE IF NOT EXISTS cca(
    id INTEGER,
    Name TEXT,
    PRIMARY KEY(id)
);"""

CREATE_TABLE_ACTIVITY = """
CREATE TABLE IF NOT EXISTS activity(
    id INTEGER,
    Name TEXT,
    Start_date TEXT,
    End_date TEXT, 
    Description TEXT,
    PRIMARY KEY(id)
);"""

CREATE_TABLE_STUDENTCCA = """
CREATE TABLE IF NOT EXISTS studentcca(
Student_id INTEGER,
Cca_id INTEGER,
Role TEXT DEFAULT 'Member',
PRIMARY KEY(Student_id,Cca_id)
FOREIGN KEY(Student_id) REFERENCES student(id),
FOREIGN KEY(Cca_id) REFERENCES cca(id)
);
"""

CREATE_TABLE_STUDENTACTIVITY = """
CREATE TABLE IF NOT EXISTS studentactivity(
Student_id INTEGER,
Activity_id INTEGER,
Category TEXT,
Role TEXT DEFAULT 'Member',
Award TEXT,
Hours INTEGER,
PRIMARY KEY(Student_id,Activity_id)
FOREIGN KEY(Student_id) REFERENCES student(id),
FOREIGN KEY(Activity_id) REFERENCES activity(id)
);
"""

CREATE_TABLE_STUDENTSUBJECT = """
CREATE TABLE IF NOT EXISTS studentsubject(
Student_id INTEGER,
Subject_id INTEGER,
PRIMARY KEY(Student_id,Subject_id)
FOREIGN KEY(Student_id) REFERENCES student(id),
FOREIGN KEY(Subject_id) REFERENCES subject(id)
);
"""