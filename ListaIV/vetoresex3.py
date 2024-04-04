import random
vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
	vetor1.append(random.randint(1,100))
	vetor2.append(random.randint(1,100))
	vetor3.append(vetor1[i])
	vetor3.append(vetor2[i])

print ("Vetor I", vetor1);
print ("Vetor II", vetor2);
print ("Vetor III", vetor3);
