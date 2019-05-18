f = open('website-access.log.1', 'r')

for line in f:
    print (line.split(' ')[9])