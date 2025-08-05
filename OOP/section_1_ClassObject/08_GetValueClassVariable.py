class HtmlDocument:
    extension = 'html'
    version = '5'

extension = getattr(HtmlDocument, 'extension')
version = getattr(HtmlDocument, 'version')

print(extension)
print(version)

media_type = getattr(HtmlDocument, 'media_type', 'text/html')
print(media_type)