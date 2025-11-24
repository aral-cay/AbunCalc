# AbunCalc

AbunCalc is a small desktop application written in Python (Tkinter + Matplotlib) to assist with stellar abundance analysis.  
It provides a graphical interface around the `abundance.exe` routine from the SPECTRUM suite (R. O. Gray) and is intended to make the workflow for line–by–line abundance work more convenient and reproducible.

The code was originally written for personal/academic use in stellar spectroscopy projects.

---

## What the application does

AbunCalc does not perform any radiative transfer or abundance calculations by itself.  
Instead, it:

1. Collects the inputs needed by `abundance.exe` through a simple GUI:
   - Model atmosphere file  
   - Line input file  
   - Atom file  
   - Microturbulence velocity (km/s)

2. Writes these inputs into a temporary `inputs.txt` file and calls:

   ```text
   abundance.exe -it <inputs.txt
