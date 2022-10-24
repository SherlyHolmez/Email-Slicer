def main():

    email_input = input("Please insert your email address:")

    if email_input == "exit" or email_input == "Exit":
        exit()

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    print("")
    print("Username: " + username)
    print("Domain: " + domain)
    print("Extension: " + extension)
    print("")
    print("----------------------------------------------")

print("Welcome to the email slicer")
print("")
while True:
    main()