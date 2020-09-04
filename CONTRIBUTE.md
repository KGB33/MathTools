# Creating a pull request
Please check out [firstcontributions/first-contributions' README](https://github.com/firstcontributions/first-contributions/blob/master/README.md), they explain how to open and contribute to a PR better than I ever could.

## Pre-commit
It is reccomended that you install the pre-commit hooks, and required that you run them.
Install using `pre-commit install`

# Issues/Bugs

Please provide the following:
  * The code causing the issue.
  * The exact error message or the incorrect output
  * The Expected output


# Pull Requests
  * __PRs must pass all the CI tests.__

All new tools & upgrades must have:
  * Adequate Unit and Hypothosis tests
  * Type Hints

If your PR fixes an issue please add test(s) for that particular issue; and add a comment on the test with the issue number.

# Example

Lets say you wanted to add a function to calculate the area of a circle
given its radius.

You'd add the function under `geometry_tools/__init__.py`. If you're unsure where to
add your function feel free to ask.

The function itself would look as follows:

```python
from math import pi

from mttools.utils.types import Number

def area_of_circle(radius: Number) -> Number:
    """
    Calculates the area of a Circle with a given radius

    Examples:

    >>> area_of_circle(3)
    28.274333882308138
    >>> area_of_circle(-48)
    7238.229473870883

    """
    return radius * radius * pi
```

Note there are
  * type hints denoting the expected input and return types.
  * A Docstring containing a simple explanation and examples


Then, the corrisponding tests in `tests/test_geometry_tools/test_GeometryTools.py`

```python
from hypothesis import given
import hypothesis.strategies as st

from mttools.geometry_tools import area_of_circle

class TestAreaOfCircle:

    def test_interger_radius(self):
        assert area_of_circle(3) == 28.274333882308138

    @given(st.floats(allow_nan=False))
    def test_inverse_radius_gives_same_area(self, radius):
        inverse_radius = radius * -1
        assert area_of_circle(radius) == area_of_circle(inverse_radius)
```

The first test checks the correctness of one particular input.
whereas the second tests a property for several different inputs.
In this case the property revolves around r^2 == (-r)^2.

Then, run `git status`

```
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   mttools/geometry_tools/__init__.py
	modified:   tests/test_geometry_tools/test_GeometryTools.py

no changes added to commit (use "git add" and/or "git commit -a")
```

You should see the two files you changed.

```
	modified:   mttools/geometry_tools/__init__.py
	modified:   tests/test_geometry_tools/test_GeometryTools.py
```

Then run `git add <source_file> <test_file>`

In our case:

	source_file:   mttools/geometry_tools/__init__.py
	test_file:   tests/test_geometry_tools/test_GeometryTools.py

Then commit the files

```
> git commit -m "added area_of_circle function" >> CONTRIBUTE.md

Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...........................................(no files to check)Skipped
Check for added large files..............................................Passed
black....................................................................Failed
- hook id: black
- - files were modified by this hook
-
- reformatted /home/kgb33/Code/Projects/MathTools/tests/test_geometry_tools/test_GeometryTools.py
- All done! ✨ 🍰 ✨
- 1 file reformatted, 1 file left unchanged.
-
- [INFO] Restored changes from /home/kgb33/.cache/pre-commit/patch1595785601.
```

It looks like one of the pre-commit checks failed, lets see what files it modified.

```
> git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   mttools/geometry_tools/__init__.py
	modified:   tests/test_geometry_tools/test_GeometryTools.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   tests/test_geometry_tools/test_GeometryTools.py
```

It looks like the test file has changes that were not staged.

`git add <test_file>`

Then commit again:

```
❯ git commit -m "blacked"
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...........................................(no files to check)Skipped
Check for added large files..............................................Passed
black....................................................................Passed
[INFO] Restored changes from /home/kgb33/.cache/pre-commit/patch1595786294.
[master 1b289ed] blacked
 2 files changed, 30 insertions(+), 2 deletions(-)
```

It looks like all the checks passed, lets push our changes up to github now.


````
> git push

<Github Password Prompt>

Enumerating objects: 21, done.
Counting objects: 100% (21/21), done.
Delta compression using up to 12 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (12/12), 2.10 KiB | 430.00 KiB/s, done.
Total 12 (delta 8), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (8/8), completed with 7 local objects.
To github.com:KGB33/MathTools.git
   def7b88..1b289ed  master -> master
```
