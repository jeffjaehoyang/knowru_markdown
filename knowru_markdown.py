from markdown import markdown

def markdown_to_html(user_given_text):


	text_length = len(user_given_text)
	p_content = ''
	footer = ''
	cite_content = ''
	cite_title = ''

	if user_given_text[0] == '>':
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
	return html




