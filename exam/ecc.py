class Ecc:
  def __init__(self, field) :
    self.p = field

  def isPointOnEcc(self, p) :
    # left = y**2 % p
    # right = x**3+7 % p
    x,y = p
    left = pow (y, 2, self.p)
    right = (pow (x, 3) + 7) % self.p
    return (left == right)

  # according to https://eng.paxos.com/blockchain-101-foundational-math,
  def add(self,x,y) :
    return (x+y)%self.p

  def sub(self,x,y) :
    return (x-y)%self.p
    
  def mul(self,x,y) :
    return (x*y) % self.p
    
  def div(self,x,y) :
    # x/y = x * (y**p-2)
    return (x * pow(y, self.p-2, self.p)) % self.p

  def addPoints(self,p1,p2) :
    x1,y1 = p1
    x2,y2 = p2
    s = self.div( (y2-y1),(x2-x1) )
    x3 = (s**2-x1-x2)%self.p
    y3 = (s*(x1-x3)-y1)%self.p
    return (x3,y3)
    
  def createGroup(self,p) :
    x,y = p
    group = [p]
    newPoint = p
    while True :
      newPoint = self.addPoints(p,newPoint)
      print(newPoint)
      group.append(newPoint)
      if (newPoint==(0,0)) :
        print ("breaking..")
        break
      
    return group
