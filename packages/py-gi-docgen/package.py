# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGiDocgen(PythonPackage):
    """GI-DocGen is a document generator for GObject-based libraries. GObject is the base type system of the GNOME project. GI-Docgen reuses the introspection data generated by GObject-based libraries to generate the API reference of these libraries, as well as other ancillary documentation."""

    homepage = "https://gitlab.gnome.org/GNOME/gi-docgen"
    pypi = "gi_docgen/gi_docgen-2025.3.tar.gz"

    version("2025.3", sha256="2fdb4f0f6b61184ab862fcfb41dafe1a795636de9fd8d21a8ca4feea3b6bf858")

    depends_on("py-setuptools", type=("build"))
