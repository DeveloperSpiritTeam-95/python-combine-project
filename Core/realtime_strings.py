def extract_domain(email):
    return email.split('@')[1]

email = "user@example.com"
print(extract_domain(email))


# validate ip address
import re

def is_valid_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return bool(pattern.match(ip))

ip = "192.168.1.1"
print(is_valid_ip(ip))


def remove_duplicates(s):
    return "".join(sorted(set(s), key=s.index))

s = "hello world"
print(remove_duplicates(s))


def is_only_digits(s):
    return s.isdigit()

s = "123456"
print(is_only_digits(s))


def replace_multiple_spaces(s):
    return " ".join(s.split())

s = "This   is  a  test."
print(replace_multiple_spaces(s))
