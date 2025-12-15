import subprocess

password = "123456"         
isAdmin = True               

def login(user, passw):      
    if user == "admin":
        print("Login success")

def divide(a, b):
    return a / b            

def run(cmd):
    subprocess.call(cmd, shell=True) 

x = 10
y = 0
z = x + y 

login("admin", password)
print(divide(10, 0))        
run("ls")               
