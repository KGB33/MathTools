# MathTools

MathTools is a library containing a mountan of various algorithms, formulas, and profilers for mathmatic and sicentific computations

## Getting Started

### Requirments
  * Python 3.8+
  * poetry (recomended)
  
### Installation
  Create and activate a virtual envrionment, then install MathTools.
  
  
  Using poetry:
  
  ```
  poetry install
  poetry shell
  ```
  
  Using pip:
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
  
