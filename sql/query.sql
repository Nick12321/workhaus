SELECT s.id, s.name, c.name
FROM student as s, course as c, student_course as sc
WHERE s.id = sc.student_id AND c.id = sc.course_id;
