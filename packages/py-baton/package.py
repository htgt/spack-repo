# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBaton(PythonPackage):
    """Python 3 Wrapper for baton."""

    homepage = "https://github.com/wtsi-hgi/python-baton-wrapper"
    pypi = "baton/baton-1.0.1.tar.gz"

    version("1.0.2", sha256="6b525acaed8961d88fc4ab668d188838e6794128ee76c6c32f2410c45adad2cc")
    version("1.0.1", sha256="76861bfa884b9a80333c5e3ac9d8636517e08ceeac4837c23e8d2bd700c5d8c6")

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-hgijson@1.3.1", type=("build", "run"))
    depends_on("py-hgicommon@1.2", type=("build", "run"), when="@1.0.1")
    depends_on("py-hgicommon@1.3.2", type=("build", "run"), when="@1.0.2")
    depends_on("py-python-dateutil@2.5.3", type=("build", "run"))
