"""
Formula :
sum of n continous numbers is (N*N+1)/2

And therefore if two number i.e. lower bound and upperbound is given then it is 
sumofUpperBound - sumoflowerbound
So N1, N2 and sum of numbers between N1 and N2 is 

(N2*N2+1)/2  -  ((N1*N1+1)/2)+N1

"""
n = 4
a = [i for i in range(1,n+1)]


# for i, j in zip(range(n), range(n,0,-1)):
#     print(i,j, sum([range()]))

for i in range(1,n+1):

    lhs = i*(i)/2
    upper_sum = n*(n+1)/2

    rhs = upper_sum - (lhs)

    print(i, lhs, rhs)

