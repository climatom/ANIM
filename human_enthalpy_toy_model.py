#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 16:36:30 2022

@author: k2147389
"""
import utils
import numba as nb
import numpy as np
import matplotlib.pyplot as plt

latent_vap=2430.0 # latent heat of vaporization (2430 kJ/g)
LR=16.5 # K/kPa
Ad=1.84 # Surface area (m^2)
Rcl=0.155*0.27
fcl=1+0.3*0.27
srs_minAct=np.array([117.1,179.7,147.5,103.9,140.9,171.8]) # g/h
srs_all=np.array([97.61,183.14,159.87,111.98,142.98,171.82]) # g/m^2
lat_loss_all=srs_all/(60**2)*latent_vap
obs_met=np.array([77.9,82.6,80.4,81.5,87.7,87.4]) # W/m^2, minAct
dry_gain_all=np.array([-1.51,8.34,18.60,41.46,61.38,76.95]) # Dry heat gain (W/m^2)
ts_all=np.array([36,38,40,44.04,47.48,50.57])
rhs_all=np.array([66.25,60.83,50.24,28.81,20.14,12.70])
# ql=-sr/(60**2)*latent_vap
# met=80 # W/m^-2
# hc=5.5
skin_ts=np.array([38.56,37.92,37.57,37.06,36.55,36.25,36.25])


@nb.jit('float64(float64,float64)')
def VP_TETENS(ta,rh):
    # Notes:
    # ta is in degC
    # rh is in percent
    # pa is returned in kPa
    ta+=273.15
    rh/=100.
    t0=273.16
    a1_w=611.21; a3_w=17.502; a4_w=32.19
    a1_i=611.21; a3_i=22.587; a4_i=-0.7
    
    # Sat Vp according to Teten's formula
    if ta>273.15:
        pa=a1_w*np.exp(a3_w*(ta-t0)/(ta-a4_w))
    else:
        pa=a1_i*np.exp(a3_i*(ta-t0)/(ta-a4_i))    
    pa=pa*rh*0.001
    return pa

nt=len(ts_all)
tw=utils._TW(nt,ts_all.flatten()+273.15,
              rhs_all.flatten(),np.ones(nt)*101300.)-273.15
me=utils._ME1D(nt,ts_all+273.15,rhs_all,p=np.ones(nt)*101300.)



# @nb.jit('float64(float64,float64)')
# def DRY_GAIN():
    
    
    
    
    
# ts=np.arange(35,40,0.1)
# rhs=np.arange(1,100,1)
# grid_t,grid_rh=np.meshgrid(ts,rhs)
# out=np.zeros(grid_t.shape)

# col=0; 
# for tsk in ts:
#     psk=VP_TETENS(tsk,0.1)
#     qh=met+ql
#     dt=-qh/hc
#     ta=tsk+dt
#     row=0
#     for rh in rhs:
#         pa=VP_TETENS(ta,rh)
#         ql_i=hc*LR*(psk-pa)
#         w=min(1,ql/ql_i)
#         me=ta*1.013 + latent_vap*0.622/1000.*pa
#         out[row,col]=me
#         row+=1
#     col+=1
    
# fig,ax=plt.subplots(1,1)
# ax.contourf(grid_t,grid_rh,out,levels=25)
    
    

    
    
    
    
        