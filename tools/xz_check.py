#!/usr/bin/env python3
"""Static integration checks only; not a substitute for Qt build and Android playback tests."""
from pathlib import Path
from xml.etree import ElementTree as ET
import re
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
delegate = re.search(r'delegate\s*:\s*Skin\.ControlButton\s*\{([^{}]*)\}', panel)
assert delegate, "XZColorFxPanel must retain its effect button delegate"
assert re.search(r'\brequired\s+property\s+int\s+index\b', delegate[1]), "XZ effect delegate must require index"
assert re.search(r'\brequired\s+property\s+string\s+modelData\b', delegate[1]), "XZ effect delegate must require modelData"
assert (root/'third_party/VynixDJ_skin/LICENSE').exists()
xml=list((root/'third_party/VynixDJ_skin').rglob('*.xml'))
for f in xml: ET.parse(f)
# QML required properties check for Knob / ControlKnob
knob_qml=(root/'res/qml/Knob.qml').read_text(encoding='utf8')
assert 'required property color color' in knob_qml, "Knob.qml must retain required property color"
knobs = re.findall(r'\bSkin\.ControlKnob\s*\{([^{}]*)\}', panel)
assert len(knobs) == panel.count('Skin.ControlKnob') == 2, "XZColorFxPanel must instantiate 2 flat ControlKnobs (CH1 and CH2)"
for deck, knob in enumerate(knobs, start=1):
 assert re.search(r'(?:^|[;\n])\s*color\s*:\s*[^;\s}]+', knob), f"CH{deck} ControlKnob must initialize required color"
 assert f'group: "[QuickEffectRack1_[Channel{deck}]]"' in knob, f"CH{deck} ControlKnob must use its native QuickEffectChain"
 assert re.search(r'\bkey\s*:\s*"super1"', knob), f"CH{deck} ControlKnob must control super1"

print(f'OK: static checks passed; {len(xml)} Vynix XML files parsed. Native compilation NOT performed.')
