def extract_domain(email):
    return email.split('@')[1]

email = "user@example.com"
print(extract_domain(email))




def replace_multiple_spaces(s):
    return " ".join(s.split())

s = "This   is  a  test."
print(replace_multiple_spaces(s))
