(venv) C:\Apache24\htdocs\mysite\mysite\tests>pytest

=============================== test session starts ===============================

platform win32 -- Python 3.8.10, pytest-7.1.3, pluggy-1.0.0

rootdir: C:\Apache24\htdocs\mysite\mysite\tests

plugins: Faker-15.1.1

collected 0 items / 1 error

===================================== ERRORS ======================================

__________________________ ERROR collecting test_post.py __________________________

ImportError while importing test module 'C:\Apache24\htdocs\mysite\mysite\tests\test_post.py'.

Hint: make sure your test modules/packages have valid Python names.

Traceback:

C:\Users\patri\AppData\Local\Programs\Python\Python38\lib\importlib\__init__.py:127: in import_module

return _bootstrap._gcd_import(name[level:], package, level)

test_post.py:7: in <module>

    from blog.factories import PostFactory

    ..\blog\factories.py:2: in <module>
    
    import factory

    E   ModuleNotFoundError: No module named 'factory'

    ============================= short test summary info =============================

    ERROR test_post.py

    !!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!

    ================================ 1 error in 0.42s =================================

(venv) C:\Apache24\htdocs\mysite\mysite\tests>python manage.py runserver

    C:\Users\patri\AppData\Local\Programs\Python\Python38\python.exe: can't open file 'manage.py': [Errno 2] No such file or directory

(venv) C:\Apache24\htdocs\mysite\mysite\tests>python manage.py runserver

    C:\Users\patri\AppData\Local\Programs\Python\Python38\python.exe: can't open file 'manage.py': [Errno 2] No such file or directory

(venv) C:\Apache24\htdocs\mysite\mysite\tests>cd ..

    
(venv) C:\Apache24\htdocs\mysite\mysite>python manage.py runserver

    Watching for file changes with StatReloader

    Performing system checks...

System check identified no issues (0 silenced).

    October 17, 2022 - 15:42:35

    Django version 4.1.2, using settings 'mysite.settings'

    Starting development server at http://127.0.0.1:8000/

    Quit the server with CTRL-BREAK.

    [17/Oct/2022 15:42:58] "GET / HTTP/1.1" 200 10681

    Not Found: /home

    [17/Oct/2022 15:43:04] "GET /home HTTP/1.1" 404 2089

    [17/Oct/2022 15:43:12] "GET /admin HTTP/1.1" 301 0

    [17/Oct/2022 15:43:12] "GET /admin/ HTTP/1.1" 302 0

    [17/Oct/2022 15:43:12] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 2218

    [17/Oct/2022 15:43:12] "GET /static/admin/css/dark_mode.css HTTP/1.1" 200 796

    [17/Oct/2022 15:43:15] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0

    [17/Oct/2022 15:43:15] "GET /admin/ HTTP/1.1" 200 3580

    [17/Oct/2022 15:43:15] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 380

    [17/Oct/2022 15:43:15] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380

    [17/Oct/2022 15:43:15] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
