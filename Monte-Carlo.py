import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import time

def function(a):
    """Returns f(a)"""
    return a**2

def max_point(fun, a, b):
    """Calculate the maximun point of the function fun between a, b values"""
    # Step 1 - Calculate the maximun of the function
    M = fun(a)
    for i in range(1000): # not enough
        rnd = np.random.uniform(a, b)
        if rnd > M: 
            M = rnd 
    return M

def integra_mc_vector(fun, a, b, num_puntos=10000):
    """Calculate the integral of the function fun with Monte Carlo method
     with vectors and returns the result in seconds"""
    tic = time.process_time()

    # Step 1 - Calculate the maximun of the function
    M = max_point(fun, a, b)

    # Step 2 - Generate random points
    # x axis of the point   
    x = np.random.uniform(a, b, num_puntos)
    # y axis of the point
    y = np.random.uniform(0.0, M, num_puntos)
    
    #x = (np.random.rand(num_puntos) * (b-a)) + a 
    #y = np.random.rand(num_puntos)  * M
    
    x = fun(x)
    below = np.sum(y < x)   # Number of points below the curve

    # Step 3 - Calculate the area below the curve
    # Print the results
    area = (below / num_puntos) * (b - a) * M
    
    #print("----VECTOR-WAY----")
    #print("N totales = {}".format(num_puntos))
    #print("N debajo = {}".format(below))
    #print("M = {}".format(M))
    #print("Area total = {}".format(area))
    
    #value = integrate.quad(fun, a, b)
    #print("Area real: {}".format(value[0]))

    toc = time.process_time()
    return 1000 * (toc - tic)

def integra_mc_loop(fun, a, b, num_puntos=10000):
    """Calculate the integral of the function fun with Monte Carlo method
     with a loop with num_puntos iterations and return the result in seconds"""
    tic = time.process_time()
    # Step 1 - Calculate the maximun of the function
    M = max_point(fun, a, b)

    # Step 2 - Generate random points
    below = 0   # Number of points below the curve
    for j in range(num_puntos):
        # x axis of the point   
        x = np.random.uniform(a, b)
        # y axis of the point
        y = np.random.uniform(0.0, M)

        if y <= fun(x):
            below += 1
        
    # Step 3 - Calculate the area below the curve
    # Print the results
    area = (below / num_puntos) * (b - a) * M
    
    #print("----LOOP-WAY----")
    #print("N totales = {}".format(num_puntos))
    #print("N debajo = {}".format(below))
    #print("M = {}".format(M))
    #print("Area total = {}".format(area))
    
    #value = integrate.quad(fun, a, b)
    #print("Area real: {}".format(value[0]))
        
    toc = time.process_time()
    return 1000 * (toc - tic)

def compara_tiempos(num_puntos, N, a, b):
    """Draw the graph od the times compared to each other.
    N is the number of comparasions done and num_puntos is the number
    of the points used to calculate the integral"""
    sizes = np.linspace(100, 100000, N)
    vector_time = []
    loop_time = []
    increment = 10000

    for size in sizes:
        vector_time += [integra_mc_vector(function, a, b, num_puntos)]
        loop_time += [integra_mc_loop(function, a, b, num_puntos)]
        
        num_puntos += increment

    # Graph drawing
    plt.figure()

    plt.scatter(sizes, vector_time, c='red', label="VECTOR TIME")
    plt.scatter(sizes, loop_time, c='blue', label="LOOP TIME")

    plt.legend()
    plt.show()

# main
a, b = 0.0, 3.0
num_experiments = 1000
num_puntos = 100

compara_tiempos(num_puntos, num_experiments, a, b)