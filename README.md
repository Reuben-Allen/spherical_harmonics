# Visualize Real Spherical Harmonics
Solving for the eigenstates of angular momentum in quantum mechanics gives functions
known as spherical harmonics, which, in spherical coordinates, can be represented by
the product of a complex exponential function of the azimuthaal angle $\phi$ and the associated legendre
polynomial of the cosine of the polar angle $\theta$. The spherical harmonics are incredibly useful
because they specify the angular depedence of the atomic orbital wavefunctions.  
Since the spherical harmonics are complex functions, to obtain shapes we are familiar with
it is necessary to plot real functions which are linear combinations of the complex eigenstates.
To get started, simply specify the angular momentum quantum number, L, which is defined for integers
greater than or equal to zero, and the magentic quantum number, which is defined for integers from
negative L to positive L. The spherical harmonic corresponding to these quantum numbers will
then be plotted in 3D.
## Example:
```
Enter the angular quantum number (must be a nonnegative integer):
2
Enter the magnetic quantum number (must be an integer between -L and L):
0
```
