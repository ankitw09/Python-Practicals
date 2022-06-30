# each character freq in an inputed string

teststring = input()

all_freq = {}
  
for i in teststring:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1


print(all_freq)