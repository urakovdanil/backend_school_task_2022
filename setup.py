import os
from importlib.machinery import SourceFileLoader

from pkg_resources import parse_requirements
from setuptools import find_packages, setup


module_name = 'disc_backend'

# Модуль может быть еще не установлен (или установлена другая версия), поэтому
# необходимо загружать __init__.py с помощью machinery.
module = SourceFileLoader(
    module_name, os.path.join(module_name, '__init__.py')
).load_module()


def load_requirements(fname: str) -> list:
    requirements = []
    try:
        with open(fname, 'r') as fp:
            for req in parse_requirements(fp.read()):
                extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
                requirements.append(
                    '{}{}{}'.format(req.name, extras, req.specifier)
                )
    except FileNotFoundError:
        with open('/mnt/requirements.txt', 'r') as fp:
            for req in parse_requirements(fp.read()):
                extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
                requirements.append(
                    '{}{}{}'.format(req.name, extras, req.specifier)
                )
    return requirements


setup(
    name=module_name,
    version=module.__version__,
    author=module.__author__,
    author_email=module.__email__,
    license=module.__license__,
    description=module.__doc__,
    # long_description=open('README.rst').read(),
    # url='https://github.com/alvassin/backendschool2019',
    platforms='all',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    python_requires='>=3.8',
    include_package_data=True,
    packages=find_packages(exclude=['tests']),
    # package_dir={"": "disc_backend"},
    package_data={"": ["alembic.ini"]},
    # packages=['disc_backend'],
    # package_dir={'disc_backend': 'disc_backend'},
    # package_data={'disc_backend': ['disc_backend/api/*']},
    # install_requires=load_requirements('requirements.txt'),
    install_requires=[
        'aiohttp==3.6.3',
        'aiohttp-apispec==2.2.3',
        'aiomisc==9.6.36',
        'aiosignal==1.2.0',
        'alembic==1.3.3',
        'apispec==3.3.2',
        'async-timeout==3.0.1',
        'asyncpg==0.26.0',
        'asyncpgsa==0.27.1',
        'attrs==22.1.0',
        'chardet==3.0.4',
        'charset-normalizer==2.1.1',
        'colorlog==6.7.0',
        'ConfigArgParse==1.5.3',
        'fast-json==0.3.2',
        'frozenlist==1.3.1',
        'idna==3.4',
        'Jinja2==3.1.2',
        'Mako==1.2.2',
        'MarkupSafe==2.1.1',
        'marshmallow==3.17.1',
        'multidict==4.7.6',
        'packaging==21.3',
        'prettylog==0.3.0',
        'psycopg2-binary==2.9.3',
        'pyparsing==3.0.9',
        'python-dateutil==2.8.2',
        'python-editor==1.0.4',
        'pytz==2019.3',
        'six==1.16.0',
        'SQLAlchemy==1.3.14',
        'ujson==5.4.0',
        'webargs==5.5.3',
        'yarl==1.5.1',
    ],
    extras_require={'dev': load_requirements('requirements.dev.txt')},
    entry_points={
        'console_scripts': [
            # f-strings в setup.py не используются из-за соображений
            # совместимости.
            # Несмотря на то, что данный пакет требует python 3.8, технически
            # source distribution для него может собираться с помощью более
            # ранних версий python, не стоит лишать пользователей этой
            # возможности.
            '{0}-api = {0}.api.__main__:main'.format(module_name),
            '{0}-db = {0}.db.__main__:main'.format(module_name)
        ]
    }
)
