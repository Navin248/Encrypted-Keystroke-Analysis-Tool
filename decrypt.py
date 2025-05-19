from cryptography.fernet import Fernet
import re

# Encryption key
key = b'7lGUTamn1KkNneBvSkvLvo_1T5TZrXgh592pFiarJOc='
cipher = Fernet(key)

# Encrypted content
encrypted = b"gAAAAABoEkDNIYZG7dSqhEe_ZfMSJlOsDwNObGkoo-fqxWXX2jBjaRZ8lsI1RpoAyUYfDMDgAakflvKmzaS-_zJeW8FojNDlbDzm5F8GXmRzVpCW3cWy9cwXQv9I-Ya0t8QhLNyGw_HyBBLvMVDbJ0nX1Q7_aQOBLpTHGOQmGxUk7RLkxDxaqraMd0ObnT2LieAhEVeZrexgSqUF697HHjHJGQUcq-23EtQEfRXSj96mx307jHrFY0C1SH3lXlnxVxbQnBU4vwVUBjZ5AQzPo8JSABdraER_3S731sgnfE484fi_BENucOY="

# Decrypt the content
decrypted = cipher.decrypt(encrypted).decode()

# Filter out text patterns like [cmd], [caps_lock], etc., but keep spaces intact
filtered_text = re.sub(r"\[.*?\]", "", decrypted)

print(filtered_text)