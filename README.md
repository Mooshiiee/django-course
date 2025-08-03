creating venv 
`py -m venv venv`

starting venv
`venv\Scripts\activate`

deactivating venv
`venv\Scripts\deactivate`

intalling Django with pip
`py -m pip install Django`

creating a project
`django-admin startproject mysite`



# 2
create a public repo and track work through Github

explain django apps vs. projects

`py manage.py startapp books`

create rudimentary view and url conf.

add app to the `settings.py`

explain SQL

explain Django ORM

create models

`py .\manage.py migrate`

explain the default models with django. migrations have already been made and are ready, 
therefore we can just run migrate staight off the bat

for our custom models we first do `makemigrations books`

`py .\manage.py makemigrations books`

now lets see the DDL to our corresponding tables

`py manage.py sqlmigrate polls 0001`

now we can migrate

`py .\manage.py migrate (books)`

lets populate the tables in the admin, hmm the tables dont show up, we need to specify what tables
have admin access

Now lets add to admin:
 - create superuser: `py manage.py createsuperuser`

now we can populate tables!

we see that rows show as "Author Object (1)" and etc,
we can add string representations to the models to help with this

Nows lets explain a bit more about the client-server-database architecture 







