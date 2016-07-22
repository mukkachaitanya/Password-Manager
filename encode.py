import base64

# password = "f7c199a97f90fe7ca09756ab3fc5b01d"
password = None
try:
    password = open(".pwd", "r").read()
except IOError:
    pass

pwd = "G!thuB"


# Source can be found at https://gist.github.com/ilogik/6f9431e4588015ecb194
# A encoding similar to Vigenere cipher

def encode(string, key=pwd):
    encoded_chars = []
    for i in xrange(len(string)):
        key_c = key[i % len(key)]
        # ord() gives the respective ascii value
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string)


def decode(string, key=pwd):
    decoded_chars = []
    # utf-8 to avoid character mapping errors
    string = base64.urlsafe_b64decode(string.encode("utf-8"))
    for i in xrange(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(abs(ord(string[i]) - ord(key_c) % 256))
        decoded_chars.append(encoded_c)
    decoded_string = "".join(decoded_chars)
    return decoded_string
