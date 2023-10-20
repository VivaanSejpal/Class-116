# PRO-C116-Reference-Code

**1. GET and POST methods**

HTTP methods are used to tell a web server what to do with a request. The two most common methods are GET and POST.

**GET** is used to retrieve data from a server. For example, when you type a URL into your web browser, you are sending a GET request to the server for the page at that URL.

**POST** is used to send data to a server. For example, when you fill out a web form and submit it, you are sending a POST request to the server with the data from the form.

**2. Server**

A web server is a computer that stores and delivers web pages and other web content to users. When you visit a website, your web browser sends a request to the web server for the page you want to visit. The web server then sends the page back to your browser.

**3. jQuery**

jQuery is a JavaScript library that makes it easier to interact with web pages. It provides a number of functions for tasks such as animating elements on a page, making AJAX requests, and handling events.

**4. Python Flask library**

The Python Flask library is a web framework that makes it easy to build web applications with Python. It provides a number of features such as routing, templates, and database support.

**5. Why we need all these**

We need all of these concepts to build and use web applications.

* HTTP methods allow us to tell the web server what to do with a request.
* Web servers store and deliver web pages and other web content to users.
* JavaScript libraries like jQuery make it easier to interact with web pages.
* Web frameworks like Python Flask make it easier to build web applications.

Here is a simple analogy that may help a 15-year-old understand these concepts:

Imagine a restaurant. The HTTP methods are like the different types of orders you can place at a restaurant. For example, you can place a GET order to get a menu, or you can place a POST order to place your food order.

The web server is like the kitchen at the restaurant. It receives the orders from the customers (via the HTTP methods) and prepares the food (web pages and other web content).

jQuery is like a waiter or waitress at the restaurant. It helps the customers interact with the kitchen (web server). For example, jQuery can be used to send orders to the kitchen, receive food from the kitchen, and update the menu when new dishes are added.

The Python Flask library is like the manager of the restaurant. It makes sure that everything runs smoothly and that the customers are happy.

We need all of these concepts to build and use web applications because they allow us to interact with web servers, create dynamic web pages, and build complex web applications.

Here is a simplified explanation of how all of these concepts work together:

When you visit a website, your browser sends a GET request to the server to retrieve the HTML, CSS, and JavaScript files that make up the website. The server then sends the web page back to your browser, and your browser displays the web page on your screen.

If the web page contains a form, you can submit the form by clicking on the submit button. When you submit the form, your browser sends a POST request to the server with the form data. The server then processes the form data and responds to the request.

The server can respond to the request in a variety of ways. For example, the server can send back a new web page, or the server can send back a JSON object with the results of processing the form data.

jQuery can be used to add animations, effects, and other interactivity to web pages. For example, jQuery can be used to make a form field glow red when it is empty, or jQuery can be used to animate a progress bar when a file is uploading.

The Python Flask library can be used to create web applications. Flask provides a simple and easy-to-use framework for developing web applications in Python.

Here is an example of how to create a simple web application in Python Flask:

Python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        name = request.form["name"]
        return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
Use code with caution. Learn more
This web application has a single route, /. The route can be accessed with both GET and POST requests.

If the request is a GET request, the web application will render the index.html template. The index.html template is a simple HTML template that contains a form with a single input field for the user's name.

If the request is a POST request, the web application will get the user's name from the form data and render the index.html template with the user's name.

This is just a simple example of how to create a web application in Python Flask. Flask can be used to create more complex web applications, such as online shopping websites and social media platforms.

Why do we need all of these concepts?

We need all of these concepts to create web applications. Web applications are programs that run on a web server and can be accessed by users through a web

**The `app.route()` function in Python Flask is used to map a URL to a function. When a user visits a URL that has been decorated with the `app.route()` function, Flask will call the associated function.

For example, the following code maps the URL `/` to the `index()` function:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

If a user visits the URL `http://localhost:5000/`, Flask will call the `index()` function and render the `index.html` template.

The `app.route()` function can also be used to map a URL to a specific HTTP method. For example, the following code maps the URL `/login` to the `login()` function, which can only be accessed using the POST method:

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Validate the username and password

    return render_template("login_success.html")

if __name__ == "__main__":
    app.run(debug=True)
```

If a user tries to access the URL `http://localhost:5000/login` using the GET method, Flask will return a 405 Method Not Allowed error.

Here are some of the varied types of `app.route()` functions:

* **Static routes:** These routes map a URL to a specific function, regardless of the HTTP method used.
* **Dynamic routes:** These routes map a URL to a function that can be accessed using multiple HTTP methods.
* **Path parameters:** These routes map a URL to a function that can accept parameters in the URL path.
* **Query parameters:** These routes map a URL to a function that can accept parameters in the query string.

For example, the following code maps the URL `/user/<username>` to the `user()` function, which can be accessed using any HTTP method:

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/user/<username>")
def user(username):
    # Get the user's data from the database

    return render_template("user.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)
```

If a user visits the URL `http://localhost:5000/user/john_doe`, Flask will call the `user()` function with the parameter `username` set to `"john_doe"`.

The `app.route()` function is a powerful tool for mapping URLs to functions in Python Flask. It is used to create a wide variety of web applications, from simple websites to complex REST APIs.


The local server at 127.0.0.1:5000 is a special server that is used to test and develop web applications. It is also known as the localhost server.

The IP address 127.0.0.1 is a loopback address, which means that any traffic sent to this address is routed back to the same computer. This makes it ideal for testing web applications, as you can be sure that the traffic is not being sent to the internet.

The port number 5000 is a common port number for web applications. It is not reserved for any specific purpose, but it is often used by developers because it is easy to remember.

So, why is the local server at 127.0.0.1:5000? Because it is a convenient and reliable way to test and develop web applications.

**Here are some of the benefits of using the local server at 127.0.0.1:5000:**

It is fast and reliable, as the traffic is not being sent to the internet.
It is secure, as the traffic is only accessible to the local computer.
It is free to use.
It is easy to set up and use.
To use the local server at 127.0.0.1:5000, you simply need to start your web application on port 5000. You can then access the application from your web browser by visiting the URL http://localhost:5000.



**Servers are computers that store and deliver data and applications to users. They are typically more powerful than regular computers and are designed to run 24/7. Servers can be used for a variety of purposes, such as hosting websites, running email servers, and storing files.**

Local servers are servers that are located on the same computer as the user. They are often used for testing and developing web applications, but they can also be used to store files and serve them to other devices on the same network.

Production servers are servers that are used to host live websites and applications. They are typically located in data centers, which are specially designed facilities that provide power, cooling, and security for servers.

Here is a table that summarizes the key differences between local servers and production servers:

Feature	Local server	Production server
Location	On the same computer as the user	In a data center
Purpose	Testing and development	Hosting live websites and applications
Performance	Typically slower than production servers	Typically faster than local servers
Availability	Typically less available than production servers	Typically more available than local servers
Security	Typically less secure than production servers	Typically more secure than local servers
Examples of local servers

The web server that is included with most operating systems
A web server that is running on a Raspberry Pi
A web server that is running in a Docker container
Examples of production servers

The servers that host Google Search, YouTube, and other Google products
The servers that host Amazon Web Services (AWS) and other cloud computing platforms
The servers that host websites and applications for businesses and organizations

**Why do we need different types of servers?**


**We need different types of servers for different purposes.** Local servers are ideal for testing and developing web applications, as they are easy to set up and use. Production servers are necessary for hosting live websites and applications, as they provide the performance, availability, and security that these applications need.