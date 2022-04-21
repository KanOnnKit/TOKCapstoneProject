CREATE_TABLE_STUDENT = """
CREATE TABLE student(
    id INTEGER,
    Name TEXT,
    Age TEXT,
    Year_enrolled TEXT,
    Graduating_year TEXT,
    PRIMARY KEY(id)
);"""

CREATE_TABLE_CLASS = """
CREATE TABLE class(
    id INTEGER,
    Name TEXT,
    Level TEXT,
    PRIMARY KEY(id)
);"""

CREATE_TABLE_SUBJECT = """
CREATE TABLE subject(
    id INTEGER,
    Name TEXT,
    Level TEXT,
    PRIMARY KEY(id)
);"""

CREATE_TABLE_CCA = """
CREATE TABLE cca(
    id INTEGER,
    Name TEXT,
    PRIMARY KEY(id)
);"""

CREATE_TABLE_ACTIVITY = """
CREATE TABLE class(
    id INTEGER,
    Name TEXT,
    Start_date TEXT,
    End_date TEXT, 
    Description TEXT,
    PRIMARY KEY(id)
);"""

CREATE_TABLE_STUDENTcca = """
CREATE TABLE studentcca(
Student_id INTEGER,
Cca_id INTEGER,
PRIMARY KEY(Student_id,Cca_id)
FOREIGN KEY(Student_id) REFERENCES student(id),
FOREIGN KEY(Cca_id) REFERENCES cca(id)
);
"""

CREATE_TABLE_STUDENTACTIVITY = """
CREATE TABLE studentactivity(
Student_id INTEGER,
Activity_id INTEGER,
PRIMARY KEY(Student_id,Activity_id)
FOREIGN KEY(Student_id) REFERENCES student(id),
FOREIGN KEY(Activity_id) REFERENCES activity(id)
);
"""

CREATE_TABLE_STUDENTSUBJECT = """
CREATE TABLE studentsubject(
Student_id INTEGER,
Subject_id INTEGER,
PRIMARY KEY(Student_id,Subject_id)
FOREIGN KEY(Student_id) REFERENCES student(id),
FOREIGN KEY(Subject_id) REFERENCES subject(id)
);
"""

INSERT_STUDENT = """
INSERT INTO student (Name, CT_class, CT_tutor)
VALUES (:Name, :CT_class, :CT_tutor);
"""

FIND_STUDENT_BY_NAME = """
SELECT Name, CT_class, CT_tutor
FROM student
WHERE Name = ?;"""

UPDATE_STUDENT_BY_NAME = """
UPDATE student SET
    CT_class = :CT_class,
    CT_tutor = :CT_tutor
WHERE Name = :Name;"""

DELETE_STUDENT_BY_NAME = """
DELETE FROM student
WHERE Name = ?;"""
...