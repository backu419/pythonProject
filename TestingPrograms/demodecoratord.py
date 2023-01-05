from datetime import datetime
def get_data_time(func):
    def wrapper():
        print("Function name = "+func.__name__)
        print(datetime.today().strftime("%Y-%M-%D %H:%M:%S"))
        func()
    return wrapper
@get_data_time
def login():
    print("Login ")
login()
@get_data_time
def logout():
    print("Logout ")
logout()
