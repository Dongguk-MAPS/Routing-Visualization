from setuptools import setup, find_packages

setup(
    name='mapsrouting',
    version='0.0.7',
    description='Visualize map paths implemented with Python',
    author='codusl100',
    author_email='codusl100@naver.com',
    url='https://github.com/Dongguk-MAPS/Routing-Visualization',
    packages=find_packages(exclude=[]),
    keywords=['codusl100', 'MAPS', 'route visualization', 'python route visualization'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)