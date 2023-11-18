def option_input():
    while True:
        try:
            print("1. Display all contacts")
            print("2. Search for a contact")
            print("3. Add a contact")
            print("4. Update a contact")
            print("5. Delete a contact")
            print("6. Exit")
            option=int(input("Enter the option number: "))
            if option<1 or option>6:
                print("----------------------------------------------------------------")
                print("Invalid option. Enter again!")
                continue
            break
        except ValueError:
            print("----------------------------------------------------------------")
            print("Invalid Input. Enter again!")
    print("----------------------------------------------------------------")
    return option
def perf_operations(option):
    if option==1:
        print("                        CONTACT BOOK                     ")
        print("----------------------------------------------------------------")
        display_contacts()
    elif option==2:
        while True:
            try:
                print("1. Name\n2. Phone Number\n3. Exit")
                choice=int(input("Enter the option number: "))
                if choice<1 or choice>3:
                    print("Invalid option! Enter again.")
                    print("----------------------------")
                    continue
                else:
                    break
            except:
                print("Invalid Optin! Enter again.")
                print("----------------------------")
        if choice==1:
            name=input("Enter the name of the contact to be searched:")
            search_contact_byname(name)
        elif choice==2:
            phone_no= input("Enter the phone number of the contact to be searched: ")
            search_contact_byphone(phone_no)
        else:
            print("-------------------------------")
    elif option==3:
        add_contact()
    elif option==4:
        name=input("Enter the name of the contact you want to update: ")
        update_contact(name)
    elif option==5:
        name=input("Enter the name of the contact you want to delete: ")
        delete_contact(name)

def write_into_file(name,phone_no,email,address):
    f=open("contactbook.txt","a")
    f.write("Name: "+name+"\n")
    f.write("Phone number: "+phone_no+"\n")
    f.write("Email id: "+email+"\n")
    f.write("Address: "+address+"\n")
    f.write("----------------------------------------------------------------\n")
    f.close()
def add_contact():
     print("Enter the contact details: ")
     name=input("Enter name: ")
     phone_no=input("Enter the phone number: ")
     email=input("Enter the email id: ")
     address=input("Enter the address: ")
     write_into_file(name,phone_no,email,address)
     print("Contact added successfully!")
     print("----------------------------------------------------------------")
def display_contacts():
    f=open("contactbook.txt","r")
    lines= f.readlines()
    i=0
    j=3
    iterator_no=1
    if len(lines)==0:
        print("No contacts found!")
    else:
        for line in lines:
            if j==0:
                print("----------------------------------------------------------------")
                i=0
                j+=1
            if i<2:
                if i==0:
                    print(iterator_no," )", line.strip())
                    iterator_no+=1
                else:
                    print("    ",line.strip())
                i+=1
                j=3
            else:
                if j>0:
                    f.readline()
                    j-=1
    print("----------------------------------------------------------------")
    f.close()
def search_contact_byname(name):
    f=open("contactbook.txt","r")
    flag_found=0
    for line in f:
        words=line.split()
        if name in words:
            print("Contact found!")
            print(f"The contact details of {name} are: ")
            flag_found=1
            print(line.strip())
            for i in range(3):
                print(f.readline().strip())
            print("-------------------------")
            break
    if flag_found==0:
        print("Contact not found!")
        print("------------------")
    f.close()
def search_contact_byphone(phone_no):
    f=open("contactbook.txt","r")
    flag_found=0
    prev_line=""
    for line in f:
        if phone_no in line:
            print("Contact found!")
            print("The contact details of the given phone number are: ")
            flag_found=1
            print(prev_line)
            print(line.strip())
            for i in range(3):
                print(f.readline().strip())
            break
        prev_line=line.strip()
    if flag_found == 0:
        print("Contact not found!")
    f.close()
def search(name):
    f=open("contactbook.txt","r")
    flag_found=0
    for line in f:
        if name in line:
            flag_found=1
            break
    f.close()
    if flag_found==0:
        return 0
    else:
        return 1
def update_contact(name):
    if not search(name):
       print("Contact not found!")
       print("------------------")
    else:
        f=open("contactbook.txt","r")
        lines=f.readlines()
        f.close()
        f=open("contactbook.txt","w")
        bool_flag=False
        i=0
        for line in lines:
            if bool_flag==True and i<4:
                i+=1
                continue
            bool_flag=False
            if name in line:
                print(f"Enter the updated details for {name}: ")
                phone_no=input("Enter the phone number: ")
                email=input("Enter the email id: ")
                address=input("Enter the address: ")
                f.write("Name: "+name+"\n") 
                f.write("Phone number: "+phone_no+"\n")
                f.write("Email id: "+email+"\n")
                f.write("Address: "+address+"\n")
                f.write("----------------------------------------------------------------\n")
                bool_flag=True
            else:
                f.write(line)
        f.close()
        print("Contact updated successfully!")
        print("----------------------------------------------------------------")
def delete_contact(name):
    if not search(name):
        print("Contact not found!")
        print("------------------")
    else:
        f=open("contactbook.txt","r")
        lines=f.readlines()
        f.close()
        f=open("contactbook.txt","w")
        bool_flag=False
        i=0
        for line in lines:
            if bool_flag==True and i<4:
                i+=1
                continue
            bool_flag=False
            if name in line:
                bool_flag=True
            else:
                f.write(line)
        f.close()
        print("Contact deleted successfully!")
def main():
    print("----------------------------------------------------------------")
    print("                   CONTACT BOOK APPLICATION                     ")
    print("----------------------------------------------------------------")
    while True:
        option = option_input()
        if option==6:
            print("                          THANK YOU! ")
            print("----------------------------------------------------------------")
            break
        perf_operations(option)
        print("Enter the option number again to continue:")
if __name__ == "__main__":
    main()