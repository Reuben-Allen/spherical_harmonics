"""
Reuben Allen
11/23/2022

Spherical harmonics specify the angular dependence of atomic orbitals,
and their visualization can provide many important insights into
chemical behavior. Solving for the eigenstates of the angular momentum
operator gives complex functions; however, to give functions we are used
to seeing as chemists, it is necessary to convert these to real eigenstates
by linear combination of the complex ones.

This program will plot the spherical harmonic for a given angular momentum
quantum number and magnetic quantum number.
"""

# import python libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import scipy.special as special 

# define function for user input
def check_str():
    """This function fetches user inputs and checks them before proceeding."""
    while True:
        print('Enter the angular quantum number (must be a nonnegative integer):')
        l_str = input()
        try:
            l = int(l_str)
            if l < 0:
                print("L must be a nonnegative integer")
                continue
        except ValueError:
            print("Invalid Characters Entered. Please Try Again!")
            continue
        break
    while True:
        print('Enter the magnetic quantum number (must be an integer between -L and L):')
        m_str = input()
        try:
            m = int(m_str)
            if np.abs(m) > l:
                print("M must be an integer between -L and L")
                continue
        except ValueError:
            print("Invalid Characters Entered. Please Try Again!")
            continue
        break
    return l,m

# define function for complex spherical harmonics
def Y_complex(theta,phi,l,m):
    coefficient = np.sqrt((2*l+1)*np.math.factorial(l-m)/(4*np.pi*np.math.factorial(l+m)))
    return coefficient * np.exp(1j*m*phi) * special.lpmv(m,l,np.cos(theta)) # lpmv is the associated legendre polynomial

# define function for real spherical harmonics
def Y_real(theta,phi,l,m):
    if m == 0:
        result = Y_complex(theta,phi,l,m)
    elif m > 0:
        result = 2**-0.5 * (Y_complex(theta,phi,l,m) + (-1)**m * Y_complex(theta,phi,l,-1*m)) # take linear combination of solutions
    else:
        result = 1j * 2**-0.5 * ((-1)**m * Y_complex(theta,phi,l,m) - Y_complex(theta,phi,l,-1*m))
    return result.real

# define function for plotting the 3D contour of a chosen harmonic
def plot_harmonic(l,m):
    # set up a grid of spherical coordinates
    theta,phi = np.meshgrid(np.linspace(0,np.pi,200),np.linspace(0,2*np.pi,200))

    # find values of spherical harmonic
    harmonic_array = Y_real(theta,phi,l,m)
    R = np.abs(harmonic_array) # get absolute value

    # convert back to cartesian coordinates
    X = R * np.sin(theta) * np.cos(phi)
    Y = R * np.sin(theta) * np.sin(phi)
    Z = R * np.cos(theta)

    fig = plt.figure(figsize=(10,10)) # set the figure size to 10x10
    ax = fig.add_subplot(111, projection='3d', alpha=0.3) # set the canvas to 3D mode

    # Normalizing the values of our function to be between 0 and 1
    if l == 0 and m == 0:
        color_scheme = np.divide(harmonic_array,(4*np.pi)**-0.5)
    else:
        color_scheme = (harmonic_array - harmonic_array.min()) / (harmonic_array.max() - harmonic_array.min())

    # plot
    ax.plot_surface(X, Y, Z, facecolors=cm.coolwarm(color_scheme), shade=False, alpha=0.3)
    # We can also add the projection of the function 
    # zdir defines the projection plane
    # offset defines the location where the projection plane is set at
    ax.contour(X, Y, Z, zdir='z',offset = -1, cmap='winter')
    ax.contour(X, Y, Z, zdir='y',offset = 1, cmap='summer' )
    ax.contour(X, Y, Z, zdir='x',offset = -1, cmap='autumn')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    plt.show()
    return

if __name__ == "__main__":
    # get user input
    l,m = check_str()
    plot_harmonic(l,m)
    