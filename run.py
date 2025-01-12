from app import create_app
import sqlite3
app = create_app()
con = sqlite3.connect('app/notes.db')

if __name__=='__main__':
    app.run(debug=True)