# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMultiprocessingLogging(PythonPackage):
	"""Logger for multiprocessing applications"""
	
	homepage = "https://github.com/jruere/multiprocessing-logging"
	pypi = "multiprocessing-logging/multiprocessing_logging-0.3.4-py2.py3-none-any.whl" 

	version("0.1", sha256="701e59d4815e191cd763675b3d1b0db1a28a2560114eafa474902a7e3e7b18b0", expand=False, url="https://files.pythonhosted.org/packages/55/11/9a335078e79e3b6f2b3a84c5fb386b301ec8bde53c16c00527ecd806c41c/multiprocessing_logging-0.1-py2-none-any.whl")
	version("0.2", sha256="60640f3ab0e82ddf065ebed7c7f49089e876705ad4356ff8a001cba0fe44f2fc", expand=False, url="https://files.pythonhosted.org/packages/1e/e6/132b7cdbe4aacd1cbef50a0ac2f5d6fb5b8e591c398884307c7afe5ceebc/multiprocessing_logging-0.2-py3-none-any.whl")
	version("0.2.1", sha256="e2fe9aa63a65e17f619d05b84677b41f4906894273ef4714fc75b09ee7d37b3d", expand=False, url="https://files.pythonhosted.org/packages/c8/17/c1e4e7e0ceb34ff348e348ddaa09bc149f7f87770e09e00981aeed96d299/multiprocessing_logging-0.2.1-py2.py3-none-any.whl")
	version("0.2.2", sha256="6e1365bcdb16b9fb41201668b05425e80503376bddd897d45458c63b49e28239", expand=False, url="https://files.pythonhosted.org/packages/f5/ce/2fc9ff60ae031a07fd27d582a878005fc081bb5916c9b75d73e7ac5e7a91/multiprocessing_logging-0.2.2-py2.py3-none-any.whl")
	version("0.2.3", sha256="7f1ea2934714dd8a25a283823c0baad658d1fd651d135dd981af5f4979dbc5fd", expand=False, url="https://files.pythonhosted.org/packages/ec/7e/9d2a7cb81d0213b6f0055c9304855174de887b0a18a3b4e7be0c57d49f17/multiprocessing_logging-0.2.3-py2.py3-none-any.whl")
	version("0.2.4", sha256="c5cc2c9c03e1d9b7383fb2f07f5f61fd563fee623d2be4649900a4c19eb0cce4", expand=False, url="https://files.pythonhosted.org/packages/62/cd/adfe5be532fd2870e34f4afc35354e96fbc30dff6e7d88fb9dacc93b649f/multiprocessing_logging-0.2.4-py2.py3-none-any.whl")
	version("0.2.5", sha256="c761016995392c1984993f34543a00b429ad88303982d4e41a723b8ce50ff063", expand=False, url="https://files.pythonhosted.org/packages/da/78/b346f11e1ac66dde4a0c742f6ab8ce516cd332113b277450d564eb3d2b65/multiprocessing_logging-0.2.5-py2.py3-none-any.whl")
	version("0.2.6", sha256="bbc437ab7a3803487267b13ccb7bc109633e85d2b509ea07e957f41065f4c908", expand=False, url="https://files.pythonhosted.org/packages/65/eb/1c3db9596eddb2bd1d1f8153dcaf2d9f2c7e144f4832d1b1449f681a0a7a/multiprocessing_logging-0.2.6-py2.py3-none-any.whl")
	version("0.3.0", sha256="76790aebe751a40c8bb63175e204db73b7a78b3d4e0b73a96b6d02a11b2630f5", expand=False, url="https://files.pythonhosted.org/packages/76/30/251cdbbb71b9abe4164dfe70a1341cde21098918c50eecd882c0d32f65ad/multiprocessing_logging-0.3.0-py2.py3-none-any.whl")
	version("0.3.1", sha256="9d3eb0f1f859b7ba6250a029726f77a7701999deda939595122d8748751de2e3", expand=False, url="https://files.pythonhosted.org/packages/2a/3f/9a123bb0f98b37956651dbc86d8a8821b6267ab96603c8a8b47d333e7f03/multiprocessing_logging-0.3.1-py2.py3-none-any.whl")
	version("0.3.2", sha256="dac775c8ca423291acd6623d2c72e2dfa7e9e596a22749afdae47eb5176e8616", expand=False, url="https://files.pythonhosted.org/packages/56/0e/0b4fb251e3b509d84a3806a40c57ec31889bae6f3605a369ac9728bab8ce/multiprocessing_logging-0.3.2-py2.py3-none-any.whl")
	version("0.3.3", sha256="c6f634b288495383597944d53baf6e511afe8cbb34753a9dd177dc2343e2d3ab", expand=False, url="https://files.pythonhosted.org/packages/19/5b/4efe65bcf7a9d0cda56912b4cf12647aad505a99325f0f56698b2d5e747a/multiprocessing_logging-0.3.3-py2.py3-none-any.whl")
	version("0.3.4", sha256="8a5be02b02edbd6fa6e3e89499af7680db69db9e2d8707fcd28d445fa248f23e", expand=False, url="https://files.pythonhosted.org/packages/9e/fe/32bd864bcb604b0607924a4cf618ed267a0ef21ac9c3e255109256046e1f/multiprocessing_logging-0.3.4-py2.py3-none-any.whl")

