import random


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def random_prime():
    while True:
        p = random.randint(1000, 5000)
        if is_prime(p):
            return p


def get_factors(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return factors


def primitive_root_of_p(p):
    n = p - 1
    factors = get_factors(n)
    for g in range(2, p):
        is_primitive_root = True
        for factor in factors:
            if pow(g, n // factor, p) == 1:
                is_primitive_root = False
                break
        if is_primitive_root:
            return g


def test_all():
    print("Testing is_prime():")
    print(is_prime(2))    
    print(is_prime(19))   
    print(is_prime(20))   
    print(is_prime(100))  
    print(is_prime(997))  

    print("Testing random_prime():")
    for _ in range(5):
        print(random_prime())  

    print("Testing get_factors():")
    print(get_factors(12))   
    print(get_factors(28))   

    print("Testing primitive_root_of_p() function:")
    print(primitive_root_of_p(7))    
    print(primitive_root_of_p(11))   
    print(primitive_root_of_p(13))   
    print(primitive_root_of_p(17))   

def testing_encryption():
    p = 1733 
    g = 3     
    e = 1343  
    b = random.randint(1, p - 1)  
    m = 123  
    c1 = pow(g, b, p)
    c2 = (m * pow(e, b, p)) % p
    
    print(f"p = {p}, g = {g}, e = {e}, b = {b}")
    print(f"Plaintext message (m) = {m}")
    print(f"Ciphertext components: c1 = {c1}, c2 = {c2}")
    print(f"Cipher text: ({c1}, {c2})")

def test_decryption():
    c1 = 264
    c2 = 502
    a = 100
    p = 1733 
    x = pow(c1, a, p)  
    x_inverse = pow(x, p - 2, p) 
    decrypted_message = (c2 * x_inverse) % p
    print(f"Decrypted message: {decrypted_message}")
test_decryption()



