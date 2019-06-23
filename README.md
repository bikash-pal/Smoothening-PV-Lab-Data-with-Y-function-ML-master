# Smoothening-PV-Lab-Data-with-Y-function-ML
Smoothening of Pressure and Volume data obtained from Constant Composition Test using Linear Regression for Machine Learning in Python.   

## About Constant Composition Test
Constant-composition expansion experiments are performed on gas condensates or crude oil to simulate the pressure-volume relations of these hydrocarbon systems. 

### The test is conducted for the purposes of determining:
 * Saturation pressure (bubble-point or dew-point pressure)
 * Isothermal compressibility coefficients of the single-phase fluid in excess of saturation pressure
 * Compressibility factors of the gas phase
 * Total hydrocarbon volume as a function of pressure

#### Involved Equations

pSat = 1936 psi

Vrel = Vt / Vsat

Y = (pSat - p) / (p * (Vrel - 1))

Y = a + bP

*Source*: Tarek H. Ahmed, Reservoir Engineering Handbook, Chapter 3, pg. 130-142.

**Note**: Data is taken from the book.

![Alt text](/figure_1.png?raw=true "P vs V Graph")

![Alt text](/figure_2.png?raw=true "P vs Y Graph")
