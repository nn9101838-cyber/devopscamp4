import os
import socket
import datetime
import getpass

print("=== SYSTEM INFO ===")
print("Time:", datetime.datetime.now())
print("Hostname:", socket.gethostname())
print("Current Files:", os.listdir())

try:
    user = os.getlogin()
except Exception:
    try:
        user = getpass.getuser()
    except Exception:
        user = os.environ.get('USER', 'root')

print("User:", user)
