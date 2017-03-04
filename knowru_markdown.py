from markdown import markdown

def markdown_to_html(user_given_text):


    if user_given_text[0] == '>':
        
        text_length = len(user_given_text)
        p_content = ''
        footer = ''
        cite_content = ''
        cite_title = ''

        for x in range(2, text_length):
            if user_given_text[x] == '(':
                x = x + 2
                break
            else: 
                p_content += user_given_text[x]
        
        for x in range(x, text_length):
            if user_given_text[x] == '"':
                x = x + 4
                break
            else:
                footer += user_given_text[x]

        for x in range(x, text_length):
            if  user_given_text[x] == '"':
                x = x + 3
                break
            else:
                cite_content += user_given_text[x]

        for x in range(x, text_length):
            if  user_given_text[x] == '"':
                break
            else:
                cite_title += user_given_text[x]
                

        user_given_text = '<blockquote>\n' + '    <p>' + p_content \
            + '</p>\n' + '    <footer>' + footer + ' in ' + '<cite title=' \
            + '"' + cite_title + '">' + cite_content \
            + '</cite></footer>\n' + '</blockquote>'

        html = markdown(user_given_text)


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