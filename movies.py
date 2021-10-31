import sqlite3

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
    conn.execute("INSERT INTO MOVIES (Name,Actor,Actress,Director, Year_of_Release) \
      VALUES ('Pirates of the Caribbean', 'Johnny Deep', 'Penelope Cruz', 'Lucy Bevan', '2011')");
    

    conn.commit()
    
print = "Records created successfully";

conn.close()