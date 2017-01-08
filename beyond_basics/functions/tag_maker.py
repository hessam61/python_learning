def tag(name, **attributes):
	result = '<' + name
	for key, value in attributes.items():
		result += ' {k}="{v}"'.format(k=key, v=str(value))
	result += '>'
	return result

image = tag('img', src="monet.jpg", alt="Sunrise by Monet", border=1)
print(image)