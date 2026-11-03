import contextlib
import io
from pathlib import Path
import runpy
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
PANEL_PATH = ROOT / 'res/qml/XZColorFxPanel.qml'
PANEL = PANEL_PATH.read_text(encoding='utf8')
READ_TEXT = Path.read_text


class XZCheckTest(unittest.TestCase):
    def check_panel(self, panel):
        def read_text(path, *args, **kwargs):
            if path == PANEL_PATH:
                return panel
            return READ_TEXT(path, *args, **kwargs)

        with patch.object(Path, 'read_text', read_text), contextlib.redirect_stdout(io.StringIO()):
            runpy.run_path(str(ROOT / 'tools/xz_check.py'), run_name='__main__')

    def test_repository_panel(self):
        self.check_panel(PANEL)

    def test_missing_ch1_color_even_with_matching_color_elsewhere(self):
        panel = PANEL.replace('color: "#fb477d";', '', 1)
        panel += '\nText { color: "#fb477d" }\n'
        with self.assertRaisesRegex(AssertionError, 'CH1.*color'):
            self.check_panel(panel)

    def test_missing_ch2_color_even_with_matching_color_elsewhere(self):
        prefix, color, suffix = PANEL.rpartition('color: "#fb477d";')
        self.assertTrue(color)
        panel = prefix + suffix + '\nText { color: "#fb477d" }\n'
        with self.assertRaisesRegex(AssertionError, 'CH2.*color'):
            self.check_panel(panel)

    def test_original_crashing_panel(self):
        panel = PANEL.replace('color: "#fb477d";', '')
        with self.assertRaisesRegex(AssertionError, 'CH1.*color'):
            self.check_panel(panel)

    def test_duplicate_deck_group(self):
        panel = PANEL.replace('[QuickEffectRack1_[Channel2]]', '[QuickEffectRack1_[Channel1]]')
        with self.assertRaisesRegex(AssertionError, 'CH2.*QuickEffectChain'):
            self.check_panel(panel)

    def test_wrong_knob_key(self):
        with self.assertRaisesRegex(AssertionError, 'CH1.*super1'):
            self.check_panel(PANEL.replace('key: "super1"', 'key: "mix"', 1))

    def test_valid_alternative_color(self):
        self.check_panel(PANEL.replace('color: "#fb477d";', 'color: "#ffffff";'))

    def test_missing_delegate_index(self):
        with self.assertRaisesRegex(AssertionError, 'delegate.*index'):
            self.check_panel(PANEL.replace('required property int index', ''))

    def test_missing_delegate_model_data(self):
        with self.assertRaisesRegex(AssertionError, 'delegate.*modelData'):
            self.check_panel(PANEL.replace('required property string modelData', ''))


if __name__ == '__main__':
    unittest.main()
