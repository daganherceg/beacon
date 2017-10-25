# beacon readme

### House keeping
- Work on your own branch and consistently pull to ensure you are up to date

### Installation requirments:
- Django 1.8
- virtual ENV

### Installation
Start virtual invironment

1. Create and activate your virtual envoronment (I called mine skillshare) inside your approproate directory

$ virtualenv .
$ source bin/activate

2. Install Django into virtual environment
```python
(skillshare)$ pip install virtualenvwrapper
(skillshare)$ pip install django==1.8
(skillshare)$ pip install --upgrade django-registration
(skillshare)$ pip install django-crispy-forms==1.7.0
(skillshare)$ pip install django-registration-redux==1.8
```

3. Clone beacon from github repo

4. Install relevant packages
I believe the following should install all uninstalled apps
$ python manage.py syncdb  // similar to migrate but also allows the creation of a superuser

If that doesn't work you will need the following:

### Running project
In your virtual environment folder (where manage.py is located), run the server
(skillshare)$ python manage.py runserver

### Userfull commands
$ pip freeze   // checkout what is installed in current environment
 when running pip freeze from your virtualenv folder you should see something like this
```python
(skillshare)$ pipfreeze
confusable-homoglyphs==2.0.2
Django==1.8
django-crispy-forms==1.7.0
django-registration==2.3
django-registration-redux==1.8
pbr==3.1.1
pytz==2017.2
six==1.10.0
stevedore==1.25.0
virtualenv==15.1.0
virtualenv-clone==0.2.6
virtualenvwrapper==4.7.2
```

$ python manage.py migrate   // syncronyses unmigrated apps to DB 

### Your base directory should look like the following

```python
 ── skillshare (virtual environment folder)
    ├── bin
    ├── include
    ├── lib
    ├── skillshare
    ├── src (project pacakge from github)
    │   ├── beacon_landing
    │   └── signups
    └── static
        ├── media
        ├── static
        ├── static-only
        └── templates
```
