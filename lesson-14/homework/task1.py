import numpy as np
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
vectorized_f_to_c = np.vectorize(fahrenheit_to_celsius)
fahrenheit_val = np.array([32, 68, 100, 212, 77])
celsius_val = vectorized_f_to_c(fahrenheit_val)
print("Fahrenheit:", fahrenheit_val)
print("Celsius:", celsius_val)
