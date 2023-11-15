import time
import string

class Encryption(object):
    def __init__(self, text, keyLength, firstWordLength):
        self.text = str(text)
        self.keyLength = int(keyLength)
        self.firstWordLength = int(firstWordLength)

def Decryption(text, keyLength):
    decrypted = ""
    for n in range(0, len(text), 1):
        decrypted += chr((((ord(text[n]) - 97) - ((ord(keyLength[n % len(keyLength)])) - 97)) % 26) + 97)
    return decrypted.upper()

def passwordCracker(cipherText, keyLength, firstWordLength):
    plainText = ""
    possibleFirstWords = {}
    possibleKeys = dict.fromkeys(string.ascii_uppercase, 1)
    firstRun = True   
    cryptFirstWord = cipherText[:int(firstWordLength)]
    dictFile = open('dict.txt', 'r')
    for line in dictFile:
        if (len(line.rstrip()) == firstWordLength):
            possibleFirstWords[line.rstrip()] = 1
    startTime = time.process_time()
    for i in range(keyLength):
        tempKeys = {}
        possibleNKeys = {}
        for currentWord in possibleFirstWords:
            possibleNKeys[currentWord[:i + 1]] = 1
        if firstRun:
            for key in possibleKeys.keys():
                if Decryption(cryptFirstWord[i], key) in possibleNKeys:
                    tempKeys[key] = 1
            firstRun = False         
        else:
            for key in possibleKeys.keys():
                for j in string.ascii_uppercase:
                    if Decryption(cryptFirstWord[:i + 1], (key + j)) in possibleNKeys:
                        tempKeys[(key + j)] = 1
        possibleKeys = tempKeys
    for currentKey in possibleKeys.keys():
        decrypted = Decryption(cryptFirstWord, currentKey)
        if decrypted in possibleFirstWords:
            print("Key: " + currentKey)
            print("Decrypted Message: " + Decryption(cipherText, currentKey))
    endTime = time.process_time() - startTime
    print("Time to decrypt the message in seconds:", endTime, "\n")


encryptedMessage = []     
encryptedMessage.append(Encryption("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", 2, 6))        
encryptedMessage.append(Encryption("PSPDYLOAFSGFREQKKPOERNIYVSDZSUOVGXSRRIPWERDIPCFSDIQZIASEJVCGXAYBGYXFPSREKFMEXEBIYDGFKREOWGXEQSXSKXGYRRRVMEKFFIPIWJSKFDJMBGCC", 3, 7))
encryptedMessage.append(Encryption("MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA", 4, 10))       
encryptedMessage.append(Encryption("SQLIMXEEKSXMDOSBITOTYVECRDXSCRURZYPOHRG", 5, 11))     
encryptedMessage.append(Encryption("LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS", 6, 9))     
encryptedMessage.append(Encryption("VVVLZWWPBWHZDKBTXLDCGOTGTGRWAQWZSDHEMXLBELUMO", 7, 13))
for x in encryptedMessage:
    print("Encrypted Message:", x.text)
    print("Key Length:", x.keyLength)
    print("First Word Length:", x.firstWordLength)
    passwordCracker(x.text, x.keyLength, x.firstWordLength)
