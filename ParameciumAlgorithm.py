# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 23:19:22 2017

@author: lufuyan

Paramecium Optimization Algorithm for one dimensinal function


"""

"""     
        #Folding
        
        # right folding
        elif fmi<fst and fmi<=fed and fed<(fst+fmi)/2.0:
            lg=lg/2.0
            mi=ed-lg/2.0
            st=ed-lg
            
            
        # left folding    
        elif fmi<=fst and fmi<fed and fst<(fed+fmi)/2.0:
            lg=lg/2.0
            mi=st+lg/2.0
            ed=st+lg
            
"""  

import math

def parameciumOpt(function,start,end,precision):
    
    
    st=start
    ed=end
    mi=(start+end)/2.0
    lg=ed-st
    
    # Initial function values for three points of paramecium
    fst=function(st)
    fmi=function(mi)
    fed=function(ed)
    
    
    while ed-st>precision:
        
              
        # swimming
        # right swimming
        if fst>=fmi and fmi>fed:
            # if crush on the boundary, then shrink to its 3/4 length
            if ed==end:
                lg=lg*3/4.0
                mi=ed-lg/2.0
                st=ed-lg
            
            # else if space is not enought for crawling, then put the head on the boundary
            elif (ed+lg/2.0)>end:
                ed=end
                mi=ed-lg/2.0
                st=ed-lg
           
            # else do the normal crawling
            else:
                ed=ed+lg/2.0
                mi=ed-lg/2.0
                st=ed-lg
            
             
        # left swimming
        elif fst<fmi and fmi<=fed:
            # if crush on the boundary, then shrink to its 3/4 length
            if st==start:
                lg=lg*3/4.0
                mi=st+lg/2.0
                ed=st+lg
                
            # else if space is not enought for crawling, then put the head on the boundary    
            elif st-lg/2.0<start:
                st=start
                mi=st+lg/2.0
                ed=st+lg
            
            # else do the normal crawling
            else:
                st=st-lg/2.0
                mi=st+lg/2.0
                ed=st+lg
        
         
        #Shrinking
        elif fmi<=fst and fmi<=fed:
            lg=lg/2.0
            st=mi-lg/2.0
            ed=mi+lg/2.0
        
        #dividing 
        else:
            # size of each paramecium after dividing equals origianl size
            # all local minimum of the parameciums can be stored and return 
            paramecium1=parameciumOpt(function,max(st-lg/2.0,start),mi,precision)
            paramecium2=parameciumOpt(function,mi,min(ed+lg/2.0,end),precision)
            return paramecium1 if paramecium1[0]<paramecium2[0] else paramecium2
        # updating the fuction value for three point of paramecium
        fst=function(st)
        fmi=function(mi)
        fed=function(ed)
    
        
    result={fst:st,fmi:mi,fed:ed}
    finalvalue=min([fst,fmi,fed])
    return (finalvalue,result[finalvalue])


# test functions:
def f(x):
    return math.sin(x)

def fproblem0(x):
    return math.sin(x)+math.sin(10*x/3.0)
start0=2.7
end0=7.5
bestf0=-1.899599
bestx0=5.145735

def fproblem1(x):
    result=[k*math.sin((k+1)*x+k) for k in range(1,7)]
    
    return -sum(result)
start1=-10
end1=10
bestf1=-12.03124
bestx1=-6.7745761


def fproblem2(x):
    return -(16*x**2-24*x+5)*math.exp(-x)
start2=1.9
end2=3.9
bestf2=-3.85045
bestx2=2.868034

def fproblem3(x):
    return -(1.4-3*x)*math.sin(18*x)
start3=0.0
end3=1.2
bestf3=-1.48907
bestx3=0.96609

def fproblem4(x):
    return -(x+math.sin(x))*math.exp(-x**2)
start4=-10
end4=10
bestf4=-0.824239
bestx4=0.67956
    

def fproblem5(x):
    return math.sin(x)+math.sin(10*x/3.0)+math.log(x)-0.84*x+3

start5=2.7
end5=7.5
bestf5=-1.6013
bestx5=5.19978
    


def fproblem6(x):
    result=[k*math.cos((k+1)*x+k) for k in range(1,7)]
    
    return -sum(result)
    
start6=-10
end6=10
bestf6=-14.508
bestx6=-7.083506

def fproblem7(x):
    return math.sin(x)+math.sin(2*x/3.0)

start7=3.1
end7=20.4
bestf7=-1.90596
bestx7=17.039

def fproblem8(x):
    return -x*math.sin(x)
start8=0.0
end8=10.0
bestf8=-7.916727
bestx8=7.9787

def fproblem9(x):
    return 2*math.cos(x)+math.cos(2*x)
start9=-math.pi/2.0
end9=2*math.pi
bestf9=-1.5
bestx9=2.09439

def fproblem10(x):
    return math.sin(x)**3+math.cos(x)**3
start10=0.0
end10=2*math.pi
bestf10=-1
bestx10=math.pi

def fproblem11(x):
    return -x**(2/3.0)-(1-x**2)**(1/3.0)
start11=0.001
end11=0.99
bestf11=-1.5874
bestx11=1/math.sqrt(2)

def fproblem12(x):
    return -math.exp(-x)*math.sin(2*math.pi*x)
start12=0.0
end12=4.0
bestf12=-0.788685
bestx12=0.224885

def fproblem13(x):
    return (x**2-5*x+6)/(x**2+1)
start13=-5
end13=5
bestf13=-0.03553
bestx13=2.41422

def fproblem14(x):
    return (x-2)**2 if x<=3 else 2*math.log(x-2)+1
start14=0.0
end14=6.0
bestf14=0.0
bestx14=2.0

def fproblem15(x):
    return -(x-math.sin(x))*math.exp(-x**2)
start15=-10.0
end15=10.0
bestf15=-0.0634905
bestx15=1.195137

def fproblem16(x):
    return x*math.sin(x)+x*math.cos(2*x)
start16=0.0
end16=10.0
bestf16=-9.50835
bestx16=4.79507

def fproblem17(x):
    return math.exp(-3*x)-math.sin(x)**3
start17=0.0
end17=20.0
bestf17=math.exp(-27*math.pi/2.0)-1
bestx17=9*math.pi/2.0



  
def gss(f, a, b, c, tau = 0.0000001):
    '''
    Python recursive version of Golden Section Search algorithm.

    This code appears to be broken - see the talk page.

    tau is the tolerance for the minimal value of function f
    b is any number between the interval a and c
    '''
    goldenRatio = (1 + math.sqrt(5)) / 2
    if b < c:
        x = b + (2 - goldenRatio) * (c - b)
    else:
        x = b - (2 - goldenRatio) * (b - a)
    if abs(c - a) < tau: 
        return (f((c + a) / 2),(c + a) / 2)
    if f(x) < f(b):
        return gss(f, b, x, c, tau) if b < c else gss(f, a, x, b, tau)
    else:
        return gss(f, a, b, x, tau) if b < c else gss(f, x, b, c, tau)    


for i in range(18):
    ST=eval("start"+str(i))
    ED=eval("end"+str(i))
    a=parameciumOpt(eval("fproblem"+str(i)),ST,ED,0.0000001)
    print(a)
    print((eval("bestf"+str(i)),eval("bestx"+str(i))))
    b=gss(eval("fproblem"+str(i)),ST,ED+(ED-ST)*(1-math.sqrt(5))/2.0 ,ED,0.0000001)
    print(b)
    print("\n")
    








