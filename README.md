# booksAdminApp
The project created for admin managing the CRUD operations of Books.
Using Django Framework (version 3.2.11) and python (version 3.7.9), the books app has been developed. The new project “books” has been created which has files – 
__init__.py
asgi.py
settings.py
urls.py
wsgi.py

In settings.py, added “booksCRUD” as an app in “INSTALLED_APPS” list and changed “DIRS” in “TEMPLATES” of settings.py. Also, changed the “DATABASES” where engine has been set to “mysql”. 

In project’s urls.py, urlpatterns contains path to admin and the urls of app which has been created.

booksCRUD/template – It has all HTML files in it. 

booksCRUD/models.py – It has two models Book and Admin. In book model, there are two fields created with CharField max_length of 200. Admin has user field which is OneToOneField.

In booksCRUD urls.py, there are multiple paths to signup, admin_login, options, create, retrieve, update, delete and logout. 

In booksCRUD views.py, there are functions for CRUD operations. 

When Django server is started with command py manage.py runserver, the user needs to http://127.0.0.1:8000/ jump to this url to see options of Admin and Signup. In signup, users will get created using SignupView form. 

For admin users, superuser has been created using py manage.py createsuperuser. If user is an admin, he will be able to login and see the CRUD operations.

For creating an entry, user needs to add book name and author name and click on “Create” button. The entry is created using ORM(Object Relational Mapping) eg. Books.objects.create(name=”SampleBook”,author=”AuthorSample”).

For retrieving the records, .all() has been used. When user clicks on retrieve button, it will show all the records that are present. We get it by Books.objects.all().

For updating an entry, user needs to enter the details of books that needs to be updated. Once the details are added, using .get() book is fetched from database and then saved the details which user has entered.

For deleting an entry, user needs to add the book name which he wants to delete. On clicking delete button, .filter() filters the record for given name and deletes it by using .delete() method.
