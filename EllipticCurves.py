import random
class ELL_CURVES:
    def __init__(self,a,b,p):
        self.a = a
        self.b = b
        self.p = p
        self.P = [0,0]
        self.s = 0
        self.k = 0 
        self.points = [["INFINITY","INFINITY"]]
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
                    desired_curves.append((a,b))
        if len(set(desired_curves)) == 0:
            return None
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
        for i in range(len(self.points)+1):
            self.scalar_multiple(P,i)
            if self.scalar_multiple(P,i) == ["INFINITY", "INFINITY"]:
                order = i
                break
        return order
    def generator_points(self):
        for point in self.points:
            if self.order_of_point(point) == len(self.points):
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
        while True:
            i = random.randint(0,len(self.points)-1)
            if i != 0:
                self.P = self.points[i]
                random_point = self.points[i]
                break
        return random_point
    def random_s(self):
        self.s = random.randint(1,self.p-1)
        return self.s
    def random_k(self):
        self.k = random.randint(1,self.p-1)
    def gen_public_key(self):
        return self.scalar_multiple(self.P, self.s)
    def encrypt_elgamal(self, D, B,k):
        m1 = self.scalar_multiple(self.P, k)
        m2 = self.addition(D, self.scalar_multiple(B, k))
        return [m1,m2]
    def decrypt_elgamal(self, cipher):
        return self.addition(cipher[1], self.negate_p(self.scalar_multiple(cipher[0], self.s)))

