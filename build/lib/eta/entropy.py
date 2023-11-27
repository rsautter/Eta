from .entropicForm import *
from .probability import *

def entropy(mat,equation=['Shannon','PowerlawTsallis'], prob=['Histogram','Permutation','Spectral'], **kwargs):
  outputs = {}
  nmat = (np.array(mat) - np.average(mat))/np.sum(mat)
  for eq in equation:
    for probType in prob:
      key = probType+'_'+eq

      if probType.lower()=='histogram':
        percent = kwargs['percent'] if 'percent' in kwargs.keys() else None
        p = getStatProb(nmat,percent)
      elif probType.lower()=='permutation':
        nx = kwargs['nx'] if 'nx' in kwargs.keys() else None
        ny = kwargs['ny'] if 'ny' in kwargs.keys() else None
        p = getPermutationProb(nmat,nx,ny)
      elif probType.lower()=='spectral':
        p = getSpectralProb(nmat)
      else:
        raise Exception("Probability: "+probType+" not implemented!")

      if eq.lower() == 'shannon':
        outputs[key] = shannon(p)
      elif eq.lower() == 'tsallis':
        q = kwargs['q'] if 'q' in kwargs.keys() else None
        eps = kwargs['eps'] if 'eps' in kwargs.keys() else None
        outputs[key] = tsallis(p,q,eps)
      elif eq.lower() == 'powerlawtsallis':
        qs = kwargs['qs'] if 'q' in kwargs.keys() else None
        eps = kwargs['eps'] if 'eps' in kwargs.keys() else None
        outputs[key] = plTsallis(p,qs,eps)
      else:
        raise Exception("Equation: "+eq+" not implemented!")

  return outputs

