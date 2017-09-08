Title: Starting Django     
Author: Joe      
Date: 2017-03-13      
category: Python Web Application  

### Django  

We can use tools in Python to help us build awesome web applications.. *enter Django.* This is a **web framework** written in Python. A web framework is essentially a set of tools designed for building interactive websites. There are slews of these tools written in other languages as well. They all do just about the same thing. Having these options provides a good set of flavors to choose from. After you feel comfortable with building a web application using Django; don't stop there! Explore others and pick out the one that works best for you.  

#### Important Notes    

- For this article, any set of text that looks like `this` will be what is typed in the terminal.  
- Down the road, anytime we edit a file, make sure to open with sudo ($~ sudo filname)  

***  

### Make a Plan  

When starting your web app project, it's a good idea to set up a nice foundation. Ask yourself some questions. What is your web application going to do? Who is going to use it? What features do you want to make sure to implement. Use a pen and paper if you have to. Do some research on the functionality of other sites you or others use and see which ones you want to incorporate or leave out of your web app. Use the above to help yourself write a *spec* (specification) or description of your project. The spec outlines the goals of your project, functionality, and talks about what it is going to look like and the user interface. Always refer back to your spec. This will help with keeping your project stay on its course to reach the goals you originally placed. You'll learn a lot along the way, so keep a logbook of sorts to jot down what you've learned during this process, so you can revisit ideas if you need to.  

### Unbuntu  

Since are using Unbuntu on the Chromebooks, this *tutorial* will go over the steps to creating a virtual environment and installing Django if you're using Unbuntu.  

#### Create New Directory  
Let's get going on creating a directory and virtual environment to work in. This is a place on your system where you will install Python packages and keep them separate from all other packages; this is important.  

Navigate to your new directory for your project in the terminal  
cd (change directory)  

***  
*user$* `cd directory_name`  
***  

#### Install and Create a Virtual Environment  

***  
*directory_name$* `sudo apt-get install python-virtualenv`    

*directory_name$* `vitualenv 11_env`    

***  

#### Activate Your Virtual Environment  
So we have are virtual environment ready to go. Let's activate it.    

***  

*directory_name$* `source 11_env/bin/activate`    

***  

Once you close the terminal you are working in, the virtual environment will become inactive. You can also stop using the virtual environment by entering `deactivate`.  

#### Install Django and Create Your Project  

While your virtual environment is activated, install Django.  

***  

*(11_env)directory_name$* `sudo pip install Django`  

***  

Take note that Django is only available to you when the environment is active.  

Create your project by entering the following commands (The period at the end of the first command is necessary!):  

***  

*(11_env)directory_name$* `django-admin.py startproject directory_name .` --> Tells Django to set up your new project called *directory_name*  

*(11_env)directory_name$* `ls` --> "ls" simply means, list everything in that directory your currently in.  

*(11_env)directory_name$* `ls directory_name`  

***  

#### Create the Database  
Django stores most of the information related to a project in a database, so we need to create one that it can work with.  

***  

*(11_env)directory_name$* `sudo python manage.py migrate`  --> *Synchronize unmigrated apps*... *Apply all migrations*    

*(11_env)directory_name$* `ls` --> notice the *db.sqlite3*  

***  

Whenever we change the database, we are *migrating* it. This just tells Django to make sure the database is lined up with project's current state. Since you used SQLite for the first time, Django creates a new database for you. For the most part, we won't have to worry about modifying the database.  

#### View Your Project  

Run the server to make sure Django (and you) set up your project properly with the *runserver* command:  

***  

*(11_env)directory_name$* `sudo python manage.py runserver`  

***  

A server is started by Django. On your system, you can now check out your project to see how well it's working.  

more info to come...  
