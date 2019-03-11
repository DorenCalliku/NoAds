from bs4 import BeautifulSoup as Soup

html = """
<html>
<head>
<title>Test Page</title>
</head>
<body>
<div>test</div>
</html>
"""
soup = Soup(html, features='lxml')

title = soup.find('title')
meta = soup.new_tag('meta')
meta['content'] = "text/html; charset=UTF-8"
meta['http-equiv'] = "Content-Type"
title.insert_after(meta)

print soup
