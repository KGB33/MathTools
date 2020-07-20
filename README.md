# MathTools

MathTools is a library containing a mountan of various algorithms, formulas, and profilers for mathmatic and sicentific computations

## Getting Started

### System Requirments
  * Python 3.8+
  
## Installation

### Using Pip

```
pip install mttools
```

### From source
  
  First, clone this repository.
  ```
  git clone git@github.com:KGB33/MathTools.git
  ```
  or, using HTTPS
  ```
  git clone https://github.com/KGB33/MathTools.git
  ```
  
  Then, create a virtual environment and Install.
  ```
  python -m venv .venv
  source .venv/bin/activate
  pip install . -e
  ```

  
  
### Tests

  This project uses Pytest and mypy.
  
  ```
  pytest ./tests
  mypy ./mttools
  ```
  
## Contributing
  Pull requests are welcome!
  
  All pull requests must have:
    
  * Type hints
  * Hypothosis testing (if possable)
  * 100% test coverage
    
  For bug fixes:
    
   * Add a test checking for that error.
  
