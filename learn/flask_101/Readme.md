# Flask

* **Flask** is a micro web framework written in Python.
* It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.
* Flask supports extensions that can add application features as if they were implemented in Flask itself.

## Installation && Deployment basics

* Install **Flask**: 

```bash
pip3 install Flask
```

* Python virtual envirement:

```bash
pip3 install virtualenv
```

> A virtual environment isolates your project from the system to prevent any conflicts.

1. Which environment variable do you need to change in order to run Flask?

```
FLASK_APP
```

## Basic syntax && Routing

* Basic "Hello World" app:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
	return "Hello, dear learner"
```

> this app display "Hello, dear learner" text on the deployed website.

* **app.route()**: allows to create different pages and dynamic URLs.

let's add a new route to our app:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
	return "Hello, dear learner"

@app.route("/admin")
def admin():
	return "Hello, Admin"
```

Now visiting the route "/" display: *"Hello, dear learner"* 
And visiting the "/admin" page display *"Hello, Admin"*

1. What's the default deployment port used by Flask?


```
5000
```

2. Is it possible to change that port? (yay/nay)

```
yay
```

## HTTP Methods && Template Rendering

> By default, a route only answers to GET requests.

* Make python differently respond to an incoming GET or POST request:

```py
from flask import request

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		return "Try to login"
	else:
		return "Show the login"

```

* Template rendering function makes Flask automatically render HTML files into a website, making it easier to handle.

```py
from flask import render_template

@app.route("/redered")
def hello(name=None):
	return render_template("template.html", name=name)

"""
HTML example:
<!DOCTYPE html>
<title>Hello From Flask</title>
<h1>Hello again.......!</h1>
"""
```

1. Does Flask support POST requests? (yay/nay)

```
yay
```

2. What markdown language can you use to make templates for Flask? 

```
html
```

## File Upload

* You can access those files by looking at the **files** attribute on the **request object** (Each uploaded file is stored in that dictionary).
*  It behaves just like a standard Python file object, but it also has a **save()** method that allows you to store that file on the filesystem of the server.

```py
from flask import request
from werkzeug.utils import secure_filename

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
	if request.method == "POST":
		f = request.files['the_file']
		f.save("/var/www/uploads/" + secure_filename(f.filename))

```

> Note: Make sure not to forget to set the **enctype="multipart/form-data"** attribute on your HTML form, otherwise the browser will not transmit your files at all.

## Flask Injection

* **Flask** definitely is a great tool but a simple misconfiguration may lead to severe security consequences.
* The template engine provided within the **Flask** framework may allow developers to introduce **Server-Side Template Injection (SSTI)** vulnerabilities.  An attacker can execute code within the context of the server (may lead to a full **RCE**).

```py
from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)

@app.route("/vuln")
def hello_ssti():
	person = {"name": "Hacker", "password": "123456789"}
	if request.args.get("name"):
		person['name'] = request.args.get('name')
	template = '''<h2>Hello %s !</h2>''' % person['name'] # Problem

	return render_template_string(template, person=person)
def get_user_file(f_name):
	with open(f_name) as f:
		return f.readlines()

app.jinja_env.globals['get_user_file'] = get_user_file

if __name__ == '__main__':
	app.run()

```

* The main reason for this vulnerability is that **Jinja2** (template rendering engine) uses *curly braces* to surround variables used in the template. As you can see on the line with *# Problem*, our template is put in **''' '''** brackets which allow us to abuse the **Jinja template mechanism**. A variable after hello is parsing a name from a variable **person**. But because this is a vulnerable code we can make it output the password. 

* GO to `IP:5000/vuln?name` and put `{{ person.password }}`
* Now let's take that vulnerability to another level and read files (LFI).  
`{{ get_user_file("/etc/passwd") }}`

* by using the `get_user_file()` we can read the `/home/flask/flag.txt` and get the flag.

1. What's inside /home/flask/flag.txt ?

```
THM{flask_1njected}
```







```bash
# https://github.com/Swafox/Flask-examples
```