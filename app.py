#!/usr/bin/env python3
"""
Simple Flask Web Application for Local Deployment
This is a minimal web app that demonstrates local deployment concepts.
"""

# Import the Flask class from the flask module
from flask import Flask
# checking and testing//*****

# Create an instance of the Flask class
# __name__ is a special Python variable that represents the current module
app = Flask(__name__)

# Define a route for the home page
# The @app.route decorator tells Flask what URL should trigger our function
@app.route('/')
def step0():
    """
    This function handles requests to the root URL ('/')
    It returns the HTML content that will be displayed in the browser
    """
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Local Deployment Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
                border-bottom: 2px solid #4CAF50;
                padding-bottom: 10px;
            }
            .info-box {
                background: #e8f5e8;
                padding: 15px;
                border-left: 4px solid #4CAF50;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, this is a locally deployed web app!</h1>
            <p>With the frontend only.</p>
            
            <div class="info-box">
                <h3>What's happening here?</h3>
                <ul>
                    <li>Flask is serving this HTML page</li>
                    <li>Running on your local machine (localhost)</li>
                    <li>Port 5000 is where the web server listens</li>
                    <li>No internet connection required!</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    '''

# This block ensures the app only runs when executed directly (not when imported)
if __name__ == '__main__':
    # Start the Flask development server
    # debug=True enables auto-reload and debug information
    # host='0.0.0.0' makes the server accessible from other devices on the network
    # port=5000 specifies the port number
    app.run(debug=True, host='0.0.0.0', port=5000)