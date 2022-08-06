from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from npe2 import implements
else:
    D = type("D", (), {"__getattr__": lambda *_: (lambda **_: (lambda f: f))})
    implements = D()


@implements.reader(
    id="get_reader",
    title="Open data with Compiled Example",
    filename_patterns=["*.npy"],
)
def napari_get_reader(path):
    if str(path).endswith(".npy"):
        return reader_function


def reader_function(path):
    paths = [path] if isinstance(path, str) else path
    arrays = [np.load(_path) for _path in paths]
    data = np.squeeze(np.stack(arrays))
    return [(data,)]
