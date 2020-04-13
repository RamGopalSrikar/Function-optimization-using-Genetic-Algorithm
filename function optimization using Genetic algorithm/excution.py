# -*- coding: utf-8 -*-

#import numpy as np
import statistics as st
from main import main_run
from ypstruct import structure
import matplotlib.pyplot as plt

def plottable(GA1,niter,k):
    
    #header
    output='iteration | GA{} maximum value     &    GA{} X value\n'.format(k,k)
    
    for i in range(niter):
        output=output+'-----------------------------------------------------------\n'
        output=output+'{}         |{}     &   {}\n'.format(i,GA1[i].bestvalue.cost,GA1[i].bestvalue.value)
    print(output)
        

GA=structure()
GA.bestsol=None
GA.avgsol=None
GA.bestvalue=structure()
niter=10
generation=100
GA1=GA.repeat(niter)
GA2=GA.repeat(niter)
GA3=GA.repeat(niter)

for i in range(niter):
    print('iteration {}'.format(i+1))
    GA1[i].bestsol,GA2[i].bestsol,GA3[i].bestsol,GA1[i].avgsol,GA2[i].avgsol,GA3[i].avgsol,GA1[i].bestvalue,GA2[i].bestvalue,GA3[i].bestvalue=main_run(generation)
    
plottable(GA1,niter,1)
plottable(GA2,niter,2)
plottable(GA3,niter,3)

mean1_max=[]
mean1_avg=[]
stddev1_max=[]
stddev1_avg=[]

mean2_max=[]
mean2_avg=[]
stddev2_max=[]
stddev2_avg=[]

mean3_max=[]
mean3_avg=[]
stddev3_max=[]
stddev3_avg=[]

for i in range(generation):
    m1_max=[]
    m1_avg=[]
    m2_max=[]
    m2_avg=[]
    m3_max=[]
    m3_avg=[]
    for j in range(niter):
        m1_max.append(GA1[j].bestsol[i])
        m1_avg.append(GA1[j].avgsol[i])
        
        m2_max.append(GA2[j].bestsol[i])
        m2_avg.append(GA2[j].avgsol[i])
        
        m3_max.append(GA3[j].bestsol[i])
        m3_avg.append(GA3[j].avgsol[i])
        
    mean1_max.append(st.mean(m1_max))
    stddev1_max.append(st.stdev(m1_max))
    mean1_avg.append(st.mean(m1_avg))
    stddev1_avg.append(st.stdev(m1_avg))
    
    mean2_max.append(st.mean(m2_max))
    stddev2_max.append(st.stdev(m2_max))
    mean2_avg.append(st.mean(m2_avg))
    stddev2_avg.append(st.stdev(m2_avg))
    
    mean3_max.append(st.mean(m3_max))
    stddev3_max.append(st.stdev(m3_max))
    mean3_avg.append(st.mean(m3_avg))
    stddev3_avg.append(st.stdev(m3_avg))


plt.plot(mean1_max,'r--',mean2_max,'g--',mean3_max,'y--')
plt.xlim(0,generation)
plt.xlabel('generations')
plt.ylabel('mean')
plt.title('(GA) 3 versions mean of maximum fitness')
plt.grid(True)
plt.legend()
plt.show()     

plt.plot(stddev1_max,'r--',stddev2_max,'g--',stddev3_max,'y--')
plt.xlim(0,generation)
plt.xlabel('generations')
plt.ylabel('standered deviation')
plt.title('(GA) 3 versions  standered deviation of maximum  fitness')
plt.grid(True)
plt.legend()
plt.show()  

plt.plot(mean1_avg,'r--',mean2_avg,'g--',mean3_avg,'y--')
plt.xlim(0,generation)
plt.xlabel('generations')
plt.ylabel('mean')
plt.title('(GA) 3 versions  mean of average fitness')
plt.grid(True)
plt.legend()
plt.show()     

plt.plot(stddev1_avg,'r--',stddev2_avg,'g--',stddev3_avg,'y--')
plt.xlim(0,generation)
plt.xlabel('generations')
plt.ylabel('standered deviation')
plt.title('(GA) 3 versions standered deviations of average fitness')
plt.grid(True)
plt.legend()
plt.show()  


    
    