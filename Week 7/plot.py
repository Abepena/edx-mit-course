import pylab as plt

my_samples = []
my_linear = []
my_quadratic = []
my_cubic = []
my_exponential = []

for i in range(30):
    my_samples.append(i)
    my_linear.append(i)
    my_quadratic.append(i**2)
    my_cubic.append(i**3)
    my_exponential.append(1.5**i) # 2^i grows so rapidly, it is hard to visualize

plt.plot(my_samples, my_linear)
plt.plot(my_samples, my_qua)