#!/usr/bin/env python
# coding: utf-8

# # QUESTIONS
# 
# With the aid of the data provided in the notepad file here, write SQL queries with sqlite that perform the following:
# 
# 1. Create a table named “employee” with columns as:
# 
# (a) Employee_id (int): Make it the primary key
# 
# (b) Last_name 
# 
# (c) First_name
# 
# (d) Position
# 
# (e) Salary
# 
# (f) date_hired
# 
# 2. Write a query to get the ‘unique’ Position from employee table
# 3. Write a query to get all employee details from the employee table, order by first_name, in descending order.
# 4. Write a query that returns employees’ first_name, last_name and salary, for salary greater than 200,000.
# 5. One of the employees whose first_name was RUDA got married and changed her last_name to Peter, write a query to effect this change on her last name, thereafter, write a query that returns all her details to enable you view the change made to her name.
# 6. One of the employees with last_name ‘KWAME’ left the organization for another job, write a query that removes his name from the database. View the whole table by writing another query to verify the change that was made to the employee.
# 7. Write a query that renames the column “Position” to “job_role”
# 8. Write a query to get the employee_id, (first_name, last_name), salary in ascending order of salary. Alias the first_name and last_name as “Name”.
# 9. Write a query that gives the count of employees whose salaries are greater than 200,000. [Hint: Use the “COUNT” clause]
# 10. Write a query to get the maximum and minimum salary from the employees table. [Hint: Use the MAX, MIN functions]
# 

# # SOLUTION TO THE QUESTIONS

# In[1]:


# Import sqlite3
import sqlite3

# Create a connection to a database
conn = sqlite3.connect("student.db")

# Create a cursor to execute sql
cursor = conn.cursor()

# Creating a table named employee
sql = """
CREATE TABLE employee(employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
last_name text,
first_name text,
position text,
salary INTEGER,
date_hired INTEGER
);
"""


# # Executing the sql
cursor.execute(sql)

# Output the query
result = cursor.fetchall()
result

print("Employee table created succefully")


# In[3]:


# Getting the unique Position from employee table
sql = """
CREATE TABLE employee(
employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
last_name text,
first_name text,
position text,
salary INTEGER,
date_hired INTEGER,
UNIQUE (position)
);
"""


# Executing the sql
cursor.execute(sql)


# In[8]:


# Adding the list
employee_list = [
(1,"Lew","Allen","City Administrator",295000,2004),
(2,"Sessoms","Allen","President",295000,2008),
(3,"HENDERSON","KAYATANYA","Superintendent Of Schools",275000,2007),
(4,"Lanier","Cathy","Chief",230743,1990),
(5,"Arons","Bernard","Medical Officer Psych",206000,2008),
(6,"Ritchie","Elspeth","Medical Officer Psych",206000,2010),
(7,"GRAY","VINCENT","Mayor",200000,2005),
(8,"Marshall","Katherine","Medical Officer Psych",200000,2008),
(9,"Gandhi","Natwar","Chief Financial Officer",199700,1997),
(10,"DUNCAN","LORETTA","Workers Compensation Recipient",197808,1984),
(11,"Baxter","Graeme","Act Provost & Vp Acd Aff",196257,2008),
(12,"Miramontes","David","Medical Director",193125,2011),
(13,"Graves","Warren","Chief Of Staff",193125,2011),
(14,"Stanchfield","Eric","Executive Director",193125,2007),
(15,"Jones","Tyler","Medical Officer Psych",190550,2008),
(16,"BROWN","KWAME","Chairman",190000,2005),
(17,"Eure","Philip","Executive Director",188692,2000),
(18,"Cooper","Ginnie","Executive Director",188044,2006),
(19,"Yadao","Nilda","Medical Officer (psychiatry)",188027,1987),
(20,"Ellerbe","Kenneth","Fire Chief",187302,2003),
(21,"Ruland","Jeffrey","Dir Of The Ctr For Wf Str & Ec",186911,2009),
(22,"Parker","Craig","General Counsel",186911,2009),
(23,"Farley","Mark","Vp, Human Resources",186911,2008),
(24,"Otero","Beatriz","Dep Mayor For Hlth & Hum Svcs",185000,2011),
(25,"Quander","Paul","Deputy Mayor",185000,2009),
(26,"Pierre","Louis","Chief Medical Examiner",185000,1985),
(27,"Pestaner","Joseph","Medical Officer (medical Exami)",183892,1997),
(28,"Revercomb","Carolyn","Medical Officer (medical Exami)",183892,2005),
(29,"Morgan","Johnson","Chief Investment Officer",183677,1991),
(30,"Williamson","Michael","Deputy Director",182000,2011),
(31,"White","Mattie","Medical Officer (psychiatry)",180604,1989),
(32,"Park","Kyung","Medical Officer (psychiatry)",180604,1987),
(33,"Gore","T","Medical Officer (psychiatry)",172101,2005),
(34,"LUDWIG","BENJAMIN","Workers Compensation Recipient",171517,1972),
(35,"Atdjian","Sylvia","Medical Officer (psychiatry)",170938,2007),
(36,"Zaidi","Syed","Medical Officer (psychiatry)",170344,2005),
(37,"Sherron","Robert","Medical Officer (psychiatry)",170344,1991),
(38,"Johnson","Nicole","Medical Officer (psychiatry)",170344,2007),
(39,"RUDA","LISA","Chief Of Staff",170000,2007),
(40,"Beers","Nathaniel","Deputy Superintendent",170000,2007),
(41,"Nuss","Laura","Director",170000,2007),
(42,"Mancini","Robert","Acting Director",170000,2004),
(43,"Wicker","Henry","Medical Officer Opthal",168378,1987),
(44,"Davenport","Nancy","Administrative Librarian",167200,2006),
(45,"Jaji","Abayomi","Medical Officer (psychiatry)",167062,2000),
(46,"Stevens","KyleeAnn","Medical Officer (psychiatry)",167051,2008),
(47,"Smothers","Kenneth","Medical Officer (psychiatry)",166995,1987),
(48,"Akhtar","Saleha","Medical Officer (psychiatry)",166995,1988),
(49,"Singh","Anjali","Medical Officer (psychiatry)",166370,1999),
(50,"Rahman","Umar","Medical Officer (psychiatry)",166370,1996),
(51,"Adewale","Benjamin","Medical Officer (psychiatry)",166370,1988),
(52,"Zaidi","Syed","Medical Officer General Practi",165842,1983),
(53,"Jackson","Kenneth","Assistant Fire Chief Srvs",165306,1982),
(54,"Berns","David","Dir Of Human Services",165200,2011),
(55,"Cordi","Stephen","Deputy Cfo Otr",165162,2008),
(56,"Mallory","Lisa","Acting Director",165000,2004),
(57,"Flowers","Brian","General Counsel",165000,1985),
(58,"Bellamy","Terry","Director",165000,2008),
(59,"West","Millicent","Director Homeland Sec & Ema",165000,2003),
(60,"Pappas","Gregory","Deputy Dir",164800,2011),
(61,"Altaf","Samia","Supervisor Medical Officer",164800,2010),
(62,"Owens","Karen","Dental Officer",164800,1989),

]

# SQL
sql = """ 
INSERT INTO employee VALUES(?,?,?,?,?,?)
"""
 
# Executing sql
cursor.executemany(sql, employee_list)
print("We have inserted", cursor.rowcount,"records to the table")


# In[9]:


# Viewing the employee table
sql = """
SELECT employee_id, last_name, first_name, position, salary, date_hired
FROM employee
"""
cursor.execute(sql)

result = cursor.fetchall()
result


# In[10]:


# Getting employee details from the employee table, order by first_name, in descending order.
sql = """ 
SELECT * FROM employee
ORDER BY first_name DESC;
"""

cursor.execute(sql)

result = cursor.fetchall()
result


# In[11]:


# Returning employees’ first_name, last_name and salary, for salary greater than 200,000.

sql = """
SELECT * FROM employee
WHERE salary >= 200000
"""

cursor.execute(sql)

result = cursor.fetchall()
result


# In[12]:


# Updating the table in the database
sql = """
UPDATE employee
SET last_name = "PETER"
WHERE rowid = 39
"""

cursor.execute(sql)

result = cursor.fetchall()
result
print("Name was succefully changed")


# In[13]:


# Viewing the employee table
sql = """
SELECT employee_id, last_name, first_name, position, salary, date_hired
FROM employee
"""
cursor.execute(sql)

result = cursor.fetchall()
result


# In[14]:


sql = """
DELETE 
FROM employee
WHERE employee_id = 16;
"""

cursor.execute(sql)
result = cursor.fetchall()
result


# In[15]:


# Viewing the employee table
sql = """
SELECT employee_id, last_name, first_name, position, salary, date_hired
FROM employee
"""
cursor.execute(sql)

result = cursor.fetchall()
result


# In[19]:


# Renaming the column Position to job_role
sql = """
ALTER TABLE employee
RENAME position TO job_role

"""
cursor.execute(sql)
result = cursor.fetchall()
result


# In[24]:


# Alias the first name and last name as Name.
sql = """ 
SELECT (first_name 
AND last_name) 
AS name
FROM employee
"""

# Executing sql
cursor.execute(sql)
result = cursor.fetchall()
result


# In[25]:


# Counting of employees whose salaries are greater than 200,000.
sql = """ 
SELECT COUNT(employee_id)
FROM employee
WHERE salary >= 200000
"""

cursor.execute(sql)
result = cursor.fetchall()
result


# In[26]:


# Getting the minimum salary from the table
sql = """ 
SELECT MIN(salary)
FROM employee
"""

cursor.execute(sql)
result = cursor.fetchall()
result


# In[27]:


# Getting the maximum salary from the table
sql = """ 
SELECT MAX(salary)
FROM employee
"""

cursor.execute(sql)
result = cursor.fetchall()
result

