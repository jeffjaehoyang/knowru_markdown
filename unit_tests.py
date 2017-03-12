import unittest
from knowru_markdown import markdown_to_html

class KnowruMarkdownUnitTestTestCase(unittest.TestCase):
    def test_paragraph(self):
        result = markdown_to_html('this is a paragraph.')
        self.assertEqual(result, '<p>this is a paragraph.</p>')

    def test_header(self):
        result = markdown_to_html('# this is a header')
        self.assertEqual(result, '<h1>this is a header</h1>')

    def test_figure_without_title_and_caption(self):
        result = markdown_to_html('![Alt text](/path/to/img.jpg)') 
        self.assertEqual(result, """<figure>
    <img alt="Alt text" src="/path/to/img.jpg" title="" />
    <figcaption></figcaption>
</figure>""")

    def test_figure_with_title_but_without_caption(self):
        result = markdown_to_html('![Alt text](/path/to/img.jpg "Optional title")') 
        self.assertEqual(result, u"""<figure>
    <img alt="Alt text" src="/path/to/img.jpg" title="Optional title" />
    <figcaption></figcaption>
</figure>""")

    def test_figure_with_title_and_caption(self):
        result = markdown_to_html('![Alt text](/path/to/img.jpg "Optional title" (\'Optional figcaption\'))') 
        print result
        self.assertEqual(result, u"""<figure>
    <img alt="Alt text" src="/path/to/img.jpg" title="Optional title" />
    <figcaption>Optional figcaption</figcaption>
</figure>""")

    def test_blockquote_with_footer_and_cite_content_and_title(self):
        result = markdown_to_html('> some content("some footer" ["cite content" "cite title"])')
        self.assertEqual(result, u"""<blockquote>
    <p>some content</p>
    <footer>some footer in <cite title="cite title">cite content</cite></footer>
</blockquote>""")

    def test_code_block(self):
        result = markdown_to_html("""``` python
def sum(a, b):
    return a + b
```""")
        self.assertEqual(result, u"""<pre class="brush: python">
def sum(a, b):
    return a + b
</pre>""")

    def test_anchor_has_target_blank(self):
        result= markdown_to_html('[content](http://url "title")')
        self.assertEqual(result, '<p><a href="http://url" title="title" target="_blank">content</a></p>')

if __name__ == '__main__':
    unittest.main()