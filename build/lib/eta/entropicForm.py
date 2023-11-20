import numpy as np

def shannon(p):
  p2 = p[p>1e-13]
  return -np.sum(p2*np.log(p2))/np.log(len(p))

def tsallis(p,q=None,eps = None):
  qi = 1 if q is None else q
  epsi = 1e-4 if eps is None else eps

  if np.abs(qi-1)>epsi:
    return (1 - np.sum(np.power(p,qi)))/(qi-1)
  else:
    return (1 - np.sum(np.power(p,qi+epsi)))/(qi+epsi-1)

def plTsallis(p,qs=None,eps=None,returnQH=False):
  ts = []
  qsi = np.linspace(1,5,100) if qs is None else qs
  epsi = 1e-4 if eps is None else eps
  for q in qsi:
    ts.append(tsallis(p,q,eps))
  alpha, _ = np.polyfit(np.log(qsi),np.log(ts),deg=1)
  if not(returnQH):
    return -alpha
  else:
    return -alpha, qsi,np. array(ts)

