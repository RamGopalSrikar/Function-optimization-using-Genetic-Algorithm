# -*- coding: utf-8 -*-
import numpy as np

def crossover(p1,p2,gamma=0):
    c1=p1.deepcopy()
    c2=p2.deepcopy()
    alpha=np.random.uniform(-gamma,1+gamma)
    c1.value[0]=p1.value[0]*alpha+(1-alpha)*p2.value[0]
    c1.value[1]=p1.value[1]*alpha+(1-alpha)*p2.value[1]
    c2.value[0]=p2.value[0]*alpha+(1-alpha)*p1.value[0]
    c2.value[1]=p2.value[1]*alpha+(1-alpha)*p1.value[1]

    return c1,c2
