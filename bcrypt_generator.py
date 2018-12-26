"""Simple bcrypt generator script in python by Martin Sooväli."""
import bcrypt
input_file = 'passwords'
output_file = 'hashes'


def generate_salts():
    """Generate salts and hashes from passwords file. Save into hashes file"""
    with open(input_file) as ip_file:
            data = ip_file.readlines()
    with open(output_file, 'w') as op_file:
        op_file.write(f"SALTS{26 * ' '}|  PASSWORDS\n")
        for password in data:
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password.encode('utf8'), salt)
            op_file.write(f"{salt.decode('utf8')}  |  {password_hash.decode('utf8')}\n")


if __name__ == "__main__":
    generate_salts()
