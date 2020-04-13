# -*- coding: utf-8 -*-
import numpy as np

def mutate(C,mu=0.1):
    Cm=C.deepcopy()
    Cm.value[0]=C.value[0]+mu*np.random.randn(1)
    Cm.value[1]=C.value[1]+mu*np.random.randn(1)
    return Cm
