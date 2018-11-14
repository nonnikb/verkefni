

def get_emails():
    mails = []
    while True:
        i = input("Email address: ")
        if i == "q":
            break
        mails.append(i)
    return mails

def get_names_and_domains(email_list):
    a = []
    for element in email_list:
        split_email = element.split("@")
        a.append(tuple(split_email))
    return a


# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)