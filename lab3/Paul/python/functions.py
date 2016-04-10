import numpy as np
import networkx as nx
import math
def compute_propag(probs,l,n_mac):

    n_iters=100
    n=len(probs)
    nums_m=np.empty(n_mac)
    sum=0
    for iters in range(0, n_iters):
        count=0
        for version in range(0,n):

            G=nx.empty_graph()
            p=probs[version]*1.0/n_mac
            n_sel=max(probs[version]-1,0)
            nums_m.fill(0)
            nums_m[0]=1
            for i in range(0,n_sel):
                k=np.random.randint(n_mac)
                while nums_m[k]==1:
                     k=np.random.randint(n_mac)
                nums_m[k]=1


            for i in range(0,n_mac):
                G.add_edge(i,i)
                for j in range(0,l):
                    k=np.random.randint(n_mac)
                    if nums_m[k]==1 and nums_m[i]==1:
                        G.add_edge(i,k)


            for i in range(0,n_mac):
                if nx.has_path(G,0,i):
                    count+=p

        sum+=count


    return sum/n_iters

def compute_probsd(n,n_mac,k):
    probs_d=[int(round(a)) for a in np.random.dirichlet(np.ones(n)*k,size=1)[0]*100]
    d=n_mac-sum(probs_d)
    c=np.random.randint(n)
    while probs_d[c]+d < 0:
        c=np.random.randint(n)
    probs_d[c]+=d

    return probs_d
