#!/usr/bin/python

#Diffie-Hellman Key Cryptographic key exchange in python
#Before using this program, ensure that you have exchanged
#The prime modulus and base with your partner
import time
def IntChecker(n): #Function for checking if secret is an integer
	intn = int(n)
	if(intn == n):
		return 1
	else:
		return 0

def PrimeChecker(n): #Function for checking if mod and base are prime
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return 1    
    if not n & 1: 
        return 0
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return 0
    return 1

#introduction
print ""
print "*********************************"
print "*  Diffie-Hellman Key Exchange  *"
print "*  ---------------------------  *"
print "*    Authored by Jack Renshaw   *"
print "*********************************"
print ""

base = input("Enter your shared prime base: ") #Request user for (shared) prime base
modulus = input("Enter your shared prime modulus: ") #Request user for (shared) prime modulus 
secret = input("Please enter your secret key: ")

#Run the secret, mod and base through the functions
if(PrimeChecker(base) != 1):
	print "Your base is not prime..."
	exit()
if(PrimeChecker(modulus) != 1):
	print "Your modulus is not prime..."
	exit()
if(IntChecker(secret) != 1):
	print "Your secret is not an integer..."
	exit()

print "calculating result..." #Really stupid and gimmicky
time.sleep(2)

print "Share this result with your partner: ", base**secret % modulus #Calculate the result
print ""
uresult = input("Please enter your partners result: ") #Request user for partners result
print "calculating shared key..." #Stupid and gimmicky
time.sleep(2)
print "Your shared secret key is: ", uresult**secret % modulus #Calculate the shared secret from partners function result and your secret key
print ""

print "Congralutations, you can now communicate in secret" #finitto
print ""