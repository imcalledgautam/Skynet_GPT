# src/test_version.py
import streamlit as st
from unittest.mock import patch, mock_open

class TestVersion(unittest.TestCase):
    def setUp(self):
        self.streamlit_mock = patch('streamlit.markdown')
        self.open_mock = patch('__builtin__.open', mock_open(read_data="Skynet v1.0\n"))
        self.streamlit_mock.start()
        self.open_mock.start()

    @patch('src.version.VERSION', 'v2.0')
    def test_render_version_badge(self):
        # Test case: Render the version badge with a new version
        render_version_badge()
        output = self.streamlit_mock.mock_calls[0][1]
        expected_output = '<p style="text-align: right; font-size: 0.9em;">Skynet v2.0</p>'
        self.assertEqual(output, expected_output)

    @patch('src.version.VERSION', 'v3.0')
    def test_render_version_badge_with_default(self):
        # Test case: Render the version badge with the default version
        render_version_badge()
        output = self.streamlit_mock.mock_calls[0][1]
        expected_output = '<p style="text-align: right; font-size: 0.9em;">Skynet v3.0</p>'
        self.assertEqual(output, expected_output)

    def tearDown(self):
        self.streamlit_mock.stop()
        self.open_mock.stop()

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)