import time


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

ciphertext = "pcxzGsKfyLKdZRObtAwohNmWhlbFnIJiofcYDeWjnNOFpdYUiqeLVqcKsUXJWeYttITQzGpFaILWQkRU!BwhehCh"
key = 7

# Process...
print("...")
time.sleep(1)
print("Decrypting ciphertext...")
time.sleep(1)
print("...")
time.sleep(1)
plaintext = decrypt(ciphertext, key)

# Output...
print("Plaintext:")
print(plaintext)
