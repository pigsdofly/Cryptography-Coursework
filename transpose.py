"""Script that uses command line argument to break up transposed ciphertext into columns"""
from sys import argv

#hardcoded value for the ciphertext
tpose_string = "teahrlifuehrkeadsigeltmtnurysblttpaoplauaaaumcrgncetehcsitanmhsueunird" 

if len(argv) <= 1:
    print("Not enough arguments")
else:
    column_len = int(argv[1])
    height = int(len(tpose_string) / column_len)
    columns = [""] * height
    iter = 0
    for t in tpose_string:
        if iter == height:
            iter = 0
        columns[iter] += t
        iter += 1
    
    for c in columns:
        print(c)