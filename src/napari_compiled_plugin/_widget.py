"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from typing import TYPE_CHECKING

from magicgui import magic_factory
from qtpy.QtWidgets import QHBoxLayout, QPushButton, QWidget

if TYPE_CHECKING:
    import napari
    from npe2 import implements
else:
    D = type("D", (), {"__getattr__": lambda *_: (lambda **_: (lambda f: f))})
    implements = D()


@implements.widget(
    id="make_qwidget",
    display_name="Example QWidget",
    title="Make example QWidget",
)
class ExampleQWidget(QWidget):
    # your QWidget.__init__ can optionally request the napari viewer instance
    # in one of two ways:
    # 1. use a parameter called `napari_viewer`, as done here
    # 2. use a type annotation of 'napari.viewer.Viewer' for any parameter
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer

        btn = QPushButton("Click me!")
        btn.clicked.connect(self._on_click)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(btn)

    def _on_click(self):
        print("napari has", len(self.viewer.layers), "layers")


@implements.widget(
    id="make_magic_widget",
    display_name="Example Magic Widget",
    title="Make example magic widget",
)
@magic_factory
def example_magic_widget(img_layer: "napari.layers.Image"):
    print(f"you have selected {img_layer}")


@implements.widget(
    id="make_func_widget",
    display_name="Example Function Widget",
    title="Make example function widget",
    autogenerate=True,
)
def example_function_widget(img_layer: "napari.layers.Image"):
    print(f"you have selected {img_layer}")
