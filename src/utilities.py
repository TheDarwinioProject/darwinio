# The GPLv3 License (GPLv3)

# Copyright (c) 2023 Tushar Maharana, and Mihir Nallagonda

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Various functions which don't fit-in in other files."""

import numpy as np
import hashlib as hlib


def normalize(arr: np.ndarray) -> np.ndarray:
    """Normalize the Numpy Array."""
    magnitude: np.floating = np.linalg.norm(arr)
    return np.nan_to_num(arr / magnitude)


def array2hex(array: np.ndarray) -> str:
    return hlib.sha1(array.tobytes()).hexdigest()
