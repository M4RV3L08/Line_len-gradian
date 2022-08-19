import os , math

os.system('cls')

class Line:
    def __init__(self,a,b) : 
        self.a = {'x': a[0] , 'y':a[1]}
        self.b = {'x': b[0] , 'y':b[1]}
 
    def __str__(self) :
        return f"Line spots :A({self.a['x']},{self.a['y']})  B({self.b['x']},{self.b['y']})"

    def line_len (self):
        return math.sqrt(((self.b['y'] - self.a['y']) ** 2) + ((self.b['x'] - self.a['x']) **2))

    def line_gradian(self):
        return (self.b['y'] - self.a['y']) / (self.b['x'] - self.a['x'])

        
X1 = float(input("Enter X1 :")) 
Y1 = float(input("Enter Y1 :"))
X2 = float(input("Enter X2 :"))
Y2 = float(input("Enter Y2 :"))

line1 = Line((X1,Y1),(X2,Y2))

print(line1)
print(f'Line lengath is :{line1.line_len()}')
print(f'Line Gradian is :{line1.line_gradian()}')