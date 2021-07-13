text = "X-DSPAM-Confidence: 0.8475"
start = text.find("0")
print(start)

end = text.find('5')
print(end + 1)

value = float(text[20:26])
print(value)


