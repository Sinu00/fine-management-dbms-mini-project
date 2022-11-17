-- student table
CREATE TABLE students(
    usn  VARCHAR(10) PRIMARY KEY NOT NULL,
    name VARCHAR(100),
    phone CHAR(10), 
    branch CHAR(2)
);

-- faculties
CREATE TABLE faculties(
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(100)
) 

-- department level fines
CREATE TABLE department_fines(
    id INT PRIMARY KEY NOT NULL,
    description VARCHAR(100),
    amount INT
);

-- college level fines
CREATE TABLE college_fines(
    id INT PRIMARY KEY NOT NULL,
    description VARCHAR(100),
    amount INT
);

-- fines table
CREATE TABLE fines(
    id CHAR(21), PRIMARY KEY 
    usn CHAR(10),
    date CHAR(8),
    amount INT,
    paid BOOLEAN NOT NULL,
    fine_id INT, -- foreign key -> about the fine
    description TEXT,
    fined_by INT, -- foreign key -> of falculty fined
    FOREIGN KEY (fine_id) REFERENCES department_fines(id) REFERENCES college_fines(id),
    FOREIGN KEY (fined_by) REFERENCES faculties(id)
)