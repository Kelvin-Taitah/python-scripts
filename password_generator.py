import string, random
c=string.ascii_letters +string.digits +string.punctuation
def gen_rand_pass():
    p=[]
    l=int(input("Enter the length of password: "))
    for i in range(l):
        p.append(random.sample(c, l))
    random.shuffle(p)
    print("".join(random.choice(p)))
gen_rand_pass()