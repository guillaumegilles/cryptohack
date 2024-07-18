# Modern cryptography involves code, and code involves coding. CryptoHack
# provides a good opportunity to sharpen your skills.

# Of all modern programming languages, Python 3 stands out as ideal for quickly
# writing cryptographic scripts and attacks.

import sys

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))
