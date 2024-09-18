# Title
Argonaute-mediated Digital Sensor Based on a Magnetic Beads-assisted Imaging Transcoding System for Multiplexed Detection of Foodborne Pathogens

## Overview of Panda
We developed an AI algorithm platform named "Panda". The Panda platform accurately classifies, grades, and counts MBs. It also calculates the nucleic acid concentration based on the total number of obtained fluorescent MBs.


## Environmental setup
- `Python 3.x`
- `numpy`
- `scipy`
- `scikit-image`
- `pandas`
  
Here are the steps you need to take to install the python environment and the above libraries:

### 1. Install Python 3.x (if not installed)
Ensure that Python 3.x is installed. You can download it from the [official Python website](https://www.python.org/).

### 2. Update `pip` (optional)
It's a good practice to keep `pip` up to date. Open a terminal (or command prompt) and run the following command:

```bash
python -m pip install --upgrade pip
```

### 3. Install Required Libraries
To install the necessary packages (`numpy`, `scipy`, `scikit-image`, `pandas`), run the following command in your terminal or command prompt:

```bash
pip install numpy scipy scikit-image pandas
```

### 4. Verify Installation
After installation, you can verify that the libraries are installed correctly by running this Python script:

```python
import numpy as np
import scipy
import skimage
import pandas as pd

print(f"numpy version: {np.__version__}")
print(f"scipy version: {scipy.__version__}")
print(f"scikit-image version: {skimage.__version__}")
print(f"pandas version: {pd.__version__}")
```

This script will print the installed versions of the libraries. If you see the version numbers printed without any errors, the libraries were installed successfully.

## Run
```bash
python panda.py
```
