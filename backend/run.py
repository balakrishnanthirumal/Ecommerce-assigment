from app import create_app

app = create_app()
wsgi = app
#this is the entry point for the application. It creates an instance of the Flask application and runs it in debug mode.
if __name__ == '__main__':
    app.run(debug=True)