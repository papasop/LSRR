import numpy as np
import pandas as pd
from mpmath import zeta, mp, mpc
from math import log10

# 设置高精度计算
mp.dps = 50

# 第一个非平凡零点的虚部
t1 = 14.134725

# 设置测试点：Re(s) 从 0.6 收敛到 0.5（临界线）
epsilons = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10]

results = []

for eps in epsilons:
    s = mpc(0.5 + eps, t1)
    zeta_s = zeta(s)

    # 构造对称补偿项 φ(s)（测试结构假设：φ = -1/(4*eps^2)）
    phi_s = -1 / (4 * eps**2)

    # 计算残差 δ(s) = |ζ(s) - φ(s)|
    delta = abs(zeta_s - phi_s)

    results.append([
        eps,
        s.real,
        s.imag,
        zeta_s,
        phi_s,
        delta,
        -log10(float(delta))
    ])

# 输出 DataFrame
df = pd.DataFrame(results, columns=["ε", "Re(s)", "Im(s)", "ζ(s)", "ϕ(s)", "δ(s)", "-log₁₀|δ(s)|"])
pd.set_option('display.float_format', lambda x: f"{x:.12g}")
display(df)
