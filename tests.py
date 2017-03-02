import unittest
from knowru_markdown import markdown_to_html

class TestKnowruMarkdownTestCase(unittest.TestCase):
    def test_paragraph(self):
        result = markdown_to_html('this is a paragraph.')
        self.assertEqual(result, '<p>this is a paragraph.</p>')

    def test_header(self):
        result = markdown_to_html('# this is a header')
        self.assertEqual(result, '<h1>this is a header</h1>')

if __name__ == '__main__':
    unittest.main()
