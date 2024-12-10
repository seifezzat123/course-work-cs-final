import random  # it lets the code to use random numbers
def key_generation():

    def is_prime(number):# Function to check if a number is prime
        if number <= 1:  #  If the numbers less than or equal to 1 are not prime
            return False
        if number == 2:  # 2 is the only even prime number
            return True
        if number % 2 == 0:  # remove even numbers greater than 2
            return False
        for i in range(3, int(number**0.5) + 1, 2):# Check if the number is divisible from 3 to the square root of the number 
            if number % i == 0:
                return False
        return True

    def random_prime(): # Function to generate a random prime number
        while True:
            p = random.randint(1000, 5000)  # Generate a random number in the range
            if is_prime(p):  # Return the number if it is prime
                return p

    def get_factors(n): # Function to find factors of a number
        factors = []
        for i in range(2, int(n**0.5) + 1):# Check if the number is divisible from 2 to the square root of the number 
            if n % i == 0:
                factors.append(i)  # Add the factor to the list
                if i != n // i:
                    factors.append(n // i)  # Add the complementary factor to the list
        return factors

    def primitive_root_of_p(p):# Function to find a primitive root modulo p
        n = p - 1  
        factors = get_factors(n)  # Factors of n
        for g in range(2, p):# Try each number from 2 to p as a primitive root
            is_primitive_root = True
            for factor in factors:
                if pow(g, n // factor, p) == 1:# checks if the factors in this equation is equal to 1 the factor cannot be the primitive root
                    is_primitive_root = False
                    break
            if is_primitive_root:  # Return g if it is a primitive root
                return g

    p = random_prime()  # Generate p as a random prime number
    g = primitive_root_of_p(p)  # Find a primitive root for p
    a = random.randint(2, p - 1)  # Generate a private key (a)
    e = pow(g, a, p)  # Calculate e = g^a mod p
    print(f" p = {p}   g = {g}  e = {e} a = {a}")
    print(f"public key: ({p, g, e})")  # prints the public key

def encryption():
    p = int(input("Enter the p: "))# input the public key of the key generation
    g = int(input("Enter the g: "))
    e = int(input("Enter the e: "))
    b = random.randint(1, p - 1)  # Generate a random private key for encryption


    while True:# checks if the message is less than the prime number
        m = int(input(f"What do you want to encrypt (m less than {p}): ")) 
        if m < p:  
            break
        print(f"(m) must be less than {p}")

    # Compute ciphertext 
    c1 = pow(g, b, p)  # c1 = g^b mod p
    c2 = (m * pow(e, b, p)) % p  # c2 = m * e^b mod p
    print(f"c1 = {c1} c2 = {c2}")
    print(f"Cipher text: ({c1, c2})")  # prints the ciphertext

# Function for decryption
def decryption():
    # Input the ciphertext, prime number and the public key 
    c1 = int(input("Enter c1: "))
    c2 = int(input("Enter c2: "))
    a = int(input("Enter the private key (a): "))
    p = int(input("Enter the prime number (p): "))

    # Decrypt the message
    x = pow(c1, a, p)  # x = c1^a mod p
    x_inverse = pow(x, p - 2, p)  # Compute the mod inverse of x
    m = (c2 * x_inverse) % p  # m = c2 * x_inverse mod p
    print(f"The decrypted message is: {m}")

# Main function to run the program
def main():
    print("Choose an option:")
    print("1. Key generation")
    print("2. Encode")
    print("3. Decode")
    
    choice = input("Enter your choice (1 or 2 or 3): ")
    if choice == "1":
        return key_generation()  # Run key generation
    elif choice == "2":
        return encryption()  # Run encryption
    elif choice == "3":
        return decryption()  # Run decryption
    else:
        print("Run again and choose (1 or 2 or 3)")  # checks the invalid input

main()
