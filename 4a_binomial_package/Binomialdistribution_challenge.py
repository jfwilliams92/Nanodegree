# TODO: import necessary libraries
import numpy as np
import math
import matplotlib.pyplot as plt
from distributions.Generaldistribution import Distribution


# TODO: make a Binomial class that inherits from the Distribution class. Use the specifications below.
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
        fig, ax = plt.subplots()
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

    # write a method to plot the probability density function of the binomial distribution
    def plot_pdf(self):
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        pass

        # TODO: Use a bar chart to plot the probability density function from
        # k = 0 to k = n
        
        #   Hint: You'll need to use the pdf() method defined above to calculate the
        #   density function for every value of k.
        
        #   Be sure to label the bar chart with a title, x label and y label

        #   This method should also return the x and y values used to make the chart
        #   The x and y values should be stored in separate lists
                
    # write a method to output the sum of two binomial distributions. Assume both distributions have the same p value.
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
        
        # TODO: Define addition for two binomial distributions. Assume that the
        # p values of the two distributions are the same. The formula for 
        # summing two binomial distributions with different p values is more complicated,
        # so you are only expected to implement the case for two distributions with equal p.
        
        # the try, except statement above will raise an exception if the p values are not equal
        
        # Hint: When adding two binomial distributions, the p value remains the same
        #   The new n value is the sum of the n values of the two distributions.
        pass
                        
    # use the __repr__ magic method to output the characteristics of the binomial distribution object.
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        
        # TODO: Define the representation method so that the output looks like
        #       mean 5, standard deviation 4.5, p .8, n 20
        #
        #       with the values replaced by whatever the actual distributions values are
        #       The method should return a string in the expected format
    
        pass
