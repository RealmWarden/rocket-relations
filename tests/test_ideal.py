import numpy as np

def charVel(gamma, R, T0):
    try:
        gamma = float(gamma)
        R = float(R)
        T0 = float(T0)
    except TypeError:
        raise TypeError("All inputs must be numbers.")
    
    if gamma <= 1:
        raise ValueError("Specific heat ratio must be greater than 1.")
    if T0 <= 0:
        raise ValueError("Stagnation temperature must be greater than 0 K.")
    if R <= 0:
        raise ValueError("Specific gas constant must be greater than 0 J/kg-K.")

    cStar = np.sqrt((1/gamma) * (((gamma+1)/2)**((gamma+1)/(gamma-1))) * R * T0)
    return cStar

def thrustCoeff(pep0, pap0, AeAstar, gamma):
    try:
        pep0 = float(pep0)
        pap0 = float(pap0)
        AeAstar = float(AeAstar)
        gamma = float(gamma)
    except TypeError:
        raise TypeError("All inputs must be numbers.")
    
    if pep0 < 0 or pep0 >= 1 or pap0 < 0 or pap0 >= 1:
        raise ValueError("Pressure ratios must be in the range [0, 1).")
    if AeAstar < 0:
        raise ValueError("Ratio of exit area to throat area must be greater than or equal to 1.")
    if gamma <= 1:
        raise ValueError("Specific heat ratio must be greater than 1.")

    Cf = np.sqrt(((2*(gamma**2))/(gamma-1)) * ((2/(gamma+1))**((gamma+1)/(gamma-1))) * (1-(pep0)**((gamma-1)/gamma))) + ((pep0-pap0)*AeAstar)
    return Cf

def test_answer():
    T0 = 3500
    gamma = 1.2
    R = 350
    pep0 = 0.0125
    pap0 = 0.02
    AeAstar = 10
    assert round(charVel(gamma, R, T0),4) == 1706.6214
    assert round(thrustCoeff(pep0, pap0, AeAstar, gamma),7) == 1.5423079