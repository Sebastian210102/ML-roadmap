#Joins
SELECT e.fname, e.lname, d.name
FROM employee e
JOIN department d;

#We need to describe how the two tables are joined 
SELECT e.fname, e.lname, d.name
FROM employee e
JOIN department d
ON e.dept_id = d.dept_id;

#If the names of the columns useed to join are the same we caon use USING instead of the ON subcaluse
SELECT e.fname, e.lname, d.name
FROM employee e
JOIN department d
	USING(dept_id);
