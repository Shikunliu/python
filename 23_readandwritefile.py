fw = open('sample.txt', 'w')
fw.write('Writing to my yexy file\n')
fw.write('I like bacon\n')
fw.close()

fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()