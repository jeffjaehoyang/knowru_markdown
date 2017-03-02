def markdown_to_html(markdown):
    html = unicode()
    if markdown.startswith('#'):
        html = '<h1>{}</h1>'.format(markdown.replace('#', '').strip())
    else:
        html = '<p>{}</p>'.format(markdown)
    return html
