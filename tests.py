import unittest
from knowru_markdown import markdown_to_html

class TestKnowruMarkdownTestCase(unittest.TestCase):
    def test_paragraph(self):
        result = markdown_to_html('this is a paragraph.')
        self.assertEqual(result, '<p>this is a paragraph.</p>')

if __name__ == '__main__':
    unittest.main()
