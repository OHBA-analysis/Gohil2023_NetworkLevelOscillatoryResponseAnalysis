"""Save training data as npy files.

"""

from glob import glob
from osl_dynamics.data import Data

files = sorted(glob("data/src/*/sflip_parc-raw.fif"))
data = Data(files, picks="misc", reject_by_annotation="omit")
data.save("data/npy")
data.delete_dir()
