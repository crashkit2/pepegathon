f = open('website-access.log', 'r')

for line in f:
    print (line.split(' ')[9])