from markdown import markdown
import re

def markdown_to_html(user_given_text):


    if user_given_text[0] == '>':
        matchObj = re.match(r'> (.*)\("(.*)" \["(.*)" "(.*)"]\)', user_given_text)

        html = '<blockquote>\n' + '    <p>' + matchObj.group(1) \
            + '</p>\n' + '    <footer>' + matchObj.group(2) + ' in ' + '<cite title=' \
            + '"' + matchObj.group(4) + '">' + matchObj.group(3) \
            + '</cite></footer>\n' + '</blockquote>'
    else:
        figcaption = str()
        if user_given_text.startswith("!["):
            html_split = user_given_text.split(' "')
            if len(html_split) > 2:
                figcaption = html_split[2]
                user_given_text = html_split[0] + ' "' + html_split[1] + ")"

        html = markdown(user_given_text)

        if html.startswith('<p><img'):
            html = html.replace('<p><img','<figure>\n    <img')
            if figcaption:
                figcaption = figcaption.replace('"', '')[:-1]
                html = html.replace('</p>', '\n    <figcaption>{}</figcaption>\n</figure>\n'.format(figcaption))
            else:
                html = html.replace('</p>','\n</figure>\n')
    return unicode(html)