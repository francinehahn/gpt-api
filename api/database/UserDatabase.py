from mysql.connector import connect, IntegrityError, Error
from api.connection_db.connection_db import config
from api.errors.UserErrors import EmailAlreadyInUse, UserNotFound

class UserDatabase:
    def create_user(self, id, data):
        """This method receives the user info from the service layer and inserts it into the database"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "INSERT INTO users_gpt (id, user_name, email, phone, password) VALUES (%s, %s, %s, %s, %s)"
            values = (id, data['user_name'], data['email'], data['phone'], data['password'])
            cursor.execute(query, values)
            connection.commit()

            return True

        except IntegrityError as err:
            if err.errno == 1062:
                raise EmailAlreadyInUse('This email is already in use.') from err
            
        except Error as err:
            raise err
        
        finally:
            cursor.close()
            connection.close()

    def get_user_by_email(self, email):
        """This method receives the user email from the service layer and returns the user info"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "SELECT * FROM users_gpt WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            
            if user:
                return user
            else:
                raise UserNotFound("Invalid user information.")

        except Error as err:
            raise err
        
        finally:
            cursor.close()
            connection.close()