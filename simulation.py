import numpy as np
import random

#number of services to take into account for the estimate
n = int(input("number of services: "))
#input for the ith service's requierd bandwidth
service_bw = []
service_bw.extend(int(i) for i in input("required bandwidth for each service (bps): ").split())
#number of simultaneous users
users = int(input("number of users: "))
#timeline length
length = int(input("discrete timeline length: "))

#simulation
iterations = 30
alpha = 3
mean = alpha/(alpha-1)
ans = []
for k in range(iterations):
    samples=[np.random.pareto(alpha, length) for _ in range(10)]
    results = [0 for _ in range(length)]
    for j in range(length):
        for i in range(10):
            if samples[i][j] > mean:
                results[j] += service_bw[random.randrange(0,n)]
    ans.append(max(results))

avg = 0
for i in range(iterations):
    avg += ans[i]
avg /= iterations
req_bw = avg/1e7

print(f"{req_bw} Mbps")