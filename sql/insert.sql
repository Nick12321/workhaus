INSERT INTO department VALUES (1, "Fine Arts");
INSERT INTO department VALUES (2, "English");
INSERT INTO department VALUES (3, "Computer Science");

INSERT INTO student VALUES (1, "Bob","123 Toronto st", "2000-01-01", 1);
INSERT INTO student VALUES (2, "Rob","402 Ontario St", "2000-04-22", 1);
INSERT INTO student VALUES (3, "Jina","23 William St.", "1999-10-02", 1);
INSERT INTO student VALUES (4, "Tisha","1015 Manitoba St.", "2001-02-08", 1);
INSERT INTO student VALUES (5, "Ali","12 Kingston Ave.", "2001-12-19", 1);

INSERT INTO course VALUES (1, "Intro to Arts", "X", "AB105", 1);
INSERT INTO course VALUES (2, "Modern Arts", "Y", "GS55", 1);
INSERT INTO course VALUES (3, "Intro to Drama", "Z", "AB501", 1);
INSERT INTO course VALUES (4, "English 101", "A", "BA103", 2);
INSERT INTO course VALUES (5, "Database 101", "B", "SF415", 3);


INSERT INTO student_course VALUES (1, 1, 1);
INSERT INTO student_course VALUES (2, 1, 2);
INSERT INTO student_course VALUES (3, 2, 1);
INSERT INTO student_course VALUES (4, 2, 2);
INSERT INTO student_course VALUES (5, 2, 3);
INSERT INTO student_course VALUES (6, 4, 5);
INSERT INTO student_course VALUES (7, 4, 4);
INSERT INTO student_course VALUES (8, 3, 3);
