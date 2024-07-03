To run and upload the package you need to install a package called twine 

create the dist folder
```
python setup.py sdist
```

install dependency
```
pip install twine
````

upload with twine to pypi
```
twine upload --skip-existing dist/*
```