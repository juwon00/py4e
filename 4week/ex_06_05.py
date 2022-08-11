str = 'X-DSPM-Confidence: 0.8475'

lpos = str.find(':')
host = str[lpos+1 :]
value = float(host)

print(value)



# str = 'X-DSPM-Confidence: 0.8475'
#
# ipos = str.find(':')
# piece = str[ipos+2:]
# value = float(piece)
# print(value)
