from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from npe2 import implements
else:
    D = type("D", (), {"__getattr__": lambda *_: (lambda **_: (lambda f: f))})
    implements = D()


@implements.sample_data_generator(
    id="make_sample_data",
    title="Load sample data from Compiled Example",
    display_name='Compiled Example',
    key='unique_id.1'
)
def make_sample_data():
    import numpy

    return [(numpy.random.rand(512, 512), {})]
