from mpmath import mp, zeta, diff, mpc, nstr

mp.dps = 50

rho = mpc('0.5', '14.134725141734693790457251983562')

zeta_1 = diff(zeta, rho, n=1)
zeta_2 = diff(zeta, rho, n=2)
zeta_3 = diff(zeta, rho, n=3)
zeta_4 = diff(zeta, rho, n=4)
expected_limit = zeta_4 / 24

epsilons = [mp.mpf(10)**(-k) for k in range(1, 6)]

print(f"{'ε':<10} {'|δ/ε⁴|':<40} {'limit (ζ⁽⁴⁾/24)':<40} {'error'}")
print("-" * 110)

for eps in epsilons:
    s = rho + eps
    φ = zeta_1 * eps + zeta_2 * eps**2 / 2 + zeta_3 * eps**3 / 6
    δ = zeta(s) - φ
    δ_over_eps4 = δ / (eps**4)
    error = abs(δ_over_eps4 - expected_limit)
    print("{:<10} {:<40} {:<40} {}".format(
        str(eps), 
        nstr(δ_over_eps4, 30), 
        nstr(expected_limit, 30), 
        nstr(error, 5)
    ))
