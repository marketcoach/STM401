str = 'X-DSPAM-CONFIDENCE: 0.8475'

ipos = str.find(":")
print(ipos)
piece = str[ipos+1:]
print(piece)
value = float(piece)
print(value)
