import random
def key_generation():
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

    p = random_prime()
    g = primitive_root_of_p(p)
    a = random.randint(2,p-1)
    e = pow(g,a,p)
    print(f" p = {p}   g = {g}  e = {e} a = {a}")
    print(f"public key: ({p,g,e})")

def encryption():
    p = int(input("Enter the p: "))
    g = int(input("Enter the g: "))
    e = int(input("Enter the e: "))
    b = random.randint(1,p-1)
    
    while True:
     m = int(input(f"what do you want to encrypt (m less than {p}): ")) 
     if m<p:
        break
     print(f"(m) must be less than {p}")
    
    c1 = pow(g,b,p)
    c2 = (m * pow(e, b, p)) % p
    print(f"c1 = {c1} c2 = {c2}")
    print(f"Cipher text: ({c1,c2})")

def decryption():
    c1 = int(input("Enter c1: "))
    c2 = int(input("Enter c2: "))
    a = int(input("Enter the private key (a): "))
    p = int(input("Enter the prime number (p): "))
    x = pow(c1, a, p)
    x_inverse = pow(x, p - 2, p)
    m = (c2 * x_inverse) % p
    print(f"The decrypted message is: {m}")

def main():
    print("Choose an option:")
    print("1. key generation")
    print("2. Encode")
    print("3. Decode")
    
    choice = input("Enter your choice (1 or 2 or 3): ")
    if choice == "1":
        return(key_generation())
    elif choice == "2":
        return(encryption())
    elif choice == "3":
        return(decryption())
    else:
        print("run again and choose (1 or 2 or 3)")
main()        
        
        

    