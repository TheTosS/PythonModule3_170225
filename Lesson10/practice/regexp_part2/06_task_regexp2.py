# Найти все URL-адреса в строке, которые начинаются с http:// или https://
# и за которыми следует последовательность непробельных символов.
import re

text = "Сайты: http://example.com и https://www.another.org/page"
pattern = re.compile(r"https?://\S+")

result = re.findall(pattern, text)
print(result)
