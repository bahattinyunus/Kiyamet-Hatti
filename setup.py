from setuptools import setup, find_packages

setup(
    name="kiyamet-hatti",
    version="0.1.0",
    description="Digital Doomsday Communication Protocol & HAM Radio Simulator",
    author="Bahattin Yunus Çetin",
    packages=find_packages(),
    install_requires=[
        # No external dependencies, keeping it survivalist.
    ],
    entry_points={
        'console_scripts': [
            'kiyamet=src.main:main',
        ],
    },
)
