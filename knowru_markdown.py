from markdown import markdown
import re

def markdown_to_html(user_given_text):
    if user_given_text.startswith('>'):
        match_obj = re.match(r'> (.*)\("(.*)" \["(.*)" "(.*)"]\)', user_given_text)

        html = u"""<blockquote>
    <p>{}</p>
    <footer>{} in <cite title="{}">{}</cite></footer>
</blockquote>
""".format(match_obj.group(1), match_obj.group(2), match_obj.group(4), match_obj.group(3))

    elif user_given_text.startswith("```"): 
        match_obj = re.match(r'``` (.*)(\s)(\S*)(.*)(\s)(\s)(.*)(\s)```', user_given_text)

        html = u"""<pre class="brush: {}">
{}{}
{}{}
</pre>
""".format(match_obj.group(1), match_obj.group(3), match_obj.group(4), match_obj.group(6), match_obj.group(7))


    elif user_given_text.startswith("!["):
        match_obj = re.match(r'!\[(.*)\]\((\S*)( "([^\']*)")?( \'(.*)\')?\)', user_given_text)
        html = u"""<figure>
    <img alt="{}" src="{}" title="{}" />
    <figcaption>{}</figcaption>
</figure>
""".format(
    match_obj.group(1)
    , match_obj.group(2)
    , match_obj.group(4) if match_obj.group(4) else unicode()
    , match_obj.group(6) if match_obj.group(6) else unicode()
)
    
    elif user_given_text.startswith("["):
        match_obj = re.match(r'\[(.*)\]\((.*) "(.*)"\)', user_given_text)
        html = u"""<p><a href="{}" title="{}" target="_blank">{}</a></p>""".format(match_obj.group(2), match_obj.group(3), match_obj.group(1))


    else:
        html = markdown(user_given_text)
    return unicode(html)


