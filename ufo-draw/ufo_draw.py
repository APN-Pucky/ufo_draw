import feynml
from pyqgraf import qgraf

from feynmodel.interface.qgraf import feynmodel_to_qgraf, qgraf_to_feynmodel
from feynmodel.interface.ufo import load_ufo_model


def main():
    path = "/home/apn/git/feynmodel/models/ufo/sm/"
    loops = 0

    # Load the UFO
    fm = load_ufo_model(path)
    # Convert to QGRAF
    qgrafmodel = feynmodel_to_qgraf(fm, True)
    # Run QGRAF
    xml_string = qgraf.run(
        "nu_e[p1], nu_e_bar[p2]",
        "nu_e[p3], nu_e_bar[p4]",
        loops=loops,
        loop_momentum="l",
        model=qgrafmodel,
        style=feynml.interface.qgraf.get_style(),
    )
    # Render the Feynman diagrams

