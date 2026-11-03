import "." as Skin
import Mixxx 1.0 as Mixxx
import QtQuick
import QtQuick.Layouts
import "Theme"

Rectangle {
    id: root
    width: 490
    height: 158
    radius: 8
    color: "#151923"
    border.color: "#53627a"
    border.width: 1
    z: 200

    Mixxx.ControlProxy {
        id: selectedFx
        group: "[Skin]"
        key: "color_fx_current"
    }

    Column {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 8
        Text { text: "XZ COMPANION  ·  SOUND COLOR FX"; color: "#dce7ff"; font.bold: true; font.pixelSize: 14 }
        Row {
            spacing: 5
            Repeater {
                model: ["FILTER", "SPACE", "DUB ECHO", "SWEEP", "NOISE", "CRUSH"]
                delegate: Skin.ControlButton {
                    width: index === 2 ? 83 : 70
                    height: 35
                    text: modelData
                    font.pixelSize: 10
                    group: "[Skin]"
                    key: "color_fx_select_" + (index + 1)
                    activeColor: "#fb477d"
                    highlight: selectedFx.value === index + 1
                }
            }
        }
        Row {
            spacing: 8
            Text { text: "CH1"; width: 36; anchors.verticalCenter: parent.verticalCenter; color: "#dce7ff" }
            Skin.ControlKnob { group: "[QuickEffectRack1_[Channel1]]"; key: "super1"; color: "#fb477d"; width: 40; height: 40 }
            Text { text: "CH2"; width: 36; anchors.verticalCenter: parent.verticalCenter; color: "#dce7ff" }
            Skin.ControlKnob { group: "[QuickEffectRack1_[Channel2]]"; key: "super1"; color: "#fb477d"; width: 40; height: 40 }
            Text { text: "FX seleccionado en ambos decks; cada knob controla su canal"; color: "#b8c6d9"; font.pixelSize: 10; anchors.verticalCenter: parent.verticalCenter }
        }
    }
}
