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

CREATE_TABLE_CLUB = """
CREATE TABLE club(
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