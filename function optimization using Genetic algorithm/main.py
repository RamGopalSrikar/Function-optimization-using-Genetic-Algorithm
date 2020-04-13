#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:44:07 2020

@author: srikarkatakam
"""
import numpy as np
from ypstruct import structure
from ga_first import ga_first
from ga_sec import ga_sec
from ga_third import ga_third
#import matplotlib.pyplot as plt

#cost function
def cost_func(x1,x2):
    fitness_value=21.5+x1*np.sin(4*np.pi*x1)+x2*np.sin(20*np.pi*x2)
    return fitness_value

def main_run(generations):
    #problem defination
    problem=structure()
    problem.cost_func=cost_func
    problem.varmin=[-12,-6]
    problem.varmax=[12,6]
    problem.var=2

    #GA paramters
    param=structure()
    param.npop=1000
    param.niter=generations #generations

    #Run GA 
    #empty induvidual
    empty_induvidual=structure()
    empty_induvidual.cost=None
    empty_induvidual.value=None
    #best value
    best_value=structure()
    best_value.cost=0
    best_value.value=None

    pop_gen=empty_induvidual.repeat(param.npop)
    pop_gen1=empty_induvidual.repeat(param.npop)
    pop_gen2=empty_induvidual.repeat(param.npop)

    for i in range(param.npop):
        pop_gen[i].value=np.random.uniform(problem.varmin,problem.varmax,2)
        pop_gen[i].cost=cost_func(pop_gen[i].value[0],pop_gen[i].value[1])
        pop_gen1[i]=pop_gen[i].deepcopy()
        pop_gen2[i]=pop_gen[i].deepcopy()
        if pop_gen[i].cost>best_value.cost:
            best_value=pop_gen[i].deepcopy()
            
    print('first GA algorithm running----------')        
    best_sol1,avg_list1,best_value1=ga_first(pop_gen,best_value,problem,param)
    print('secound GA algorithm running----------')
    best_sol2,avg_list2,best_value2=ga_sec(pop_gen1,best_value,problem,param)
    print('third GA algorithm running----------')
    best_sol3,avg_list3,best_value3=ga_third(pop_gen2,best_value,problem,param)
    #best_value1=ga_sec(problem,params)
    return best_sol1,best_sol2,best_sol3,avg_list1,avg_list2,avg_list3,best_value1,best_value2,best_value3
#    # Results
#    plt.plot(best_sol1,'r--',avg_list1,'g--')
#    # plt.semilogy(out.bestcost)
#    plt.xlim(0,param.niter)
#    plt.xlabel('generations')
#    plt.ylabel('Best Cost')
#    plt.title('(GA) first version')
#    plt.grid(True)
#    plt.show()
#
#    plt.plot(best_sol2,'r--',avg_list2,'g--')
#    # plt.semilogy(out.bestcost)
#    plt.xlim(0,param.niter)
#    plt.xlabel('generations')
#    plt.ylabel('Best Cost')
#    plt.title('(GA) secound version')
#    plt.grid(True)
#    plt.show()
#
#    plt.plot(best_sol3,'r--',avg_list3,'g--')
#    # plt.semilogy(out.bestcost)
#    plt.xlim(0,param.niter)
#    plt.xlabel('generations')
#    plt.ylabel('Best Cost')
#    plt.title('(GA) third version')
#    plt.grid(True)
#    plt.show()
#    


