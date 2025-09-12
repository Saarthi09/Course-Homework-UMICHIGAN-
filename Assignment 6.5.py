text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
b = text[23:]
a = b.strip()
c = float(a)
print(c)