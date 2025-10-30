# rocket_relations

Short description: Python package for computing **ideal rocket propulsion parameters**: the **characteristic velocity (c\*)** and **thrust coefficient (Cf)**.  

## Installation

Download the source code or clone the repo locally.

In the project root directory, open a terminal and create/activate
a fresh conda environment (or reuse an existing one):

```
bash
conda create -n rocketenv python=3.14
conda activate rocketenv
pip install -e .
```

## Quickstart
``` python
#import top level API
__init__.py
#define parameters
T0 = 3500
gamma = 1.2
R = 350
pep0 = 0.0125
pap0 = 0.02
AeAstar = 10
#calculate results
charVel(gamma, R, T0)
thrustCoeff(pep0, pap0, AeAstar, gamma)
```

## Details
use help(rocket_relations.ideal)

## Test
Running pytest -q will execute the following file:
\rocket-relations\tests\test_ideal.py
This test will run both functions with the values defined in Quickstart.
The expected results are c* ≈ 1706.6214 m/s and CF ≈ 1.5423079 (rounded to 8 significant figures).
A successful test will return "[100%] 1 passed".



