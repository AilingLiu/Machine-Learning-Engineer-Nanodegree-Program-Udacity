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

def calculate_stdev(self, sample=True):

"""Method to calculate the standard deviation of the data set.

Args:
sample (bool): whether the data represents a sample or population

Returns:
float: standard deviation of the data set

"""

# TODO:
#   Calculate the standard deviation of the data set
#
#   The sample variable determines if the data set contains a sample or a population
#   If sample = True, this means the data is a sample.
#   Keep the value of sample in mind for calculating the standard deviation
#
#   Make sure to update self.stdev and return the standard deviation as well

    list_diff = lambda arr, val: [math.pow(i-val, 2) for i in arr]
    mu = self.mean
    if sample:
    n = len(self.data)-1
    else:
    n = len(self.data)

    std = math.sqrt(sum(list_diff(self.data, mu))/n)
    return std
