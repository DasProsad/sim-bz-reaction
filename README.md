# Simulation of the Belousov-Zhabotinsky reaction

### Introduction
The Belousov-Zhabotinsky (BZ) reaction is a classic example of non-equilibrium thermodynamics, resulting in a type of chemical oscillator. The reaction demonstrates how certain chemical systems can exhibit temporal oscillations and spatial pattern formation, even far from equilibrium. It’s a fascinating phenomenon that combines elements of chemistry, physics, and complexity science.

### Overview of the Belousov-Zhabotinsky Reaction

The BZ reaction involves a mixture of several chemicals that react in a cyclic manner. The most common form of the BZ reaction involves:
- Malonic acid (as a substrate)
- Potassium bromate (as an oxidizer)
- Cerium, manganese, or ferroin (as a catalyst)
- Sulfuric acid (as the acidic medium)

The reaction proceeds through a series of intermediate steps, leading to periodic changes in the concentration of reactants and products. The visual result is often a beautiful display of color changes and patterns, such as concentric rings or spirals.

### Simplified Reaction Mechanism

The BZ reaction can be simplified into three main processes:
1. **Production of Bromine (Br₂):**

  $$
  \begin{align}
  \text{BrO}_3^- + 3 \text{HBr}_2 + 3 \text{H}^+ \rightarrow 3 \text{Br}_2 + 3 \text{H}_2\text{O}.
  \end{align}
  $$
  
2. **Oxidation of the Organic Substrate:**
 
  $$
  \begin{align}
  \text{Br}_2 + \text{CH}_2(\text{COOH})_2 \rightarrow 2 \text{BrCH}(\text{COOH})_2.
  \end{align}
  $$

4. **Regeneration of Bromide Ions:**

  $$
  \begin{align}
  \text{Ce}^{4+} + \text{CH}_2(\text{COOH})_2 + \text{H}_2\text{O} \rightarrow 2 \text{Ce}^{3+} + 2 \text{CO}_2 + 6 \text{H}^+.
  \end{align}
  $$

These reactions repeat in a cyclic manner, leading to the observed oscillations.

### Mathematical Model

The mathematical model often used to describe the BZ reaction involves partial differential equations (PDEs) that take into account both the reaction kinetics and the diffusion of chemicals. The Oregonator model is one such simplified model.

#### Oregonator Model Equations

$$
\begin{aligned}
    \frac{\partial u}{\partial t} &= D_u \nabla^2 u + f(u, v, w) \\
    \frac{\partial v}{\partial t} &= D_v \nabla^2 v + g(u, v, w) \\
    \frac{\partial w}{\partial t} &= D_w \nabla^2 w + h(u, v, w)
\end{aligned}
$$

where \( u, v, w \) are the dimensionless concentrations of the chemical species, \( D_u, D_v, D_w \) are their respective diffusion coefficients, and \( f, g, h \) are the nonlinear reaction terms.

### Simulation of the BZ reaction with a minimal model

The reaction can be simplified as:

$$
  \begin{aligned}
    A + B \xrightarrow{\alpha} 2A \\
    B + C \rightarrow 2B \\
    C + A \rightarrow 2C
  \end{aligned}
$$

Then, the dynamics can be written as a set of three difference equations:

$$
\begin{aligned}
A_{t+1} = A_{t} + A_{t}(\alpha B_{t} - \gamma C_{t}) \\
B_{t+1} = B_{t} + B_{t}(\beta C_{t} - \alpha A_{t}) \\
C_{t+1} = C_{t} + C_{t}(\gamma A_{t} - \beta B_{t})
\end{aligned}
$$

<p align="center"> <img src="bz_sim.gif" alt="A beautiful scenery" width="500"/> </p>
