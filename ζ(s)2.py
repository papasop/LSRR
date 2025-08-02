import mpmath
import pandas as pd
mpmath.mp.dps = 50  # 高精度

# 第 2 和第 3 个零点（来自 Riemann 非平凡零点表）
t_list = [21.022039638771554, 25.010857580145688]  # t_2, t_3

# epsilon 测试范围
epsilons = [10**(-k) for k in range(1, 11)]

results = []

for idx, t in enumerate(t_list, start=2):
    for eps in epsilons:
        s = mpmath.mpf('0.5') + eps + mpmath.mpc(0, t)
        zeta_s = mpmath.zeta(s)
        phi_s = -1 / (4 * eps**2)
        delta = abs(zeta_s - phi_s)

        results.append({
            "zero_index": idx,
            "ε": eps,
            "Re(s)": mpmath.nstr(s.real, 20),
            "Im(s)": mpmath.nstr(s.imag, 20),
            "ζ(s)": zeta_s,
            "ϕ(s)": phi_s,
            "δ(s)": delta,
            "δ·ε²": delta * eps**2,
            "-log₁₀|δ(s)|": -mpmath.log10(delta)
        })

# 显示为表格
df = pd.DataFrame(results)
import matplotlib.pyplot as plt

# 可选：分别画出 log(δ) vs log(ε) 的斜率（理论应为 -2）
for zero_idx in df["zero_index"].unique():
    sub_df = df[df["zero_index"] == zero_idx]
    plt.plot([mpmath.log10(e) for e in sub_df["ε"]], sub_df["-log₁₀|δ(s)|"], label=f"Zero {zero_idx}")

plt.title("log(δ) vs log(ε) near ζ(s)=0")
plt.xlabel("log₁₀(ε)")
plt.ylabel("-log₁₀|δ(s)|")
plt.legend()
plt.grid(True)
plt.show()

# 输出数据
import IPython.display as disp
disp.display(df)
