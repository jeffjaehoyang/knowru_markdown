import unittest
import subprocess
import tempfile
import os
import shutil

class KnowruMarkdownIntegrationTestTestCase(unittest.TestCase):
    def setUp(self):
    	self.temp_dir = tempfile.mkdtemp()
    	self.input_file_path = os.path.join(self.temp_dir, 'input.markdown')
    	self.output_file_path = os.path.join(self.temp_dir, 'output.html')
        input_file_handler = open(self.input_file_path, 'w')
        input_file_handler.write("""# Title

Paragraph

![Alt](http://url "Title" ('Figure Caption'))

# Another title

1. Ordered list

2. Ordered list
""")
        input_file_handler.close()

    def test_support_input_and_output_file_paths(self):
        return_code = subprocess.call("python knowru_markdown.py -i {} -o {}".format(self.input_file_path, self.output_file_path), shell=True)

        self.assertEqual(return_code, 0)
        self.assertTrue(os.path.exists(self.output_file_path))

        output_file_handler = open(self.output_file_path, 'r')
        output_file_content = output_file_handler.read()
        self.assertEqual(output_file_content, """<h1>Title</h1>
<p>Paragraph</p>
<figure>
    <img alt="Alt" src="http://url" title="Title" />
    <figcaption>Figure Caption</figcaption>
</figure>\n
<h1>Another title</h1>
<ol>
<li>
<p>Ordered list</p>
</li>
<li>
<p>Ordered list</p>
</li>
</ol>""")
        output_file_handler.close()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

if __name__ == '__main__':
    unittest.main()


