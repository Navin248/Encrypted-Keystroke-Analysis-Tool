from cryptography.fernet import Fernet
import re

# Encryption key(generate your own)
key = b''
cipher = Fernet(key)

# Encrypted content inside quotes
encrypted = b""

# Decrypt the content
decrypted = cipher.decrypt(encrypted).decode()

# Filter out text patterns like [cmd], [caps_lock], etc., but keep spaces intact
filtered_text = re.sub(r"\[.*?\]", "", decrypted)

print(filtered_text)
