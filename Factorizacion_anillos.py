from math import log

def descomposion(n): #devuelve la descomposicion de un numero inmpar en la forma m*2^k
  m=n-1
  k=0
  while m%2==0:
    m=m/2
    k+=1
  print("n-1=",n-1,"=",m,"*2^",k)
  return m,k

def testigo_MR(n,m,k,a): #devuelve si a es testido de Miller-Rabin de n, asume que n impar y mcd(a,n)=1
  print("1:",pow(a,m)%n)
  if pow(a,m)%n==1:
    return False
  for i in range(k):
    print("2-:i=",i,"-",pow(a,pow(2,i)*m)%n)
    if pow(a,pow(2,i)*m)%n==n-1:
      return False
  return True

def test_prim_MR_deter(n):  #test primalidad de Miller_Rabin deterministico
  m, k = descomposion(n)
  i=2
  while i<(1+(n-1)/4):
    print("Testigo ",i)
    if testigo_MR(n,m,k,i):
      return False
    i+=1
  return True

def test_prim_MR_prob(n, alfa): #test primalidad de Miller_Rabin probabilistico
  m, k = descomposion(n)
  l = int(log(alfa)/log(1/4))
  i=2
  while i<=l:
    print("Testigo ",i)
    if testigo_MR(n,m,k,i):
      return False
    i+=1
  return True

