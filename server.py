from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_name(name):
    return f'Hi {name}!'

@app.route('/repeat/<num>/<word>')      #can you <int:num>/<string:word> to cast it from the URL to an int
def repeat_word(num, word):
    result = ''
    for i in range (0, int(num)):
        result += f'<p>{word}</p>'
    return result

@app.route('/<random>')
def random(random):
    print("Sorry! No response. Try again.")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.