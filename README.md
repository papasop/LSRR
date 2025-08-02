# LSRR: Local Structural Residual Regularity for ζ(s)

This repository contains code and documentation for validating the **Local Structural Residual Regularity (LSRR)** conjecture near nontrivial zeros of the Riemann zeta function.

## 📘 Overview

The LSRR framework analyzes the local behavior of the Riemann zeta function ζ(s) near a nontrivial zero \( \rho = \tfrac{1}{2} + i t \), modeling it as:
\[
\zeta(s) = \varphi_\rho(s) + \delta_\rho(s),
\]
where:
- \( \varphi_\rho(s) = \zeta'(\rho) (s - \rho) \) is the **compensator**,
- \( \delta_\rho(s) = \zeta(s) - \varphi_\rho(s) = O(\varepsilon^2) \) is the **residual**,
- \( s = \rho + \varepsilon \) with \( \varepsilon \in \mathbb{R} \) small.

This decomposition captures analytic regularity and symmetry properties of ζ(s), supporting the critical line hypothesis.

## 🧪 Numerical Validation

The code validates:
- Second-order behavior: \( \delta_\rho(s) = O(\varepsilon^2) \),
- Even symmetry: \( \delta_\rho(\rho + \varepsilon) = \delta_\rho(\rho - \varepsilon) \),
- Approximation: \( \delta(s)/\varepsilon^2 \to \tfrac{1}{2} \zeta''(\rho) \) as \( \varepsilon \to 0 \).

## 📂 Files

| File           | Description |
|----------------|-------------|
| `Lsrr.py`      | Main script for validating LSRR at the first nontrivial zero. |
| `ζ(s)1.py`     | Evaluation of ζ(s), ζ′(s), ζ″(s) for \( s = \rho_1 + \varepsilon \). |
| `ζ(s)2.py`     | Evaluation at the second zero \( \rho_2 \), for consistency check. |
| `README.md`    | This file. Overview and instructions. |


https://doi.org/10.5281/zenodo.16722682
Local Symmetry and Residual Decomposition of (s) Near Nontrivial Zeros




