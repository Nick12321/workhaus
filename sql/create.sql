--Department table in sqlite3
CREATE TABLE department (
	id int PRIMARY KEY,
	name varchar(30) UNIQUE
);

--Student table in sqlite3
CREATE TABLE student (
	id int PRIMARY KEY,
	name varchar(30),
	address varchar(200),
	dob varchar(19), --yyyy-MM-dd HH:mm:ss
	department_id int REFERENCES department(id)
);


--Course table in sqlite3
CREATE TABLE course (
	id int PRIMARY KEY,
	name varchar(30) UNIQUE,
	professor varchar(30),
	location varchar(5),
	department_id int,
	FOREIGN KEY(department_id) REFERENCES department(id) --long format example
);

CREATE TABLE student_course (
	student_course_id PRIMARY KEY,
	student_id int REFERENCES student(id),
	course_id int REFERENCES course(id)
);
