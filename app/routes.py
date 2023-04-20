from flask import Flask             # from the flask module import the flask class
# PEP 8

app = Flask(__name__)               # create an instance of flask into our variable "app"
                                    # from here on out "app" is now a "object"
        
@app.get("/")                       # We can now use our object's method "get" as a director.
def index():                        # A decorator wraps a function ( more on this in a bit)
    me = {                          # On line 8, we create a new directory with hey/value pairs.
        "first_name": "Aaron",
        "last_name": "Pride",
        "hobbies": "Art",
        "is_active": True
    }
    return me                       # When you return a dictionary from a view function,
                                    # flask automatically converts it to JSON for compatibility.