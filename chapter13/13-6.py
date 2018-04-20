f = open("earth.jpg", "rb")
g = open("thecopy.jpg", "wb")

while True:
    buf = f.read(1024)
    if len(buf) == 0:
         break
    g.write(buf)


f.close()
g.close()

import urllib.request

def retrieve_page(url):
    """ Retrieve the contents of a web page.
        The contents is converted to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = my_socket.read()
    dta = str(dta)
    my_socket.close()
    return dta

the_text = retrieve_page("http://python.org")
print(the_text)
myfile = open("python.html", "w")
myfile.write(the_text)