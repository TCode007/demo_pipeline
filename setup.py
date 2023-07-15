from setuptools import setup, find_packages

setup(name="censor_income",
      version="0.0.1",
      author ="Ram",
      author_email="ram@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )