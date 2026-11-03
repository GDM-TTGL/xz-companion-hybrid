#!/usr/bin/env python3
"""Static integration checks only; not a substitute for Qt build and Android playback tests."""
from pathlib import Path
from xml.etree import ElementTree as ET
import sys
root=Path(__file__).resolve().parents[1]
cpp=(root/'src/qml/qmlapplication.cpp').read_text(encoding='utf8')
h=(root/'src/qml/qmlapplication.h').read_text(encoding='utf8')
qml=(root/'res/qml/MainWindow.qml').read_text(encoding='utf8')
panel=(root/'res/qml/XZColorFxPanel.qml').read_text(encoding='utf8')
assert cpp.count('void QmlApplication::setupXZColorFx()')==1
assert cpp.count('    setupXZColorFx();')==1
assert 'std::vector<std::unique_ptr<ControlObject>> m_xzColorFxControls;' in h
for i in range(1,7):
 assert f'color_fx_select_{i}' in cpp or 'color_fx_select_%1' in cpp
assert 'Skin.XZColorFxPanel {' in qml
assert 'model: ["FILTER", "SPACE", "DUB ECHO", "SWEEP", "NOISE", "CRUSH"]' in panel
assert (root/'third_party/VynixDJ_skin/LICENSE').exists()
xml=list((root/'third_party/VynixDJ_skin').rglob('*.xml'))
for f in xml: ET.parse(f)
print(f'OK: static checks passed; {len(xml)} Vynix XML files parsed. Native compilation NOT performed.')
