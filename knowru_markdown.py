from markdown import markdown

def markdown_to_html(user_given_text):
    html = markdown(user_given_text)
    return html
