#!/usr/bin/env python3
# SPDX-License-Identifier: (GPL-2.0-or-later OR BSD-2-Clause)

# While Python 3 is the default, it's also possible to invoke
# this setup.py script with Python 2.

"""
setup.py file for SWIG libfdt
Copyright (C) 2017 Google, Inc.
Written by Simon Glass <sjg@chromium.org>
"""

from setuptools import setup, Extension
import os
import re
import sys

srcdir = os.path.dirname(__file__)

def get_top_builddir():
    if '--top-builddir' in sys.argv:
        index = sys.argv.index('--top-builddir')
        sys.argv.pop(index)
        return sys.argv.pop(index)
    else:
        return srcdir

top_builddir = get_top_builddir()

libfdt_module = Extension(
    '_libfdt',
    sources=[os.path.join(srcdir, 'pylibfdt/libfdt.i')],
    include_dirs=[os.path.join(srcdir, 'libfdt')],
    libraries=['fdt'],
    library_dirs=[os.path.join(top_builddir, 'libfdt')],
    swig_opts=['-I' + os.path.join(srcdir, 'libfdt')],
)

setup(
    name='libfdt',
    use_scm_version={
        "root": srcdir,
    },
    setup_requires = ['setuptools_scm'],
    author='Simon Glass',
    author_email='sjg@chromium.org',
    description='Python binding for libfdt',
    ext_modules=[libfdt_module],
    package_dir={'': os.path.join(srcdir, 'pylibfdt')},
    py_modules=['libfdt'],
)
