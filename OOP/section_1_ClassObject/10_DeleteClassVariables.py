class HtmlDocument:
    extension = 'html'
    version = '5'

# 1.
delattr(HtmlDocument, 'version')

# 2. 
del HtmlDocument.version