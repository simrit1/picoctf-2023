MOD = 41

def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


final = ''

with open("message.txt") as f:
    nums = [int(x) for x in f.read().rstrip().split(' ')]
    # nums = [1, 26, 27, 36, 37]
    for x in nums:
        x = modinv(x % 41, MOD)
        if x <= 26:
            final += chr(64+x)
        elif x <= 36:
            final += chr(x+(48-27))
        else:
            final += '_'
    print(final)
