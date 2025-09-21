# tolerant-float 

Extensions of the Python `float` data-type, which permits arbitrary (absolute) tolerance used in comparison operations.

Use-cases where this may be useful include:
- outputs from parallelised arithmetic operations (common in HPC work)
- outputs resulting from casting smaller datatypes (e.g. float16) as python floats (common in GPUs)

---

### Installation

I don't plan to put this on PyPI unless it gains traction, to avoid cluttering the namespace there.

Instead, you can install the latest version [`v0.0.1`] with pip directly from github;
```bash
pip install git+https://github.com/LukeRoantree4815162342/TolerantFloat@v0.0.1
```

### TolerantFloat class

A `TolerantFloat` instance of value `5.34` and tolerance `1e-5` can be created as
```python
a = TolerantFloat(5.34, tol=5)

a==5.35 # False
a==5.340001 # True
```

You can specify whether the string representation of a TolerantFloat object should remain the same as a normal float, or whether the tolerance should be displayed too;
```python
a = TolerantFloat(5.34, tol=5)
b = TolerantFloat(5.34, tol=5, show_tol=True)

print(a) # 5.34
print(b) # 5.34 ± 1e-05
```

All comparison operations involving equality (`==`, `!=`, `<=`, `>=`) will make use of the tolerance(s) asssociated with TolerantFloat object(s) on the left or right of the operator.

All arithmetic operations on a TolerantFloat object will return a TolerantFloat instance, with the same tolerance as the original. In cases where two or more TolerantFloat objects are involved, the most restrictive tolerance is used.

### AdaptiveTolerantFloat class (planned)
An `AdaptiveTolerantFloat` class is in development, which will behave similarly to the TolerantFloat class but with the instances created via aritmetic operations having 'adaptive' tolerances, in line with the principles of the propagation of uncertainty