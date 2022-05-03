# Meduzzen_backend_test

To test the application, you need to activate pipenv, run migrations, create a superuser and activate the server:

pipenv install
pipenv shell
python manage.py makemigrations
python manage.py migrate
python manage.py creates superuser
python manage.py runserver

Next, the local server starts and the web page opens along the way
/admin/ you can view the standard admin panel of the system.
/api/v1/usersList System API.
/api/v1/usersList/<int:pk>/ will help to test put, delete, patch requests to the system.

All testing of the system was carried out using Postman
