# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import numpy as np
from crossover import crossover
from mutate import mutate
from parent_selection import rand_parentsel
def ga_first(pop_gen,best_value,problem,param):
    
    #porblem paramter extraction
    cost_func=problem.cost_func
    varmin=problem.varmin
    varmax=problem.varmax
    
    #param
    niter=param.niter
    npop=param.npop
      
    best_costsam=best_value.deepcopy()
    bestsol=np.empty(niter)
    avg_list=np.empty(niter)
    
    for i in range(niter):
        
        popc=[]
        popp=[]
                   
        for j in range(npop//2):
            
            #parent selection
            
            p1,p2=rand_parentsel(pop_gen,npop)
            #generating offpring
            c1,c2=crossover(p1,p2)
            #mutate the offspring
            c1m=mutate(c1)
            c2m=mutate(c2)
            apply_bounds(c1m,varmin,varmax)
            apply_bounds(c2m,varmin,varmax)
            #cost value calculation of children
            c1m.cost=cost_func(c1m.value[0],c1m.value[1])
            if c1m.cost>best_costsam.cost:
                    best_costsam=c1m.deepcopy()
            c2m.cost=cost_func(c2m.value[0],c2m.value[1])
            if c2m.cost>best_costsam.cost:
                    best_costsam=c2m.deepcopy()
            
            popc.append(c1m)
            popc.append(c2m)
            
            popp.append(p1)
            popp.append(p2)
            
            
        #ranking model
        pop_gen=popc+popp
        pop_gen=sorted(pop_gen, key=lambda x: x.cost)
        pop_gen=pop_gen[npop-1:-1]
        avg=0
        for j in range(npop):
            avg=avg+pop_gen[j].cost
        avg=avg/npop
        avg_list[i]=avg
        bestsol[i]=best_costsam.cost
        best_value=best_costsam.deepcopy()
        
        #best cost
        #print('generation {} is {} and avg is {} '.format(i+1,bestsol[i],avg_list[i]))
        
    
    return bestsol,avg_list,best_value
            
def apply_bounds(x,varmin,varmax):
    x.value[0]=np.maximum(x.value[0],varmin[0])
    x.value[1]=np.maximum(x.value[1],varmin[1])
    x.value[0]=np.minimum(x.value[0],varmax[0])
    x.value[1]=np.minimum(x.value[1],varmax[1])
    
    
        
    
    
    


    

    
    
    

