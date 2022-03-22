# Write a program that reads in a text file and outputs the number of e's it contains
# author:Regina Fennessy

#filename = 'moby-dick.txt'

#with open(filename, 'r') as f:
    #f.write("The number os e is : ")

fname = input("Moby-Dick.txt")
l=input("e")
k = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1
print("Occurrences of the letter:")
print(k)