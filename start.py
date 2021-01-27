import webbrowser

address = "http://www.pythonchallenge.com/pc/def/0.html"
retval = 2**38
new_address = address.replace("0", str(retval))
webbrowser.open(new_address)

# Go to map.py