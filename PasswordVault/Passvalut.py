import json
import os


filename="vault.json"

vault={}

def load_data():
    global vault  #means this vault variable declared outside the function,not a new local one
    if os.path.exists(filename):
        with open(filename,"r") as f:
            vault=json.load(f)


def save_data():
    with open(filename,"w") as f:
        json.dump(vault,f,indent=4)
    print("✅ vault saved.")

def add_login():
    site=input("Website: ")
    user=input("UserName: ")
    password=input("Password: ")
    vault[site]={"username":user,"password":password}
    print("✅ Login saved")

def view_login():
    if not vault:
        print("Vault is empty")
    for site,creds in vault.items():
        print(f"{site} - 🧑‍🏫 {creds['username']} | 🔏 {creds['password']}")


def search_login():
    site=input("Enter site name to search")
    if site in vault:
        print(vault[site])
    else:
        print("❌ Not found")

def delete_login():
    site=input("Enter site name to delete")
    if site in vault:
        del vault[site]
        print("🗑️ Deleted")
    else:
        print("❌ Not found")

def menu():
    load_data()
    while True:
        print("\n 🔏 PASSWORD VAULT")
        print("1. Add Login")
        print("2. View All")
        print("3. Search Login")
        print("4. Delete login")
        print("5. Save and Exit")

        ch=input("Choice: ")
        if ch=='1':add_login()
        elif ch=='2':view_login()
        elif ch=='3':search_login()
        elif ch=='4':delete_login()
        elif ch=='5':
            save_data()
            break
        else:
            print("❌ Invalid choice. Try Again!")

menu()


