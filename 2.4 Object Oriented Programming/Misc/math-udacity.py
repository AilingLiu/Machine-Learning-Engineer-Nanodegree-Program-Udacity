import math

def normp(x, mu, var):
    """Calculate the probability density function given x, mean, and variance

    Args:
        x: float or integer
        mu: float or integer, population mean
        var: float or integer, population variance

    Return:
        float, the probability of x

   """

    prob = (1/math.sqrt(2*math.pi*var))*math.exp(-math.pow(x-mu, 2)/(2*var))
    return prob

p155 = normp(155, 180, math.pow(34,2))
p120 = normp(120, 180, math.pow(34, 2))
print(p155-p120)
