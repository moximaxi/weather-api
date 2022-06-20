from setuptools import setup

setup(
   name='app',
   version='1.0',
   description='Weather API',
   author='MaxiMoxi',
   packages=['app'],
   install_requires=['fastapi', 'uvicorn', 'starlette', 'httpx', 'sqlalchemy', 'psycopg2', 'jinja2'],
)