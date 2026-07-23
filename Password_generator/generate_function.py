import secrets
import string

def generate_password(length):
    mix = string.ascii_letters + string.digits
    done = ''.join([secrets.choice(mix) for x in range(length)])
    return done