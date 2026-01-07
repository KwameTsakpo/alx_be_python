from mysql import connector as mysql


#connect to database
my_db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Crazy@moon1234',
    database = 'authdb'
)

username = str(input("Username: "))
password = str(input("Password: "))

if my_db.is_connected():
    print("----------------------------------------\nDatabase connection: Connected successfully\n---------------------------------------")

    #indicate cursor 
    my_cursor = my_db.cursor()

    try:
        query = ('select * from login_details')
        # values = (username,password)
        
        # my_cursor.execute(query,values)
        my_cursor.execute(query)
        
        record = my_cursor.fetchall()
        
        for row in record:
            if row[1] == username and row[2] == password:
                print(f'Welcome {username}, your password is accepted. you are now logged in.')
                print(f'Your record: {record}')
        
            elif record == None:
                print(f'No record exist: {record}')
        
        
        

    except Exception as e:
        print(f"Records doesn't exist: {e}")

else:
    print('No connection established')

