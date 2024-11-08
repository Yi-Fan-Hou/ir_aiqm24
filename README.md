# Accurate and Affordable Simulation of Molecular Infrared Spectra with AIQM Models

The computational details are described at:

- Yi-Fan Hou, Cheng Wang, [Pavlo O. Dral](http://dr-dral.com). Accurate and Affordable Simulation of Molecular Infrared Spectra with AIQM Models. Preprint on ChemRxiv: https://doi.org/10.26434/chemrxiv-2024-r5prt.

## Data

- Calculated IR spectra are in the zip files prefixed with "static".
- Experiment data can be downloaded from the [NIST Chemistry Webbook](https://webbook.nist.gov/chemistry/).

## Code

- You need to install [MLatom 3.13+](https://github.com/dralgroup/mlatom).
- The "specific_scaling.py" will scale the calculated IR spectra, broaden the spectra with Lorentzian line shape functions and compare with the experiment data.
- The "global_scaling.py" will calculate the optimal scaling factor and average similarity scores.