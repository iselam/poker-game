def get_connection_string():
    #instantiate the variables needed to establish a connection
   server='MSI\\MSSQLSERVER01'
   database='game-db'
   username='gameuser'
   password='gameruser01!'
   
   #define a connection string to establish a connection with the ODBC Driver
   connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

   return connection_string
