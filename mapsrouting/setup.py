from setuptools import setup, find_packages

setup(
    name='maps',
    version='0.1.10',
    description='Visualize map paths implemented with Python',
    author='codusl100',
    author_email='codusl100@naver.com',
    url='https://github.com/Dongguk-MAPS/Routing-Visualization',
    packages=['maps'],
    package_dir={'maps': 'src/maps'},
    package_data={'maps': ['src/*']},
    install_requires=['folium', 'pandas', 'numpy', 'osrm', 'polyline'],
    keywords=['codusl100', 'MAPS', 'route visualization', 'python route visualization'],
    python_requires='>=3.6',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)