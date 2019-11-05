import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.special import factorial  # for array factorial calculation

from distributions.Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """

    def __init__(self, p=0.5, n=100):
        
        self.p = p
        self.n = n

        mean = self.calculate_mean()
        stdev = self.calculate_stdev()

        Distribution.__init__(self, mu=mean, sigma=stdev)

    def calculate_mean(self):
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        
        mean = self.p * self.n
        self.mean = mean

        return mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        stdev = math.sqrt(self.n * self.p * (1 - self.p))
        self.stdev = stdev
        
        return stdev

    def replace_stats_with_data(self, file_name):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        # read in the data - this updates the self.data attribute
        self.read_data_file(file_name)

        # p is n_successes/n_trials
        self.p = sum(self.data) / len(self.data)
        self.n = len(self.data)

        # update distribution parameters
        self.calculate_mean()
        self.calculate_stdev()

        return self.p, self.n

    def plot_bar(self, normed=False, **kwargs):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            Optional normed (boolean): plot as proportion instead of count
            Optional kwargs for matplotlib
            
        Returns:
            None
        """

        try:
            assert len(self.data) > 0, 'empirical data is not populated from file'
        except AssertionError:
            raise

        _, ax = plt.subplots()
        successes = self.data.count(1)
        failures = self.data.count(0)
        y_label = 'Count'

        if normed:
            successes = successes / len(self.data)
            failures = failures / len(self.data)
            y_label = 'Proportion'

        x = [0, 1]
        y = [failures, successes]

        ax.bar(x, y, **kwargs)
        ax.set_xlabel('Success or Failure')
        ax.set_ylabel(y_label)
        ax.set_xticks([0,1])
        ax.set_xticklabels([0,1])
        ax.set_title(f"Distribution of Successes vs Failures in {self.n} Trials")

    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function

        Returns:
            float: probability density function output
        """
        n_factorial = math.factorial(self.n)
        n_minus_k_factorial = math.factorial(self.n - k)
        k_factorial = math.factorial(k)

        p_of_k = n_factorial / (n_minus_k_factorial * k_factorial) * (self.p ** k) * (1 - self.p) ** (self.n - k)

        return p_of_k

    def pdf_ufunc(self, k_values):
        """Vectorized probability density function calculator for binomial distribution.

        Args:
            k_values (array): array-like sequence of k values to calculate pdf for 

        Returns:
            array: array-like sequence of pdf values for given k_values
        """

        # uses scipy.special.factorial for vectorized factorial, approximated by gamma fxn
        k_values = np.array(k_values)
        n_factorial = math.factorial(self.n)
        n_minus_k_factorial = factorial(self.n - k_values)
        k_factorial = factorial(k_values)

        p_of_kvalues = n_factorial / (n_minus_k_factorial * k_factorial) * np.power(self.p, k_values) * np.power((1 - self.p), (self.n - k_values))

        return p_of_kvalues

    def plot_pdf(self, start=None, end=None, range_color='r', **kwargs):
        """Function to plot the pdf of the binomial distribution
        
        Args:
            Optional start (int): The value to start calculating pdf at. Default 0.
            Optional end (int): The value to stop calculating pdf at. Default n.
            Optional range_color (string): Valid matplotlib color string for highlighting pdf range
            Optional matplotlib plotting kwargs.
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            float: probability between start and stop
            
        """

        x_values = list(range(0, self.n + 1))
        y_values = self.pdf_ufunc(x_values)
        probability = y_values.sum()
        
        _, ax = plt.subplots()
        barlist = ax.bar(x_values, y_values, **kwargs)
        
        # if endpoint or startpoint is given, highlight the range and calculate the probability within the range
        if start or end:
            start = 0 if not start else start
            end = self.n if not end else end
            for bar in barlist[start:end + 1]:
                bar.set_color(range_color)
            probability = y_values[start:end + 1].sum()

        ax.set_xlabel('Num Successes')
        ax.set_ylabel('Probability')

        ax.set_title('Probability Density of k Successes in Binomial Distribution')

        return x_values, list(y_values), probability
                
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        return Binomial(self.p, self.n + other.n)
                        
    # use the __repr__ magic method to output the characteristics of the binomial distribution object.
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        mean = self.calculate_mean()
        stdev = self.calculate_stdev()
        n = self.n
        p = self.p

        return f"mean {mean}, stdev {stdev}, p {p}, n {n}"
