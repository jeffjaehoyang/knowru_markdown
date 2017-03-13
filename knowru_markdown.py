from markdown import markdown
import re
import argparse

def markdown_to_html(user_given_text):
    

    user_given_text = re.sub(r'!\[(.*)\]\((.*) "(.*)" \(\'(.*)\'\)\)', 
        r'<figure>\n    <img alt="\g<1>" src="\g<2>" title="\g<3>" />\n    <figcaption>\g<4></figcaption>\n</figure>', 
        user_given_text)

    user_given_text = re.sub(r'!\[(.*)\]\((.*) "(.*)"\)', r'<figure>\n    <img alt="\g<1>" src="\g<2>" title="\g<3>" />\n    <figcaption></figcaption>\n</figure>',
        user_given_text)

    user_given_text = re.sub(r'!\[(.*)\]\((.*)\)', r'<figure>\n    <img alt="\g<1>" src="\g<2>" title="" />\n    <figcaption></figcaption>\n</figure>', 
        user_given_text)

    user_given_text = re.sub(r'> (.*)\("(.*)" \["(.*)" "(.*)"]\)', r'<blockquote>\n    <p>\g<1></p>\n    <footer>\g<2> in <cite title="\g<4>">\g<3></cite></footer>\n</blockquote>',
        user_given_text)

    user_given_text = re.sub(r'```(\s)(\w*)(\n)([^`]*)(\n)```', r'<pre class="brush: \g<2>">\n\g<4>\n</pre>', 
        user_given_text, 
        flags = re.DOTALL)

    user_given_text = re.sub(r'\[(.*)\]\((.*) "(.*)"\)', r'<a href="\g<2>" title="\g<3>" target="_blank">\g<1></a>', 
        user_given_text)


    html = markdown(user_given_text)
    

    return unicode(html)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Knowru Markdown - Convenient tool to convert markdown to html')
    parser.add_argument('-i', '--input_path', type=str, required=True, help='Path to input markdown file')
    parser.add_argument('-o', '--output_path', type=str, required=True, help='Path to output html file')

    args = parser.parse_args()

    input_file_handler = open(args.input_path, 'r')
    markdown_input = input_file_handler.read()
    input_file_handler.close()

    html_output = markdown_to_html(markdown_input)

    output_file_handler = open(args.output_path, 'w')
    output_file_handler.write(html_output)
    output_file_handler.close()