import marimo

__generated_with = "0.3.8"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Dislocation displacement fields
        
        The dimensionless displacement fields for an edge dislocation are given by:

        $$
        \begin{align}
        u(x,y) &= \frac{\beta}{2\pi} \left( \tan^{-1}\left[\frac{x}{y}\right] + \frac{x y}{2\left(1 -\nu \right)\left(x^2 + y^2\right)} \right) \\
        v(x,y) &= \frac{\beta}{2\pi} \left(\frac{1 - 2\nu}{2(1-\nu)} \log{\left[\frac{\beta}{\sqrt{x^2+y^2}}\right]} + \frac{1}{2(1-\nu)}\frac{y^2}{x^2 + y^2} \right),
        \end{align}
        $$

        where $\beta$ is the normalized Burgers vector (in units of lattice constant) and $\nu$ is Poisson's ratio. 

        Play around with the parameters below to get a sense of how they affect the dilation and displacement fields!
        
        ---
        
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    ### UI controls
    ui_controls = mo.ui.array(
        [
            mo.ui.slider(0, 1, 0.05, value=0, label="Burgers vector magnitude"),
            mo.ui.slider(-1, 0.5, 0.05, value=1 / 3, label="Poisson's ratio"),
            mo.ui.checkbox(value=True, label="Color Atoms by Total Energy"),
        ]
    )

    beta = ui_controls[0]
    nu = ui_controls[1]
    show_lj = ui_controls[2]

    mo.vstack(ui_controls)
    return beta, nu, show_lj, ui_controls


@app.cell(hide_code=True)
def __(
    displaced_x,
    displaced_y,
    epsilon_xx,
    epsilon_yy,
    lennard_jones_energy,
    n_atoms,
    np,
    plt,
    xx,
    yy,
):
    ### plotting
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.contourf(
        xx,
        yy,
        epsilon_xx + epsilon_yy,
        levels=np.linspace(-0.00375, 0.00375, 32),
        extent=[-n_atoms - 1, n_atoms + 1, -n_atoms - 1, n_atoms + 1],
        cmap="PiYG",
        extend="both",
    )
    ax.scatter(
        displaced_x.ravel(),
        displaced_y.ravel(),
        c=lennard_jones_energy,
        s=25,
        cmap="turbo",
    )
    ax.axis("off")
    ax.set_xlim([-n_atoms - 1, n_atoms + 1])
    ax.set_ylim([-n_atoms - 1, n_atoms + 1])
    ax.set_title("Curves of constant dilation (green is expansion)")
    ax
    return ax, fig


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
    ## Boring zone 🥱
    ---

    """
    )
    return


@app.cell(hide_code=True)
def __(np):
    ### displacement fields
    def edge_dislocation_displacement_field(x, y, beta=1, nu=1 / 3):
        """Return normalized displacement fields"""
        r2 = x**2 + y**2
        r = np.sqrt(r2)

        prefactor = beta / (2 * np.pi)
        nu_factor = 2 * (1 - nu)
        u = prefactor * (np.arctan2(y, x) + x * y / (nu_factor * r2))
        v = prefactor * (
            (1 - 2 * nu) / nu_factor * np.log(beta / r) + y**2 / (nu_factor * r2)
        )
        return u, v


    def strain_field(x, y, beta=1, nu=1 / 3):
        """Return strain field components according to input displacement fields"""
        if beta > 0:
            u, v = edge_dislocation_displacement_field(x, y, beta=beta, nu=nu)
            epsilon_xx, du_dy = np.gradient(u)
            dv_dx, epsilon_yy = np.gradient(v)
            epsilon_xy = (du_dy + dv_dx) / 2
        else:
            epsilon_xx = epsilon_yy = epsilon_xy = np.zeros_like(x)
        return epsilon_xx, epsilon_yy, epsilon_xy


    def dislocate_atoms(x, y, beta=1, nu=1 / 3):
        """Displace atoms according to edge-dislocation displacement fields"""
        if beta > 0:
            u, v = edge_dislocation_displacement_field(x, y, beta=beta, nu=nu)
        else:
            u = v = 0
        return x + u, y + v
    return (
        dislocate_atoms,
        edge_dislocation_displacement_field,
        strain_field,
    )


@app.cell(hide_code=True)
def __(beta, dislocate_atoms, np, nu, show_lj, strain_field):
    ### function calls
    n_atoms = 8
    nx = 128j
    x, y = np.mgrid[-n_atoms - 0.5 : n_atoms + 1, -n_atoms - 0.5 : n_atoms + 1]
    xx, yy = np.mgrid[
        -n_atoms - 1 : n_atoms + 1 : nx, -n_atoms - 1 : n_atoms + 1 : nx
    ]
    displaced_x, displaced_y = dislocate_atoms(x, y, beta=beta.value, nu=nu.value)
    epsilon_xx, epsilon_yy, epsilon_xy = strain_field(
        xx, yy, beta=beta.value, nu=nu.value
    )

    if show_lj.value:
        complex_pos = displaced_x.ravel() + displaced_y.ravel() * 1j
        distance = np.abs(complex_pos[:, None] - complex_pos) + np.eye(
            complex_pos.shape[0]
        )
        lennard_jones_energy = (
            (np.sum((1 - distance**3) / distance**6, 0) + 4) / 3
        ) ** 0.5
    else:
        lennard_jones_energy = [0.75, 0.75, 0.75]
    return (
        complex_pos,
        displaced_x,
        displaced_y,
        distance,
        epsilon_xx,
        epsilon_xy,
        epsilon_yy,
        lennard_jones_energy,
        n_atoms,
        nx,
        x,
        xx,
        y,
        yy,
    )


@app.cell
def __():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


if __name__ == "__main__":
    app.run()
