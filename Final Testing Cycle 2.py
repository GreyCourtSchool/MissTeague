Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> writeSQL()
SELECT* FROM lessonTable
(1, 'T1', 2, '18/2/19', '20:30', 'g')
(2, 'T1', 2, '18/2/19', '20:30', 'g')
(3, 'T1', 21, '24/08/18', '1652', 'R')
(4, 'T1', 31, '24/08/18', '1652', 'R')
(5, 'T1', 24, '24/08/18', '1652', 'R')
(6, 'T1', 1, '24/08/18', '1652', 'R')
(7, 'T1', 21, '24/08/18', '1652', 'R')
(8, 'T1', 31, '24/08/18', '1652', 'R')
>>> SELECT * FROM classroomTable
SyntaxError: invalid syntax
>>> writeSQL()
SELECT * FROM classroomtable
('T1', '0,1', '0,2', '0,3', '0,4', '0,5', '0,6', '0,7', '3,7', '3,6', '3,5', '3,4', '3,3', '3,2', '3,1', '3,0', '4,0', '4,1', '4,2', '4,3', '4,4', '4,5', '4,6', '4,7', '7,7', '7,6', '7,5', '7,4', '7,3', '7,2', '7,1', '7,0', 'null')
>>> TD7
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    TD7
NameError: name 'TD7' is not defined
>>> setClass()
***Existing Classes***
('8 Beech',)
('8 beech',)
From the list above, type the class you want to choose
>
Your new class will now be added
[]

>>> writeSQL()
DELETE FROM lessonTable WHERE lessonID=1
>>> writeSQL()
SELECT * FROM lessonTable
(2, 'T1', 2, '18/2/19', '20:30', 'g')
(3, 'T1', 21, '24/08/18', '1652', 'R')
(4, 'T1', 31, '24/08/18', '1652', 'R')
(5, 'T1', 24, '24/08/18', '1652', 'R')
(6, 'T1', 1, '24/08/18', '1652', 'R')
(7, 'T1', 21, '24/08/18', '1652', 'R')
(8, 'T1', 31, '24/08/18', '1652', 'R')
>>> writeSQL()
SELECT * FROM classTable
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    writeSQL()
  File "/home/pi/Desktop/Testing Database.py", line 85, in writeSQL
    cursor.execute(sql)
sqlite3.OperationalError: no such table: classTable
>>> writeSQL()
SELECT * FROM lessonTable
(2, 'T1', 2, '18/2/19', '20:30', 'g')
(3, 'T1', 21, '24/08/18', '1652', 'R')
(4, 'T1', 31, '24/08/18', '1652', 'R')
(5, 'T1', 24, '24/08/18', '1652', 'R')
(6, 'T1', 1, '24/08/18', '1652', 'R')
(7, 'T1', 21, '24/08/18', '1652', 'R')
(8, 'T1', 31, '24/08/18', '1652', 'R')
>>> writeSQL()
SELECT * FROM classesTable
(0, 0, 'T1', '8 Beech')
(2, 0, 'T1', '8 beech')
(3, 0, 'T1', '')
>>> writeSQL()
DELETE FROM classesTable WHERE classID>0
>>> writeSQL()
SELECT * FROM classesTable
(0, 0, 'T1', '8 Beech')
>>> setClass()
***Existing Classes***
('8 Beech',)
From the list above, type the class you want to choose
>8 Beech
[(0,)]
0
>>> TD9
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    TD9
NameError: name 'TD9' is not defined
>>> setClass()
***Existing Classes***
('8 Beech',)
From the list above, type the class you want to choose
>8bC
Your new class will now be added
[]
8bC
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
('8 Beech',)
('8bC',)
From the list above, type the class you want to choose
>8bC
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    setClass()
  File "/home/pi/Desktop/Testing Database.py", line 63, in setClass
    currentClass = getClass(generateDatabase(),currentClass)
  File "/home/pi/Desktop/Testing Database.py", line 70, in getClass
    cursor.execute(sql)
NameError: name 'cursor' is not defined
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
('8 Beech',)
('8bC',)
From the list above, type the class you want to choose
>8bC
4
>>> setClass()
***Existing Classes***
('8 Beech',)
('8bC',)
From the list above, type the class you want to choose
>8 beech
Your new class will now be added
Your new class will now be added
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    setClass()
  File "/home/pi/Desktop/Testing Database.py", line 63, in setClass
    currentClass = getClass(generateDatabase(),currentClass)
  File "/home/pi/Desktop/Testing Database.py", line 80, in getClass
    getClass(database,currentClass)
  File "/home/pi/Desktop/Testing Database.py", line 79, in getClass
    cursor.execute(sql)
sqlite3.OperationalError: database is locked
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
('8 Beech',)
('8bC',)
From the list above, type the class you want to choose
>8 beech
Your new class will now be added
Your new class will now be added
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    setClass()
  File "/home/pi/Desktop/Testing Database.py", line 63, in setClass
    currentClass = getClass(generateDatabase(),currentClass)
  File "/home/pi/Desktop/Testing Database.py", line 80, in getClass
    getClass(database,currentClass)
  File "/home/pi/Desktop/Testing Database.py", line 79, in getClass
    cursor.execute(sql)
sqlite3.OperationalError: database is locked
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setCass()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    setCass()
NameError: name 'setCass' is not defined
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
('8 Beech',)
('8bC',)
From the list above, type the class you want to choose
>8 beech
Your new class will now be added
8 beech
>>> writeSQL()
SELECT * FROM classesTable
(0, 0, 'T1', '8 Beech')
(4, 0, 'T1', '8bC')
(5, 0, 'T1', '8 beech')
>>> writeSQL()
DELETE FROM classesTable where classID=5
>>> writeSQL()
SELECT * FROM classesTable
(0, 0, 'T1', '8 Beech')
(4, 0, 'T1', '8bC')
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
('8 Beech',)
('8bC',)
From the list above, type the class you want to choose
>8 beech
Your new class will now be added
8 beech
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
('8 Beech',)
('8bC',)
('8 beech',)
From the list above, type the class you want to choose
>8 beech
'8 Beech'
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
('8 Beech',)
('8bC',)
('8 beech',)
From the list above, type the class you want to choose
>8 beech
'8 Beech'
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
('8 Beech',)
('8bC',)
('8 beech',)
From the list above, type the class you want to choose
>8 beech
'8 Beech'
>>> writeSQL()
SELECT * FROM classesTable
(0, 0, 'T1', '8 Beech')
(4, 0, 'T1', '8bC')
(6, 0, 'T1', '8 beech')
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
('8 Beech',)
('8bC',)
('8 beech',)
From the list above, type the class you want to choose
>8bc
[]
Your new class will now be added
[]
[('8 Beech',), ('8bC',), ('8 beech',)]
[]
>>> writeSQL()
SELECT * FROM classesTable
(0, 0, 'T1', '8 Beech')
(4, 0, 'T1', '8bC')
(6, 0, 'T1', '8 beech')
(7, 0, 'T1', '8bc')
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setclass()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    setclass()
NameError: name 'setclass' is not defined
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
('8 Beech',)
('8bC',)
('8 beech',)
('8bc',)
From the list above, type the class you want to choose
>8bc
[(4,), (7,)]
'8 Beech'
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
()
()
()
()
From the list above, type the class you want to choose
>
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
 Bee

 bee

From the list above, type the class you want to choose
>
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
8 Beech
8bC
8 beech
8bc
From the list above, type the class you want to choose
>
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> 
>>> setClass()
***Existing Classes***
 - 8 Beech
 - 8bC
 - 8 beech
 - 8bc
From the list above, type the class you want to choose
>8bC
[(4,), (7,)]
'8 Beech'
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
 - 8 Beech
 - 8bC
 - 8 beech
 - 8bc
From the list above, type the class you want to choose
>8bc
[(4,), (7,)]
'8 Beech'
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
 - 8 Beech
 - 8bC
 - 8 beech
 - 8bc
From the list above, type the class you want to choose
>8bc
2 [(4,), (7,)]
'8 Beech'
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
 - 8 Beech
 - 8bC
 - 8 beech
 - 8bc
From the list above, type the class you want to choose
>8bc
2 [(4,), (7,)]
[('8 Beech',), ('8bC',), ('8 beech',), ('8bc',)]
1 [('8 Beech',), ('8bC',), ('8 beech',), ('8bc',)]
8bc
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> writeSQL()
DELETE FROM classesTable where classID>0
>>> WriteSQL()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    WriteSQL()
NameError: name 'WriteSQL' is not defined
>>> writeSQL()
SELECT * FROM classesTable
(0, 0, 'T1', '8 Beech')
>>> writeSQL()
DELETE FROM classesTable where classIS = 0
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    writeSQL()
  File "/home/pi/Desktop/Testing Database.py", line 93, in writeSQL
    cursor.execute(sql)
sqlite3.OperationalError: no such column: classIS
>>> writeSQL()
DELETE FROM classesTable where classID = 0
>>> setClass()
***Existing Classes***
From the list above, type the class you want to choose
>8 Beech
2 []
Your new class will now be added
2 []
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
 - 8 beech
From the list above, type the class you want to choose
>8bC
[]
Your new class will now be added
[]
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
 - 8 beech
 - 8bc
From the list above, type the class you want to choose
>8 Beech
[('8 beech',), ('8bc',)]
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
 - 8 beech
 - 8bc
From the list above, type the class you want to choose
>8 beech
[('8 beech',), ('8bc',)]
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
 - 8 beech
 - 8bc
From the list above, type the class you want to choose
>8 Beech
[(8,)]
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
 - 8 beech
 - 8bc
From the list above, type the class you want to choose
>8 Beech
(8,)
>>> 
=============== RESTART: /home/pi/Desktop/Testing Database.py ===============
>>> setClass()
***Existing Classes***
 - 8 beech
 - 8bc
From the list above, type the class you want to choose
>8 Beech
8
>>> writeSWL()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    writeSWL()
NameError: name 'writeSWL' is not defined
>>> writeSQL()
SELECT * FROM classesTable
(8, 0, 'T1', '8 beech')
(9, 0, 'T1', '8bc')
>>> 
