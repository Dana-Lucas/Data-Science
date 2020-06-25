# PHY299

Work completed in my Scientific Modeling and Data Analysis course (PHY299 at the University of Mount Union)

The following are some of my favorite/most challenging homework assignments and a description of each:

Lucas HW4-3.py: Uses the Monte Carlo method to estimate the value of pi. 1000 pseudo-random coordinate 
pairs were determined within the region bounded by 0 and 1 on both the x and y axes. The proportion of 
points under the curve sqrt(1-x^2) estimates the value of pi.

Lucas HW4-4.py: A simulation game of tic-tac-toe

Lucas HW5-1.py: Determines the Earth Simularity Index (ESI) of astronomical bodies based on a text file 
containing properties of each. Finds the body with properties closet to those of Earth. 

Lucas HW9-1.py: Creates a Mandelbrot set fractal

Lucas HW10-1.py: Using the concept learned in Modern Physics, a Fourier Series was created with a varying number 
of terms. As the number of terms increases, it is seen that the graph becomes closer to the target square pulse wave.

Lucas HW10-2.py: Experimenting with the ways a noisy signal can be cleaned up by modifying Fourier coefficients. 
The bottom graphs show (from left to right) the original Fourier coefficients, only high coefficients, only low 
coefficients, and removing coefficients that are much smaller than the maximum coefficient. The graphs on the top 
show how well each 'filter' removes the excess noise from the data.

Lucas HW11-1.py: Works with solving ordinary differential equations using SciPy. The equations used describe the 
motion of Hyperion about Saturn. For example, Hyperion's distance, r, from Saturn as a function of its semi-major 
axis, a, eccentricity, e, and orbital angle, phi. domega/dphi was defined as a function of similar variables. The 
spin rate, omega, was plotted as a function of the orbital angle, phi, in two different scenarios using different initial conditions.

Lucas HW13-1.py: Estimating the number of lines a needle will cross if it is dropped on a piece of lined paper 
based on the distance from the needle's midpoint to the closest line on its left and the angle between the needle 
and the vertical axis. The first graph plots 10,000 random drops and the second graph plots 10,000 drops where 
there is a bias towards getting the needle to land on the vertical axis.

Lucas HW13-2.py: Performs some analysis based on data files containing the temperature on each day in every major 
US city since 1995. The code demonstrates the use of dictionaries, the glob module, and organized graphing techniques 
to come to conclusions on weather patterns based on Kolmorogorov-Smirnov tests and p-values.

Lucas HW14-1.py: Fitting data describing the temperature in Baltimore MD each day since 1995 to a sinusoidal curve. 
It is seen that each period lasts approximately 1 year, as expected from a graph that shows temperature vs. time.
