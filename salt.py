import random
import string
import hashlib

def make_salt():
    return "".join(random.choice(string.letters) for x in xrange(5))
 
def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()

    return '%s,%s' % (h, salt)
    
print make_pw_hash('daniel', 'shotonwa')


def valid_pw(name, pw, h):
    salt = h.split(',')[1]

    return h == make_pw_hash(name, pw, salt)
    
h = make_pw_hash('daniel', 'shotonwa')
print valid_pw('daniel', 'shotonwa', h)
