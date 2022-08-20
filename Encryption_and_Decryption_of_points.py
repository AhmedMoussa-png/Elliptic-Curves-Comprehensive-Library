import random
class ELL_CURVES:
    def __init__(self,a,b,p):
        self.a = a
        self.b = b
        self.p = p
        self.P = [0,0]
        self.s = 0
        self.k = 0 
        self.points = []
        self.generators = []
        self.a_values = []
        self.b_values = []
        self.curves = []
        self.non_singular_curves()
        self.list_of_points()
        #self.random_point()
        #self.random_s()
        self.generator_points()
        #self.random_k()
    def non_singular_curves(self):
        for a in range(self.p):
            for b in range(self.p):
                if 4*(a)**3+27*(b)**2 !=0:
                    self.curves.append((a,b))
                    self.a_values.append(a)
                    self.b_values.append(b)
        return None
    def find_curve(self,n):
        desired_curves =[]
        for a in self.a_values:
            for b in self.b_values:
                if ELL_CURVES(a,b,self.p).number_of_points() == n:
                    desired_curves.append(f"a = {a} and b = {b}")
        return set(desired_curves)
    def discriminant(self):
        return 4*(self.a)**3+27*(self.b)**2 != 0
    def reduce_mod_p(self,x):
        return x%self.p
    def equal_mod_p(self,x,y):
        return (x-y)%self.p == 0
    def invmodP(self, x):
        return pow(x, -1, self.p)
    def list_of_points(self):
        for x in range(self.p):
            for y in range(self.p):
                if self.equal_mod_p(y*y, x**3+self.a*x+self.b):
                    self.points.append([x,y])
        return None
    def number_of_points(self):
        return len(self.points)
    def double(self, P):
        x, y = P[0], P[1]
        P3 = [0,0]
        if x == "INFINITY":
            P3[0] = "INFINITY"
            P3[1] = "INFINITY"
        elif y != 0:
            m = (3*x*x + self.a)*(self.invmodP(self.reduce_mod_p(2*y)))
            P3[0] = self.reduce_mod_p(m*m-2*x)
            P3[1] = self.reduce_mod_p(m*(x-P3[0])-y)
        else:
            P3[0] = 'INFINITY'
            P3[1] = 'INFINITY'
        return P3
    def addition(self,P1,P2):
        x1, y1, x2, y2 = P1[0], P1[1], P2[0], P2[1]
        P3 = [0,0]
        if x1 != "INFINITY" and x2 != "INFINITY":
            if x1 != x2:
                m = (y2-y1)*self.invmodP(x2-x1)
                P3[0] = self.reduce_mod_p(m*m - x1 - x2)
                P3[1] = self.reduce_mod_p(m*(x1-P3[0])-y1)
            elif x1 == x2 and y1 != y2:
                P3[0] = 'INFINITY'
                P3[1] = 'INFINITY'
            elif P1 == P2:
                P3 = self.double(P1)
        elif x1 == "INFINITY" and x2 != "INFINITY":
            P3[0] = x2
            P3[1] = y2
        elif x2 == "INFINITY" and x1 != "INFINITY":
            P3[0] = x1
            P3[1] = y1
        elif x1 == "INFINITY" and x2 == "INFINITY":
            P3[0] = "INFINITY"
            P3[1] = "INFINITY"
        return P3
    def order_of_point(self, P):
        order = 0
        for i in range(len(self.points)):
            self.scalar_multiple(P,i)
            order = order + 1
            if self.scalar_multiple(P,i) == ["INFINITY", "INFINITY"]:
                break
        return order + 1
    def generator_points(self):
        for point in self.points:
            if self.order_of_point(point) == len(self.points)+1:
                self.generators.append(point)
    def scalar_multiple(self, P, m):
        S = P
        binary = list(format(m,"b"))
        for i in range(1,len(binary)):
            S = self.double(S)
            if int(binary[i]) == 1:
                S = self.addition(S,P)
        return S
    def negate_p(self, P):
        if P != ["INFINITY","INFINITY"]:
            return [P[0],self.reduce_mod_p(-P[1])]
        else:
            return ["INFINITY", "INFINITY"]
    def random_point(self):
        i = random.randint(0,len(self.points)-1)
        self.P = self.points[i]
    def random_s(self):
        self.s = random.randint(0,self.p-1)
    def random_k(self):
        self.k = random.randint(0,self.p-1)
    def gen_public_key(self):
        return self.scalar_multiple(self.P, self.s)
    def encrypt_elgamal(self, D, public_key,k):
        m1 = self.scalar_multiple(self.P, k)
        m2 = self.addition(D, self.scalar_multiple(public_key, k))
        return [m1,m2]
    def decrypt_elgamal(self, cipher):
        return self.addition(cipher[1], self.negate_p(self.scalar_multiple(cipher[0], self.s)))

while True:
    decrypt_or_encrypt = input("\nDo you want to encrypt data or decrypt data? e/d/exit ")
    if decrypt_or_encrypt == "e":
    
        a = int(input("\nEnter the a constant for your curve: "))
        b = int(input("\nEnter the b constant for your curve: "))
        p = int(input("\nEnter the prime field: "))
        your_curve = ELL_CURVES(a,b,p)
        
        D = list(map(int,input("\nEnter the data you want as a point on this curve: ").split()))[:2]
        k = int(input("\nEnter your private random integer k less than p for encryption: "))

        public_key_present_or_not = input("\nDo you have the public key of the message receiver? y/n ")
        if public_key_present_or_not == "y":
            public_key = list(map(int,input("\nEnter the coordinates of B: ").split()))[:2]
            your_curve.P = list(map(int,input("\nEnter the coordinates of P: ").split()))[:2]
        else:
            your_curve.random_point()
            your_curve.random_s()
            public_key = your_curve.gen_public_key()
            print(f"Your random point P = {your_curve.P}")
            print(f"Your secret integer s = {your_curve.s}")
            print(f"Your B = sP: {public_key}")
        
        response_encrypt = input("\nDo you want to encrypt your data? y/n ")
        while True:
            if response_encrypt == "y":
                cipher = your_curve.encrypt_elgamal(D, public_key, k)
                print(f"\nYour ciphertext points = {cipher}")
                #print(cipher[0])
                #print(f"your original message = {your_curve.decrypt_elgamal(cipher)}")
                break
            else:
                break
    elif decrypt_or_encrypt == "d":
        a = int(input("\nEnter the a constant for your curve: "))
        b = int(input("\nEnter the b constant for your curve: "))
        p = int(input("\nEnter the prime field: "))
        
        your_curve = ELL_CURVES(a,b,p)
        your_curve.s = int(input("\nEnter your secret random integer s: "))
        
        cipher = [list(map(int,input("\nEnter the coordinates of the first cipher: ").split()))[:2],list(map(int,input("\nEnter the coordinates of the second cipher: ").split()))[:2]]
        
        response_decrypt = input("\nDo you want to decrypt your data? y/n ")
        while True:
            if response_decrypt == "y":
                print(f"\nYour ciphertext points = {cipher}")
                print(f"Your original message = {your_curve.decrypt_elgamal(cipher)}")
                break
            else:
                break
    else:
        break