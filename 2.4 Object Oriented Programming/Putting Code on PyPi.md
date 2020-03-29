Putting Code on PyPi
---
---

[watch video](https://www.youtube.com/watch?v=4uosDOKn5LI)

PyPi vs. Test PyPi
---


Note that [pypi.org](https://pypi.org/) and [test.pypy.org](https://test.pypi.org/) are two different websites. You'll need to register separately at each website. If you only register at pypi.org, you will not be able to upload to the test.pypy.org repository.

Also, remember that your package name must be unique. If you use a package name that is already taken, you will get an error when trying to upload the package.

Summary of the Terminal Commands Used in the Video
---
```
cd binomial_package_files
python setup.py sdist
pip install twine

# commands to upload to the pypi test repository
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ dsnd-probability

# command to upload to the pypi repository
twine upload dist/*
pip install dsnd-probability
```

**More PyPi Resources**

Tutorial on distributing packages
This link has a good [tutorial on distributing Python packages](https://packaging.python.org/tutorials/distributing-packages/) including more configuration options for your setup.py file. You'll notice that the python command to run the `setup.py` is slightly different with

```
python3 setup.py sdist bdist_wheel
```

This command will still output a folder called `dist`. The difference is that you will get both a .tar.gz file and a .whl file. The .tar.gz file is called a source archive whereas the .whl file is a built distribution. The .whl file is a newer type of installation file for Python packages. When you pip install a package, pip will first look for a whl file (wheel file) and if there isn't one, will then look for the tar.gz file.

A tar.gz file, ie an sdist, contains the files needed to [compile](https://en.wikipedia.org/wiki/Compiler) and install a Python package. A whl file, ie a built distribution, only needs to be copied to the proper place for installation. Behind the scenes, pip installing a whl file has fewer steps than a tar.gz file.

Other than this command, the rest of the steps for uploading to PyPi are the same.

Other Links

If you'd like to learn more about PyPi, here are a couple of resources:

[Overview of PyPi](https://docs.python.org/3/distutils/packageindex.html)

[MIT License](https://opensource.org/licenses/MIT)
