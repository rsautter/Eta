import numpy as np
import ordpy

def getSpectralProb(mat):
  ft = np.fft.fftn(mat)
  #measures the PSD
  ft = np.real(ft*np.conj(ft))
  #normalizes it as a probability
  ft = ft/np.sum(ft)
  return np.ravel(ft)

def getStatProb(mat,percent=None):
  p =  0.1 if percent is None else percent
  m = np.ravel(mat)
  m,_ = np.histogram(m,bins=int(p*len(m)))
  m = m/np.sum(m)
  return m

def getPermutationProb(mat,nx=3,ny=3):
  dx = 3 if nx is None else nx
  dy = 3 if ny is None else ny
  _, p = ordpy.ordinal_distribution(mat,dx,dy)
  return p
