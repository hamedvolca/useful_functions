# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:28:51 2023

@author: hk21local
"""

import numpy as np

def create_circle_from_three_points(a, plot_flag):
    """
    create_circle_from_three_points(a, False)
    a = np.random.rand(2, 3) # three points in the form of 2x3 matrix
    plot_flag: False -> no plot, True -> plot the circle
    
    The code does check the collinearity.
    If three points are not distinct, collinearity is detected.
    The code does NOT check the size and type of the inputs.
    """
    
    def pointsAreCollinear(xy):
        return np.linalg.matrix_rank(xy[1:,:] - xy[0,:]) == 1
    
    if pointsAreCollinear(a.T):
        print('Collinear points')
        center = False
        radius = False
    else:
        temp, order = np.sort(a[1,:]), np.argsort(a[1,:])
        a_sorted_1 = a[:,order]
        
        p1 = a_sorted_1[:,2]

        a_sorted = a_sorted_1
        a_sorted = np.delete(a_sorted, 2, axis=1)
        temp, order = np.sort(a_sorted[0,:]), np.argsort(a_sorted[0,:])
        a_sorted = a_sorted[:,order]

        p2 = a_sorted[:,1]
        p3 = a_sorted[:,0]
        
        v1 = (p2-p1)/2
        v2 = (p3-p2)/2
        v1_p = np.array([v1[1],-v1[0]])
  
        x1 = v1[0]
        y1 = v1[1]
        x2 = v2[0]
        y2 = v2[1]
        
        m1 = x1 * x2 + x2 * x2 + y1 * y2 + y2 * y2
        m2 = y1 * x2 - x1 * y2
        mu = m1/m2
        c = p1 + v1 + mu * v1_p

        center = c
        radius = np.linalg.norm(c-p1)
        
        if plot_flag:
            import matplotlib.pyplot as plt
            
            def circle(x,y,r):
                th = np.arange(0, 2*np.pi+np.pi/50, np.pi/50)
                xunit = r * np.cos(th) + x
                yunit = r * np.sin(th) + y
                h = plt.plot(xunit, yunit)
                return h
            
            plt.figure()
            plt.scatter(p1[0],p1[1],c='red')
            plt.scatter(p2[0],p2[1],c='b')
            plt.scatter(p3[0],p3[1],c='k')
            plt.scatter(c[0],c[1],c='black',marker='+')
           
            plt.plot([p1[0]+v1[0],center[0]],[p1[1]+v1[1], center[1]],'k-.')
            plt.plot([p2[0]+v2[0],center[0]],[p2[1]+v2[1], center[1]],'k-.')
            circle(c[0],c[1],np.linalg.norm(c-p1))
            plt.plot([p1[0],p2[0]],[p1[1],p2[1]],'b')
            plt.plot([p2[0],p3[0]],[p2[1],p3[1]],'b')
            plt.axis('equal')
            
    return center, radius

if __name__=='__main__':
    a1 = np.random.rand(2, 3) 
    a2 = np.array([[1,-1,0],[1,1,-1]])
    a3 = np.array([[1,1,-1],[1,-1,0]])
    a4 = np.array([[1,1,0],[1,1,-1]])
    c1, r1 = create_circle_from_three_points(a1, True)
    c2, r2 = create_circle_from_three_points(a2, True)
    c3, r3 = create_circle_from_three_points(a3, True)
    c4, r4 = create_circle_from_three_points(a4, True)