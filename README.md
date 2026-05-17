# Semiconductor Formula Calculator

## Aim
The aim of this project is to build a beginner-friendly Python program that calculates important first-year semiconductor physics formulas through a simple menu-driven interface.

## Introduction
Semiconductors are materials whose electrical conductivity lies between conductors and insulators. They are the foundation of modern electronic devices such as diodes, transistors, integrated circuits, sensors, and solar cells. This software project helps students understand semiconductor behavior by converting classroom formulas into a working calculator.

## Features
- Menu-driven interface for easy use
- Beginner-friendly Python code with comments
- Modular file structure using separate files for formulas and utilities
- Input validation to prevent crashes
- Formula display before every calculation
- Answers shown clearly with units
- Multiple calculations in one run
- Uses only standard Python libraries

## Physics Connection
Semiconductor devices are based on charge carriers, conductivity, band gap, drift current, diode current, and Hall effect. These formulas help explain how semiconductor materials behave inside electronic devices and how properties such as current flow, voltage response, and carrier concentration can be studied.

## List of Formulas
1. Conductivity
   `sigma = q(n*mu_n + p*mu_p)`
2. Resistivity
   `rho = 1 / sigma`
3. Intrinsic carrier concentration relation
   `np = ni^2`
   `ni = sqrt(n*p)`
   `n = ni^2 / p`
   `p = ni^2 / n`
4. Electron concentration in n-type semiconductor
   `n ~= Nd`
5. Hole concentration in p-type semiconductor
   `p ~= Na`
6. Minority carrier concentration in n-type semiconductor
   `p = ni^2 / Nd`
7. Minority carrier concentration in p-type semiconductor
   `n = ni^2 / Na`
8. Band gap energy using wavelength
   `Eg = 1240 / lambda`
9. Photon energy
   `E = hc / lambda`
   `E(eV) = 1240 / lambda(nm)`
10. Thermal voltage
   `VT = kT / q`
11. Diode current using Shockley equation
   `I = I0(e^(V / (eta*VT)) - 1)`
12. Cut-in voltage information
   Silicon diode `~ 0.7 V`
   Germanium diode `~ 0.3 V`
13. Drift current
   `Idrift = n*q*A*vd`
14. Drift velocity
   `vd = mu*E`
15. Electric field
   `E = V / L`
16. Current density
   `J = sigma*E`
17. Hall coefficient
   `RH = 1 / (n*q)`
18. Hall voltage
   `VH = RH*I*B / t`
19. Fermi level explanation
   For intrinsic semiconductors, the Fermi level is approximately at the middle of the forbidden energy gap.
20. Semiconductor type detector
   If `n > p`, output N-type semiconductor
   If `p > n`, output P-type semiconductor
   If `n = p`, output Intrinsic semiconductor

## Folder Structure
```text
semiconductor_formula_calculator/
|-- main.py
|-- formulas.py
|-- utils.py
|-- README.md
`-- requirements.txt
```

## How to Run
1. Make sure Python 3 is installed on your computer.
2. Open a terminal in the project folder.
3. Run the program with:

```bash
python main.py
```

## Sample Input/Output

### Sample 1: Thermal Voltage
```text
Enter your choice (1-19): 8

Thermal Voltage
---------------
Formula: VT = kT / q
Constants used: k = 1.381e-23 J/K, q = 1.602e-19 C
Enter temperature T (K): 300

Thermal voltage VT = 0.025861 V
```

### Sample 2: Band Gap Energy
```text
Enter your choice (1-19): 6

Band Gap Energy
---------------
Formula: Eg = 1240 / lambda
Eg is in eV when wavelength lambda is in nm.
Enter wavelength lambda (nm): 620

Band gap energy Eg = 2 eV
```

### Sample 3: Conductivity
```text
Enter your choice (1-19): 1

Conductivity
------------
Formula: sigma = q(n*mu_n + p*mu_p)
Constant used: q = 1.602e-19 C
Enter electron concentration n (per m^3): 1e21
Enter hole concentration p (per m^3): 5e20
Enter electron mobility mu_n (m^2/V.s): 0.14
Enter hole mobility mu_p (m^2/V.s): 0.05

Conductivity = 26.433 S/m
```

### Sample 4: Semiconductor Type Detector
```text
Enter your choice (1-19): 18

Semiconductor Type Detector
---------------------------
Rule:
If n > p, the material is n-type.
If p > n, the material is p-type.
If n = p, the material is intrinsic.
Enter electron concentration n (per m^3): 2e16
Enter hole concentration p (per m^3): 8e15

Detected type: N-type semiconductor
```

## Applications
- Learning basic semiconductor physics formulas
- Supporting first-year laboratory and project work
- Quick revision before physics practicals or viva
- Understanding carrier concentration and diode behavior
- Demonstrating how physics formulas can be implemented in software

## Conclusion
This project combines physics and programming in a simple and practical way. It helps students calculate key semiconductor quantities, understand the meaning of important formulas, and see how software can be used to study electronic materials.
