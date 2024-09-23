from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#       key_file.write(key)
# write_key()

def load_key():
  with open("key.key", "rb") as file:
    key = file.read()
    return key

key=load_key()
fer = Fernet(key)

def add():
  name=input("Enter your username: ")
  pwd = input("Enter your password: ")
  with open("passwords.txt", "a") as f:
      f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
  with open("passwords.txt", "r") as f:
    for line in f.readlines():
      data = line.rstrip()
     # user,pwds = data.split("|")
     # decrypted_pwd = fer.decrypt(pwds.encode()).decode()
     # print("User: ", user,"| Password" ,decrypted_pwd)
      try:
        user, pwds = data.split("|")
        decrypted_pwd = fer.decrypt(pwds.encode()).decode()
        print("User:", user, "| Password:", decrypted_pwd)
      except ValueError:
        print(f"Skipping line due to incorrect format: {data}")

master_pwd = input("What is the master password? ")

# def mastadd():
#   with open("master_pass.txt", "a") as f:
#     pwd="hokhok69"
#     f.write(fer.encrypt(pwd.encode()).decode())
# mastadd()

def mastview():
  with open("master_pass.txt", "r") as f:
    for line in f.readlines():
      data = line.rstrip()
      decrypted_pwd = fer.decrypt(data.encode()).decode()
      return decrypted_pwd

if master_pwd == mastview():
    print("true")
    while True:
      choice = input("Enter your choice You want to view or add pass or quit: ").lower()
      if choice == "quit":
        break
      if choice== "add":
        add()  
      elif choice == "view":
        view()
      else:
        print("Invalid choice. Please try again.")
else:
  print("Wrong password")
