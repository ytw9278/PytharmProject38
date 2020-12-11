import random

ranlist = ['python', 'c', 'ruby', 'cisco']
n1 = random.choice(ranlist)
n2 = random.sample(ranlist, 2)
print(n1, n2, sep='\n')

ip1 = random.randint(0, 255)
ip2 = random.randint(0, 255)
ip3 = random.randint(0, 255)
ip4 = random.randint(0, 255)
random_ip = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)
print(random_ip)

s = 'fuck tangwei'
z = s.upper()
yy = z.lower()
print(z)
print(yy)
