import mysql.connector as mysql


#database connection

db_connect = mysql.connect(
    host = "localhost",
    user = "root",
    password = "Crazy@moon1234",
    database = "authdb"
)

if db_connect.is_connected():
    print("----------\n Connection established\n---------")
    cursor = db_connect.cursor()

else: raise Exception("Error: Not connected")

is_loggedIn = False



##Main program
def main():
    username = str(input("Enter your username, min characters(50): "))
    password = str(input("Enter your password min characters(15): "))
    # email = str(input("Enter emial: "))
    # phone = str(input("Enter phone: "))
    
    # user = Auth_session(username,password,email,phone)
    
    # user.add_new_user()
    
    # print("\n__________________________________________________________\nPlease login with your username and password that was created\n__________________________________________________________\n\n")
    
    print("\n___________________________________\nWelcom to CHES Alumni Network\n___________________________________")
    user = Login_auth(username,password)
    user.login_auth()

#class Definition
class Auth_session:

    def __init__(self, username, password, email, phone, userID):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.userID = userID
        
    def getDetails(self):
        if is_loggedIn:
            print(f"UserName: {self.username}\nEmail: {self.email}\nPhone Number: {self.phone}")
        
        else:
            print("Please login first.")


    def add_new_user(self):

        print("Create Account\n_________________________________________________________")

        try:
            query = ("insert into login_details(username, password, email, phone) values(%s,%s,%s,%s)")
            values = (self.username, self.password, self.email, self.phone)

            cursor.execute(query,values)
            db_connect.commit()
            print("\n__________________________________________________________\nProfile Created Successfully\n__________________________________________________________\n")

        except Exception as e:
            print("Sorry there was a problem: ",e)
    
class Login_auth:

    user_info = None
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login_auth(self):
        # print("\n___________________________________\nWelcom to CHES Alumni Network\n___________________________________")
        # username = str(input("Enter Username: "))
        # password = str(input("Enter Password: "))
        
        try:
            query = ("Select * from login_details where username = %s and password = %s")
            values = (self.username,self.password)
            
            cursor.execute(query,values)
            
            record = cursor.fetchall()
            
            print(record)
            for row in record:
                try:
                    if record:
                        if row[1] == self.username:
                            pass
                        else:
                            print("Invalid Username")
                        
                        if row[2] == self.password:
                            uID = row[0]
                            uname = row[1]
                            upas = row[2]
                            uemail = row[3]
                            uphone = row[4]
                            
                            is_loggedIn = True
                            self.user_info = Auth_session(uname,upas,uemail,uphone,uID)
                            self.user_info.getDetails()
                            
                        else:
                            print("Invalid Password")
                    else:
                        print("User does not exist")
                        
                except Exception as e:
                    print(f'Error in authentication level: {e}')
            
            
        
        except Exception as e:
            print(f'Error in Login: {e}')



if __name__ == '__main__':
    main()