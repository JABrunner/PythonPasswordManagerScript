from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, values in initial_values.items():
                self.add_password
                
    def load_password_file(self,path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")
    def get_password(self, site):
        return self.password_dict[site]

def main():
    password = {
        "email": "1234567",
        "facebook": "myfbpass",
        "youtube": "myYTpass",
        "twitter": "mytwitterPass"
    }
    pm = PasswordManager()

    print("""What do you want to do?
    (1) Create New Key
    (2) Load an Existing Passwor
    (3) Create new password file
    (4) Load and existing file
    (5) Add a new password
    (6) Get a new password
    (Q) Quit
    """)

    done = False

    while not done:
        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter Path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input("Enter Path")
            pm.load_key(path)
        elif choice == "3":
            path = input ("Enter path: ")
            pm.create_password_file(path, password)
        elif choice == "4":
            path = input ("Enter path: ")
            pm.load_password_file(path)
        elif choice == "5":
            site = input("Enter the Site: ")
            password = input("Enter the Password: ")
            pm.add_password(site, password)
        elif choice == "6":
            site = input("What site do you want?: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif choice == "Q":
            done = True
            print("Goodbye")
        else:
            print("Error, invalide choice")

if __name__ == "__main__" : 
     main()
