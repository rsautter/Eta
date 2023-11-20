# Eta (&eta;)

&eta; is a package for computing entropy in matrices. It encompasses the following attributes:
  
  1. Probability Measurement (Histogram, Spactral and Permutation)
  2. Entropic Form (Shannon, Tsallis and Power-Law Tsallis)

# Requirements
  - Numpy
  - Ordpy

# Install

    pip install ordpy
    pip install git+https://github.com/rsautter/eta/

# Simple  Example

The following script provides the all entropy measurements of a random matrix:

    import numpy
    import eta
    mat = np.random.rand(256*256).reshape(256,256)
    eta.entropy(mat)


# Reference

[1] Pessa, A. A., & Ribeiro, H. V. (2021). ordpy: A Python package for data analysis with permutation entropy and ordinal network methods. Chaos: An Interdisciplinary Journal of Nonlinear Science, 31(6).
