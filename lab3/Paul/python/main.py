import numpy as np
import math
import functions as fct
import csv

with open('final_3_20.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    l=3
    n=20
    n_mac=100
    probs = np.random.random(n)
    probs /= probs.sum()
    probs_un=np.empty(n)
    probs_un.fill(1.0/n)
    probs_d=np.random.dirichlet(np.ones(n)/10,size=1)[0]
    H=-sum(p*math.log(p,2) for p in probs)
    Hun=-sum(p*math.log(p,2) for p in probs_un)
    #print "H=" + str(H) + " and Hd=" + str(Hd) + " with Hun =" +str(Hun)
    #print "H=" + str(H) + " and Hd=" + str(Hd) + " with Hun =" +str(Hun)







    for k in range(1,150) :

        probs_d=fct.compute_probsd(n,n_mac,1.0/k)
        Hd=-sum( 0 if p<=0 else p*1.0/n_mac*math.log(p*1.0/n_mac,2) for p in probs_d)
        n_inf=fct.compute_propag(probs_d,l,n_mac)
        writer.writerow([Hd,n_inf])
        print k/6


    for aa in range(0,30):
        for k in range(1,10) :

            probs_d=fct.compute_probsd(n,n_mac,1.0/k)
            Hd=-sum( 0 if p<=0 else p*1.0/n_mac*math.log(p*1.0/n_mac,2) for p in probs_d)
            n_inf=fct.compute_propag(probs_d,l,n_mac)
            writer.writerow([Hd,n_inf])
            print (aa*10+150+k)/6


    for k in range(1,150) :

        probs_d=fct.compute_probsd(n,n_mac,k)
        Hd=-sum( 0 if p<=0 else p*1.0/n_mac*math.log(p*1.0/n_mac,2) for p in probs_d)
        n_inf=fct.compute_propag(probs_d,l,n_mac)
        writer.writerow([Hd,n_inf])
        print (k+450)/6


