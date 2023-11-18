import random
def password_generator(pass_len):
    lowercase_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','v','t','u','w','x','y','z']
    uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O', 'P','Q','R','S','V','T','U','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    special_letters=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|',';',':','<','>','/','?','~']
    password = []
    while len(password) < pass_len:
        lowercase_letter = random.choice(lowercase_letters)
        uppercase_letter = random.choice(uppercase_letters)
        number = random.choice(numbers)
        special_letter = random.choice(special_letters)
        characters = [lowercase_letter,uppercase_letter,number,special_letter]
        random_characters = random.choice(characters)
        password.append(random_characters)
    return password

def inp_passlen():
    flag =True
    again_flag = False
    while(flag):
        try:
            if again_flag==True:
                pass_len= int(input("Enter the length of the password again: "))
                if pass_len<4 :
                    print("Password length must be greater than 3.")
                    continue
                flag =False
            else:
                pass_len= int(input("Enter the length of the password: "))
                if pass_len<4 :
                    print("Password length must be greater than 3.")
                    continue
                flag =False
        except ValueError:
            print("Invalid Input! ")
            again_flag=True
    return pass_len

def print_pass(password,pass_len):
    print("Your password of length ",pass_len," is :",''.join(password))

def main():
    print("-----------------------------------------------")
    print("      WELCOME TO THE PASSWORD GENERATOR")
    print("-----------------------------------------------")
    pass_len = inp_passlen()
    password = password_generator(pass_len)
    print_pass(password,pass_len)
    print("-----------------------------------------------")
    print("                 THANK YOU! ")
    print("-----------------------------------------------")
if __name__ == "__main__":
    main()