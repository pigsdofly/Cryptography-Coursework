"""Solution for question 2"""
import re

def xor_all(dump):
    """XORs both keys with the ciphertext in turn""" 
    i = 0
    key = [175, 190]
    result = ''
    keyval = 0
    #loop through the hex dump two at a time to get each byte
    while i < len(dump)-1:
        hexchr = dump[i] + dump[i+1]
        hexval = int(hexchr, 16)
        result += chr(hexval ^ key[keyval])
        i += 2
        #flip keyval from 0 to 1 or vice versa
        keyval ^= 1
    return result

def count_all(dump):
    """Returns the frequencies of each hex character in the ciphertext, adapted from freq.py for hex values"""
    i = 0 
    count = {}
    total = 0
    while i < len(dump)-1:
        hexchr = dump[i]+dump[i+1]
        if hexchr in count.keys():
            count[hexchr] += 1
        else:
            count[hexchr] = 1
        total += 1
        i+=2

    for letter in sorted(count, key=count.get, reverse=True):
        percent = (float(count[letter]) / float(total)) * 100
        print( "Frequency of %s: %f" % (letter, percent))

if __name__ == "__main__":
    try:
        hex_file = open("51_dump",'r')
        hex_dump = hex_file.read()
        #Use regex to remove extra characters from hex dump, leaving just the hex
        hex_dump = re.sub("[0123456789abcdef]" * 8, '', hex_dump)
        hex_dump = re.sub("[ \n\|\.]", '', hex_dump)
        
        print("Frequencies for ciphertext:\n")
        count_all(hex_dump)

        print("\nDecrypted Plaintext:\n")
        print(xor_all(hex_dump))
    except:
        print("Failed to open file")
