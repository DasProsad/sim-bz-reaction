# Simulation of the Belousov-Zhabotinsky reaction

The reaction can be modelled 

<div align="center">

$$
  \begin{aligned}
    A + B \rightarrow 2A \\
    arr[q, 0] = s[0] + s[0] * (alpha * s[1] - gamma * s[2]) \\
    arr[q, 1] = s[1] + s[1] * (beta * s[2] - alpha * s[0]) \\
    arr[q, 2] = s[2] + s[2] * (gamma * s[0] - beta * s[1])
  \end{aligned}
$$

</div>

# Centered Equations Example

Here is a set of centered equations:

<div align="center">

$$
\begin{aligned}
    A + B \rightarrow 2A \\
    arr[q, 0] = s[0] + s[0] * (alpha * s[1] - gamma * s[2]) \\
    arr[q, 1] = s[1] + s[1] * (beta * s[2] - alpha * s[0]) \\
    arr[q, 2] = s[2] + s[2] * (gamma * s[0] - beta * s[1])
\end{aligned}
$$

</div>

<p align="center"> <img src="bz_sim.gif" alt="A beautiful scenery" width="500"/> </p>
