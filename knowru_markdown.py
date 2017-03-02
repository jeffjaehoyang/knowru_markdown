from markdown import markdown

def markdown_to_html(user_given_text):
    html = markdown(user_given_text)

    if html.startswith('<p><img'):
	html = html.replace('<p><img','<figure>\n    <img').replace('</p>','\n</figure>\n')
    
    return html

