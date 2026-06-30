#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:34:04 2023
python/dessins/animate/poisson.py
@author: erictixidor
"""
import numpy as np

def arc_cercle(x_c,y_c,r,angle_parc,angle_init):
    x1 = []
    y1 = []
    angle_fin = angle_init+angle_parc
    for angle in range(angle_init,angle_fin):
        angle_rad = angle/180*np.pi
        x1.append(x_c+r*np.cos(angle_rad))
        y1.append(y_c+r*np.sin(angle_rad))
    return x1[0],y1[0],x1[-1],y1[-1],x1,y1


def poisson(C0,angle,r):
    x = []
    y = []
    alpha0 = np.arccos(5/6)    
    angle_dep = int(angle-alpha0*180/np.pi-103)
    angle_parc = 80
    angle_fin = angle_dep + angle_parc
    C1_x = C0[0] - r*5/6*np.cos(angle_fin/180*np.pi-alpha0)
    C1_y = C0[1] - r*5/6*np.sin(angle_fin/180*np.pi-alpha0)
    qx1,qy1,qx_1,qy_1,x1,y1 = arc_cercle(C1_x,C1_y,r,angle_parc,angle_dep)
    
    C2_x = C0[0] + 1 * r*5/6*np.cos(angle_fin/180*np.pi-alpha0)
    C2_y = C0[1] + 1 * r*5/6*np.sin(angle_fin/180*np.pi-alpha0)
    if (qy_1-C2_y)<0 and (qx_1-C2_x) < 0:
        alpha1 = int(np.arctan((qy_1-C2_y)/(qx_1-C2_x))*180/np.pi+180)
    elif (qy_1-C2_y)>0 and (qx_1-C2_x) < 0:
        alpha1 = int(np.arctan((qy_1-C2_y)/(qx_1-C2_x))*180/np.pi+180)
    elif (qy_1-C2_y)<0 and (qx_1-C2_x) > 0:
        alpha1 = int(np.arctan((qy_1-C2_y)/(qx_1-C2_x))*180/np.pi)
    else: 
        alpha1 = int(np.arctan((qy_1-C2_y)/(qx_1-C2_x))*180/np.pi)
    _,_,qx2,qy2,x2,y2 = arc_cercle(C2_x,C2_y,r,angle_parc,alpha1)
    x = x1  + x2 + [qx1]
    y = y1 + y2 + [qy1] 
    return x,y
    