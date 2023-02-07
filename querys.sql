PRAGMA foreign_keys = ON; -- foreign_keys are not turned on in sqlite by default

-- student table
CREATE TABLE students(
    usn  TEXT PRIMARY KEY NOT NULL,
    name TEXT,
    phone INTEGER, 
    branch TEXT
);

-- faculties
CREATE TABLE faculties(
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT
); 

-- department level fines
CREATE TABLE department_fines(
    id INTEGER PRIMARY KEY NOT NULL,
    description TEXT,
    amount INTEGER
);

-- college level fines
CREATE TABLE college_fines(
    id INTEGER PRIMARY KEY NOT NULL,
    description TEXT,
    amount INTEGER
);

-- fines table
CREATE TABLE fines(
    id TEXT PRIMARY KEY,
    usn TEXT,
    date TEXT,
    paid BOOLEAN NOT NULL,
    fine_id INTEGER, 
    description TEXT,
    fined_by INTEGER, 
    FOREIGN KEY (usn) REFERENCES students(usn),
    FOREIGN KEY (fine_id) REFERENCES department_fines(id)
    , FOREIGN KEY (fine_id) REFERENCES college_fines(id),
    FOREIGN KEY (fined_by) REFERENCES faculties(id)
);

-----


CREATE TABLE fines(
     usn TEXT , 
     description TEXT, 
    FOREIGN KEY(usn) REFERENCES students(usn)
);

insert into students values("4PA20CS094", "RABEEH T A");
insert into fines values("4PA20CS094", "this is some big description about the thing");