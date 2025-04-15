# Accurate and Affordable Simulation of Molecular Infrared Spectra with AIQM Models

The computational details are described at:

- Yi-Fan Hou, Cheng Wang, [Pavlo O. Dral](http://dr-dral.com). [Accurate and Affordable Simulation of Molecular Infrared Spectra with AIQM Models](https://doi.org/10.1021/acs.jpca.5c00146). *J. Phys. Chem. A* **2025**, *ASAP*. DOI: 10.1021/acs.jpca.5c00146. Preprint on *ChemRxiv*: https://doi.org/10.26434/chemrxiv-2024-r5prt (2024-11-08).

## Tutorial

See the [tutorial](https://xacs.xmu.edu.cn/docs/mlatom/tutorial_ir.html) on how to perform IR simulations.

## Data

- Calculated IR spectra are in the zip files prefixed with "static".
- Experiment data can be downloaded from the [NIST Chemistry Webbook](https://webbook.nist.gov/chemistry/).

## Code

The final implementation of the IR simulations and calculate spectra similarities is available in the open-source [MLatom](https://github.com/dralgroup/mlatom).

The code below is the one used to perform the original study:
- You need to install [MLatom 3.13+](https://github.com/dralgroup/mlatom).
- The "specific_scaling.py" will scale the calculated IR spectra, broaden the spectra with Lorentzian line shape functions and compare with the experiment data.
- The "global_scaling.py" will calculate the optimal scaling factor and average similarity scores.
