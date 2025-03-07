import random

def get_random_code(length):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join([random.choice(chars) for i in range(length)])
