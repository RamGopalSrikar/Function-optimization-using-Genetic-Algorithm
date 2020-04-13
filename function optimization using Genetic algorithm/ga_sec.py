# -*- coding: utf-8 -*-
import numpy as np
from crossover import crossover
from mutate import mutate
from parent_selection import fitness_prob
from parent_selection import tournament_sel
from parent_selection import rand_tournamet_fitness
def ga_sec(pop_gen,best_value,problem,param):
    
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
        cost_sum=0
        cost_prob=[]
        s=0
        for j in range(npop):
            cost_sum+=pop_gen[j].cost
        for k in range(npop):
            s=s+(pop_gen[k].cost/cost_sum)
            cost_prob.append(s)
            
        for j in range(npop//2):
            
            #parent selection
            p1,p2=fitness_prob(pop_gen,npop,cost_prob)
            #generating offpring
            c1,c2=crossover(p1,p2,0.2)
            #mutate the offspring
            c1m=mutate(c1,0.3)
            c2m=mutate(c2,0.3)
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
    
    
        
    
    
    


    

    
    
    