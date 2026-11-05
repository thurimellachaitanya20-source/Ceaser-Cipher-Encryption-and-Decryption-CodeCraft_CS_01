Python Implementation (Code)

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ !@#$%^&*'

def caesar_cipher(message, key, mode): result = ""

for ch in message.upper():

if

else:

ch in ALPHABET:

idx = ALPHABET.index(ch)

if mode == "encrypt":

idx = (idx + key) % len(ALPHABET)

else: # decrypt

idx = (idx - key) % len(ALPHABET)

result += ALPHABET[idx]

result += ch return result

while True:

print("\n==== Caesar Cipher ====")

print("1. Encrypt a Message")

print("2. Decrypt a Message")

print("3. Quit")

choice = input("Choose an option (1/2/3): ").strip()

if choice == "3":

print("Goodbye!") break

elif choice not in ["1", "2"]:

try:

print("Invalid choice. Try again.")

continue

key = int(input(f"Enter key (0 to {len(ALPHABET)-1}): ")) if not (0 <= key < len(ALPHABET)): print("Invalid key range.") continue

except ValueError:

print("Key must be a number.") continue

message = input("Enter your message: ") mode = "encrypt" if choice == "1" else "decrypt" result = caesar_cipher(message, key, mode)

print("Result:", result)
