"""
This module is an example of a barebones writer plugin for napari.

It implements the Writer specification.
see: https://napari.org/stable/plugins/guides.html?#writers

Replace code below according to your needs.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Sequence, Tuple, Union

if TYPE_CHECKING:
    from npe2 import implements

    DataType = Union[Any, Sequence[Any]]
    FullLayerData = Tuple[DataType, dict, str]
else:
    D = type("D", (), {"__getattr__": lambda *_: (lambda **_: (lambda f: f))})
    implements = D()


@implements.writer(
    id="write_multiple",
    title="Save multi-layer data with Compiled Example",
    layer_types=["image*", "labels*"],
    filename_extensions=[],
)
def write_multiple(path: str, data: List[FullLayerData]) -> List[str]:
    """Writes multiple layers of different types."""

    # implement your writer logic here ...

    # return path to any file(s) that were successfully written
    return [path]


@implements.writer(
    id="write_single_image",
    title="Save image data with Compiled Example",
    layer_types=["image"],
    filename_extensions=[".npy"],
)
def write_single_image(path: str, data: Any, meta: dict) -> List[str]:
    """Writes a single image layer"""

    # implement your writer logic here ...

    # return path to any file(s) that were successfully written
    return [path]
