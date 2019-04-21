from sys import argv

def frequency_analysis( ct ):
    """ Prints an ordered list of letters and frequencies (in %) """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    frequencies = {}
    total = 0
    for a in alphabet: 
        frequencies[a] = 0
    
    for c in ct.lower():
        if str.isalnum(c):
            frequencies[c] += 1 #iterate the frequency value for a letter if it shows up
            total += 1
            
    #Sort the dictionary so that the letter with the highest number of occurrences appears at the top
    for letter in sorted(frequencies, key=frequencies.get, reverse=True):
        percent = (float(frequencies[letter]) / float(total)) * 100
        print( "Frequency of %s: %f" % (letter, percent))

if __name__ == "__main__":

    if len(argv) <= 1:
        print("not enough args")
    else:
        try:
            ct_file = open(argv[1], 'r')
            ciphertext = ct_file.read()
            frequency_analysis(ciphertext)
            
            ct_file.close()
            
        except:
           print("Failed to open ciphertext file")
