import math
#return eucledian distance
def distance(p,q):
  return math.sqrt(math.pow(p[0]-q[0],2)+ math.pow(p[1]-q[1],2))

def minDistanceRec(Px,Py):
  s=len(Px)
  #if only 2 or 3 points are left use brute force method
  if (s==2):
    return distance(Px[0],Px[1])
  elif(s==3):
    return min(distance(Px[0],Px[1]),distance(Px[1],Px[2]),distance(Px[2],Px[0]))
  
  #dividing from the middle
  m=s//2
  Qx=Px[:m]
  Rx=Px[m:]
  #min value
  xR=Rx[0][0]

  









def minDistance(Points):
  Px = sorted(Points)
  Py = Points
  Py.sort(key=lambda x: x[-1])
  #print(Px,Py)
  return Px,Py



pts =  [(2, 15), (40, 5), (20, 1), (21, 14), (1,4), (3, 11)]
result = minDistance(pts)
print(result)