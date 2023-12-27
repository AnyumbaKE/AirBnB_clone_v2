# 0x02. AirBnB clone - MySQL
<table>
        <tr>
            <td>Group project</td>
            <td>Python</td>
            <td>OOP</td>
            <td>Back-End</td>
            <td>MySQL</td>
            <td>ORM</td>
            <td>OOP</td>
            <td>SQLAlchemy</td>
        </tr>
    </table>


The aim of the project is to develop a MySQL database for [AirBnb clone Project](https://github.com/AnyumbaKE/AirBnB_clone/tree/master)

<table>
        <tr>
            <td>By: Guillaume</td>
        </tr>
        <tr>
            <td>Weight: 2</td>
        </tr>
        <tr>
            <td>Project to be done in teams of 2 people (your team: Stanley Anyumba, Margaret Wangechi)</td>
        </tr>
        <tr>
            <td>Project will start Dec 15, 2023 6:00 AM, must end by Dec 21, 2023 6:00 AM</td>
        </tr>
        <tr>
            <td>Checker will be released at Dec 16, 2023 6:00 PM</td>
        </tr>
        <tr>
            <td>An auto review will be launched at the deadline</td>
        </tr>
    </table>
    
### Authors
[Stan Anyumba](https://www.github.com/AnyumbaKE) </br>
[Maggie Wangechi](https://www.github.com/QueenMaggie)

### Background Context
Environment variables will be your best friend for this project!

- HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
- HBNB_MYSQL_USER: the username of your MySQL
- HBNB_MYSQL_PWD: the password of your MySQL
- HBNB_MYSQL_HOST: the hostname of your MySQL
- HBNB_MYSQL_DB: the database name of your MySQL
- HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)

### Resources
Read or watch:

[cmd module](https://docs.python.org/3/library/cmd.html) </br>
[unittest module](https://docs.python.org/3/library/unittest.html#module-unittest) </br>
[args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/) </br>
[SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html) </br>
[How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql) </br>
[Python3 and environment variables](https://docs.python.org/3/library/os.html?highlight=env#os.getenv)</br>
[SQLAlchemy](https://docs.sqlalchemy.org/en/13/) </br>
[MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

### General
- What is Unit testing and how to implement it in a large project
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function
- How to create a MySQL database
- How to create a MySQL user and grant it privileges
- What ORM means
- How to map a Python Class to a MySQL table
- How to handle 2 different storage engines with the same codebase
- How to use environment variables
### Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- 
### Python Unit Tests
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project: ex: for models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
We strongly encourage you to work together on test cases, so that you don’t miss any edge cases
### SQL Scripts
- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0
- Your files will be executed with SQLAlchemy version 1.4.x
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc
