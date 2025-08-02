# Install mpmath if not already installed (in Colab, it's usually available via sympy, but let's ensure)
!pip install mpmath

from mpmath import mp, mpc, zeta, diff

# Set high precision
mp.dps = 50

# Define the first nontrivial zero rho1 = 0.5 + i * t1
t1 = mp.mpf('14.1347251417346937904572519835624702707842571156992431751869149029')
rho1 = mpc(0.5, t1)

# Function to compute zeta derivatives at rho
def zeta_derivative(point, order):
    return diff(zeta, point, n=order)

# Compute zeta'(rho1) and zeta''(rho1)
zeta_prime_rho1 = zeta_derivative(rho1, 1)
zeta_double_prime_rho1 = zeta_derivative(rho1, 2)
half_zeta_double_prime = zeta_double_prime_rho1 / 2

print("zeta'(rho1):", zeta_prime_rho1)
print("zeta''(rho1):", zeta_double_prime_rho1)
print("1/2 zeta''(rho1):", half_zeta_double_prime)

# Test for multiple epsilon values
epsilons = [mp.mpf('0.1'), mp.mpf('0.01'), mp.mpf('0.001'), mp.mpf('0.0001'), mp.mpf('0.00001')]

for eps in epsilons:
    s = rho1 + eps
    zeta_s = zeta(s)
    phi = zeta_prime_rho1 * eps
    delta = zeta_s - phi
    delta_over_eps2 = delta / (eps ** 2)
    
    print(f"\nFor epsilon = {eps}:")
    print("zeta(s):", zeta_s)
    print("phi(s):", phi)
    print("delta(s):", delta)
    print("delta / eps^2:", delta_over_eps2)
    print("Difference from 1/2 zeta''(rho1):", delta_over_eps2 - half_zeta_double_prime)