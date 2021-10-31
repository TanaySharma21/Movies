import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect('Movies.db')
    
    print = "Opened database successfully";


def create_table(conn, create_table_sql):
    conn.execute('''CREATE TABLE MOVIES(
         Name text PRIMARY KEY,
         Actor text NOT NULL,
         Actress text NOT NULL,
         Director text NOT NULL,
         Year_of_Release text NOT NULL
         );''')
    
    print = "Table created successfully";

def create_movies(conn, movies):
    
    cur = conn.cursor()
    cur.execute("INSERT INTO MOVIES (Name,Actor,Actress,Director, Year_of_Release) \
      VALUES ('Pirates of the Caribbean', 'Johnny Deep', 'Penelope Cruz', 'Lucy Bevan', '2011')");
    
    cur.execute("INSERT INTO MOVIES (Name,Actor,Actress,Director, Year_of_Release) \
      VALUES ('Shutter Island', 'Leonardo DiCaprio', 'Patricia Clarkson', 'Martin Scorsese', '2010')");
      
    cur.execute("INSERT INTO MOVIES (Name,Actor,Actress,Director, Year_of_Release) \
      VALUES ('The Silence of the Lambs', 'Anthony Hopkins', 'Jodie Foster', 'Jonathan Demme', '1991')"); 

    cur.execute("INSERT INTO MOVIES (Name,Actor,Actress,Director, Year_of_Release) \
      VALUES ('The Perks of Being a Wallflower', 'Logan Lerman', 'Emma Watson', 'Stephen Chbosky', '2012')");

    cur.execute("INSERT INTO MOVIES (Name,Actor,Actress,Director, Year_of_Release) \
      VALUES ('Fight CLub', 'Brad Pitt', 'Helena Bonham Carter', 'David Fincher', '1999')");
      
    conn.commit()
    
    print = "Records created successfully";

def select_movies_rows (conn, movies):
    cur = conn.cursor()
    cur.execute("SELECT Name, Actor, Actress, Director, Year_of_Release FROM Movies")
    rows = cur.fetchall()
    
    for row in rows:
        print=(row)

def select_movies_where(conn, movies):
    cur = conn.cursor()
    cur.execute("SELECT Name FROM WHERE Actor = Leonardo DiCaprio")
        
    for row in cur:
        print = "Name = ", row[0],"\n"
        
        print = "Operation done successfully";
        conn.close()
