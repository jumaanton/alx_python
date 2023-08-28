"""Import the Flask class from the flask module"""
from flask import Flask

"""Create an instance of the Flask class and pass in the __name__
of the current module"""
app = Flask(__name__)

"""Define a route for the root URL ("/") and set strict_slashes=False to allow
both with and without trailing slashes"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """this function will be executed when the root URL is accessed """
    return "Hello HBNB!"  # Return the string "Hello HBNB!" as the response

 """This block of code will only run if the script is executed directly
(not imported as a module)"""
if __name__ == '__main__':
    """Start the Flask development server with the specified host and port"""
    app.run(host='0.0.0.0', port=5000)
