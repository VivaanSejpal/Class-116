
    # """
    # This is a basic Flask application that renders an HTML template called "index.html" and passes a
    # variable named "name" with the value "VIVAAN" to the template.
    # :return: The function `first_webpage()` returns the rendered template 'index.html' with the variable
    # 'name' passed as 'index_variable'.
    # """
# `from flask import Flask, render_template` is importing the Flask module and the `render_template`
# function from the Flask module.
from flask import Flask, render_template
# `app = Flask(__name__)` creates an instance of the Flask class and assigns it to the variable `app`.
# The `__name__` argument is a special Python variable that represents the name of the current module.
# By passing `__name__` as an argument, we are telling Flask to use the current module as the starting
# point for the application.
app = Flask(__name__)
#in the function return render_template(‘index.html’)
# `@app.route("/index")` is a decorator in Flask that associates the URL path "/index" with the
# function `first_webpage()`. When a user visits the "/index" URL, Flask will call the
# `first_webpage()` function and return the result as the response.
@app.route("/index")
def first_webpage():
    """
    The function "first_webpage" renders an HTML template called "index.html" and passes a variable
    named "name" with the value "VIVAAN" to the template.
    :return: the rendered template 'index.html' with the variable 'name' passed as 'index_variable'.
    """
    #Create a variable
    name = 'VIVAAN'
    # Pass the variable in the template
    # `return render_template('index.html', index_variable = name)` is rendering an HTML template
    # called "index.html" and passing a variable named "index_variable" with the value of the `name`
    # variable to the template. This means that the value of the `name` variable will be accessible in
    # the "index.html" template using the variable name "index_variable".
    return render_template('index.html', index_variable = name)
# `app.run(debug=True)` is a method that starts the Flask development server. The `debug=True`
# argument enables debug mode, which provides more detailed error messages and automatically reloads
# the server whenever changes are made to the code.
app.run(debug=True)



