#Importing flask module in the project
# The line `from flask import Flask` is importing the Flask module, which is a web framework for
# Python. This module provides tools and functionalities to build web applications. By importing the
# Flask module, we can create an instance of the Flask class and use its methods and attributes to
# define routes and handle HTTP requests.
from flask import Flask

#Create an object of the Flask class
# `app = Flask(__name__)` creates an instance of the Flask class and assigns it to the variable `app`.
# The `__name__` argument is a special Python variable that represents the name of the current module.
# In this case, it represents the name of the main module or script that is being executed.
app = Flask(__name__)

#The route() function of the Flask class 
# `@app.route("/")` is a decorator that binds the URL "/" to the function `first_flask()`. This means
# that when a user visits the root URL of the Flask application (e.g., http://localhost:5000/), the
# function `first_flask()` will be executed and its return value will be displayed in the browser.
@app.route("/")
#‘/’ URL is bound with first_flask function.
def first_flask():
    """
    The function "first_flask" returns a string that says "This is my first flask program".
    :return: the string "This is my first flask program".
    """
    return "This is my first flask program"

#Define a function with different endpoint
# `@app.route("/flask_2")` is a decorator that binds the URL "/flask_2" to the function
# `second_flask()`. This means that when a user visits the URL "/flask_2" in their browser, the
# function `second_flask()` will be executed and its return value will be displayed in the browser.
@app.route("/flask_2")
def second_flask():
    """
    The function "second_flask" returns the string "Python is fun!".
    :return: the string "Python is fun!".
    """
    return "Python is fun!"

#run using debug argument
# `app.run(debug=True)` is used to run the Flask application. The `debug=True` argument enables the
# debug mode, which provides additional information and helpful error messages in case of any issues
# with the application. It is recommended to use the debug mode during development to aid in debugging
# and troubleshooting.
app.run(debug=True)

