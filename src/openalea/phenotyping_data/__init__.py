# -*- python -*-
#
#       Copyright INRIA - CIRAD - INRA
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
# ==============================================================================
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("openalea.phenotyping_data")
except PackageNotFoundError:
    # package is not installed
    pass
