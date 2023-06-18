# -*- coding: utf-8 -*-

import os
import sys
import setuptools as st
from io import open

# Fix so that the setup.py usage is CWD-independent
SETUPDIR = os.path.abspath(os.path.dirname(__file__))
SETUPDIR = os.path.dirname(__file__)
PKGDIR = os.path.join(SETUPDIR, 'src')

sys.path.append(PKGDIR)
import imreg_dft

reqsfname = os.path.join(SETUPDIR, 'requirements.txt')
reqs = open(reqsfname, 'r', encoding='utf-8').read().strip().splitlines()

descfname = os.path.join(SETUPDIR, 'doc', 'description.rst')
longdesc = open(descfname, 'r', encoding='utf-8').read()

st.setup(
    name="imreg_dft_nw",
    version=imreg_dft.__version__,
    author=u"Matěj Týč",
    author_email="matej.tyc@gmail.com",
    description=("Tiny no-warn fork of imreg_dft, Image registration "
                 "utility using algorithms based on "
                 "discrete Fourier transform (DFT, FFT), "
                 "To get rid of those np.bool deprecation warnings."),
    license="BSD",
    url="https://github.com/xtofl/imreg_dft_nw",
    package_dir = {'': PKGDIR},
    packages = st.find_packages(PKGDIR),
    entry_points = {
        'console_scripts': [
           'ird = imreg_dft.cli:main',
           'ird-tform = imreg_dft.tform:main',
           'ird-show = imreg_dft.show:main',
        ],
    },
    install_requires=reqs,
    extras_require={
        'plotting':  ["matplotlib>=1.2"],
        'loading images': ["pillow>=2.2"],
        'better performance': ["pyfftw>=0.9"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ],
    long_description=longdesc,
    zip_safe=True,
)
