def f(N):
 if N ==2:
  return 2
 elif N == 1:
  return 1
 else:
  return F(N-1)+F(N-2)

def F(N):
 if len(m) >= N:
  return m[N]
 else:
  m[N] = f(N)
  return m[N]

def Fib(N):
 if N ==2:
  return 2
 elif N == 1:
  return 1
 else:
  return Fib(N-1)+Fib(N-2)

m={}
sum=0
for i in range(1,100):
 if F(i) > 4000000:
  break
 else:
  print i, " ", F(i)
for j in range(1,i):
 if 0 == F(j) % 2:
  sum+=F(j)
  print j, " ", F(j), " " , sum
print sum
