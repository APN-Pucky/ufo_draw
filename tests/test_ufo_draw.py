from pyqgraf import qgraf

from feynmodel.interface.qgraf import feynmodel_to_qgraf, qgraf_to_feynmodel
from feynmodel.interface.ufo import load_ufo_model

from xsdata.formats.dataclass.parsers import XmlParser
from pyfeyn2.render.latex.feynmp import FeynmpRender
from pyfeyn2.render.latex.tikzfeynman import TikzFeynmanRender
from pyfeyn2.render.pyx.pyxrender import PyxRender
from pyfeyn2.feynmandiagram import FeynML

from pyfeyn2.auto.bend import auto_bend
from pyfeyn2.auto.label import auto_label
from pyfeyn2.auto.position import feynman_adjust_points

from feynml.interface import qgraf as iqgraf
from ufo_draw.ufo_diagrams import generate_diagrams

from pyfeyn2.auto.diagram import auto_diagram
from pyfeyn2.render.latex.tikzfeynman import TikzFeynmanRender

def test_ufo_draw():
    # Parameters
    #path = "/home/apn/git/feynmodel/models/ufo/sm/"
    path = "ufo_sm"
    loops = 0
    fml = generate_diagrams(path, 
            ["nu_e", "nu_e_bar"],
            ["nu_e", "nu_e_bar"], loops=loops)
    for d in fml.diagrams:
        auto_diagram(d)
        t = TikzFeynmanRender(d)
        #print(t.get_src())
        t.render(show=True)