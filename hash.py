import hashlib

import hmac

SECRET = "LetsGo"
def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return '%s,%s' % (s, hash_str(s))

def check_secure_val(h):
    s = h.split(',')[0]
    if h == make_secure_val(s):
        return s

print hash_str('dan')
