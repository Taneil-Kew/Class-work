
f = open("1-bluemarble_west.jpg", "rb")
g = open("thebluecopy.jpg", "wb")

# while True:
#     buf = f.read(1024)
#     if len(buf) == 0:
#          break
#     g.write(buf)
buf = f.read(1024)

g.write(buf)

f.close()
g.close()
#
# import urllib.request
# myfile = open("python2.html", "w")
# def retrieve_page(url):
#     """ Retrieve the contents of a web page.
#         The contents is converted to a string before returning it.
#     """
#     my_socket = urllib.request.urlopen(url)
#     dta = my_socket.read()
#     dta = str(dta)
#     my_socket.close()
#     return dta
#
# the_text = retrieve_page("http://python.org")
# print(the_text)
# myfile = open("python.html", "w")
# myfile.write(the_text)