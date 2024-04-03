# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModsem(RPackage):
	"""Latent Interaction (and Moderation) Analysis in Structural
Equation Models (SEM)

	
    Estimation of interaction (i.e., moderation) effects between latent variables
    in structural equation models (SEM). 
    The supported methods are:
      The constrained approach (Algina & Moulder, 2001).
      The unconstrained approach (Marsh et al., 2004).
      The residual centering approach (Little et al., 2006).
      The double centering approach (Lin et al., 2010).
      The latent moderated structural equations (LMS) approach (Klein & Moosbrugger, 2000).
      The quasi-maximum likelihood (QML) approach (Klein & Muthén, 2007)
    The constrained- unconstrained, residual- and double centering- approaches
    are estimated via 'lavaan' (Rosseel, 2012), whilst the LMS- and QML- approaches
    are estimated via 'nlsem' (Umbach et al., 2017). Alternatively model can be
    estimated via 'Mplus' (Muthén & Muthén, 1998-2017).
    References:
    Algina, J., & Moulder, B. C. (2001). 
      <doi:10.1207/S15328007SEM0801_3>.
      "A note on estimating the Jöreskog-Yang model for latent variable interaction using 'LISREL' 8.3."
    Klein, A., & Moosbrugger, H. (2000). 
      <doi:10.1007/BF02296338>.
      "Maximum likelihood estimation of latent interaction effects with the LMS method."
    Klein, A. G., & Muthén, B. O. (2007). 
      <doi:10.1080/00273170701710205>.
      "Quasi-maximum likelihood estimation of structural equation models with multiple interaction and quadratic effects."
    Lin, G. C., Wen, Z., Marsh, H. W., & Lin, H. S. (2010). 
      <doi:10.1080/10705511.2010.488999>.
      "Structural equation models of latent interactions: Clarification of orthogonalizing and double-mean-centering strategies."
    Little, T. D., Bovaird, J. A., & Widaman, K. F. (2006). 
      <doi:10.1207/s15328007sem1304_1>.
      "On the merits of orthogonalizing powered and product terms: Implications for modeling interactions among latent variables."
    Marsh, H. W., Wen, Z., & Hau, K. T. (2004). 
      <doi:10.1037/1082-989X.9.3.275>.
      "Structural equation models of latent interactions: evaluation of alternative estimation strategies and indicator construction."
    Muthén, L.K. and Muthén, B.O. (1998-2017).  
      "'Mplus' User’s Guide.  Eighth Edition."
      <https://www.statmodel.com/>.
    Umbach N, Naumann K, Brandt H, Kelava A (2017). 
      "Fitting Nonlinear Structural Equation Models in R with Package 'nlsem'."
      <doi:10.18637/jss.v077.i07>.
    Rosseel Y (2012). 
      <doi:10.18637/jss.v048.i02>.
      "'lavaan': An R Package for Structural Equation Modeling." 
	"""
	
	homepage = "https://github.com/Kss2k/modsem"
	cran = "modsem" 

	version("0.1.0", md5="fe5848561c15c97294f0b8400f582cba")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-mplusautomation", type=("build", "run"))
	depends_on("r-nlsem", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
