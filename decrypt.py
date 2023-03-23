import time
from datetime import datetime


def decrypt(ciphertext, key):
    plaintext = ""  # Initialize an empty string to store the plaintext
    for i in range(0, len(ciphertext)):  # Loop through each character in the ciphertext
        if i % (key + 1) == 0:  # Check if the current index is a multiple of (key + 1)
            plaintext = plaintext + ciphertext[i]  # Add the character at the current index to the plaintext string
    return plaintext  # Return the plaintext string


# Input...
# ciphertext = "YFwoJeELOvlDVrOlNBDConouLwhdCC mkIjsYeKsuaGsDbSRJymLJVOaYNQRrgKBSifPOdnCbUleWCbf"
# key = 4

# ciphertext = "HNABntvVepMaQSNHyKxQTXZf HVbQXcqJSXfswOAuRBzpefOdfBeylimeqDHDlFc"
# key = 7

# ciphertext = "PqKgakYBpfzveAHVrrUgbzpkaMWUcskukxac QfsWpFSrTrwiaQRtSsXesGlrBqv"
# key = 3

# ciphertext = "HXelrEed fCxojmVersu Gtehvee NSluGnJ"
# key = 1

# ciphertext = "PHcRrveeRUmDnfqMFAnBJvvwyzSDrj tqXhrLRXIegaDLwdInIGCvqelcjzU"
# key = 5

# ciphertext = "CaLbsilDbelGGgb RbbSAWPZgcOsdVavIdSdxxfVeHQtvmJxDfyCYwo"
# key = 4

# ciphertext = "pcxzGsKfyLKdZRObtAwohNmWhlbFnIJiofcYDeWjnNOFpdYUiqeLVqcKsUXJWeYttITQzGpFaILWQkRU!BwhehCh"
# key = 7

def take_user_input():
    ciphertext = input("Enter a ciphertext to decode or 'q' to exit: ")
    if ciphertext == "q" or ciphertext == "Q":
        exit()
    key = None
    try:
        key = int(input("Enter a key as a number between 1 and 10: "))
    except:
        print("Please enter a number")
        print("")
        take_user_input()
    while True:
        if key not in range(1, 10):
            print("You entered a wrong key")
            take_user_input()
        start_time = datetime.now()
        plain_text = decrypt(ciphertext, key)
        end_time = datetime.now()
        print("=" * 20)
        print("plain_text:\t", plain_text)
        time_elapsed = (end_time - start_time).total_seconds()
        if time_elapsed > 60:
            minutes, seconds = divmod(time_elapsed, 60)
            print(f"Time taken to complete decryption is  {int(minutes)} minutes, {seconds:.2f} seconds")
        else:
            print(f"Time taken to complete decryption is  {(end_time - start_time).total_seconds()} seconds")
        print("=" * 20)
        take_user_input()


take_user_input()


# Process...
# print("...")
# time.sleep(1)
# print("Decrypting ciphertext...")
# time.sleep(1)
# print("...")
# time.sleep(1)
# plaintext = decrypt(ciphertext, key)
#
# # Output...
# print("Plaintext:")
# print(plaintext)
