from py_bing_search import PyBingImageSearch
import urllib

bing_image = PyBingImageSearch('6b82m95vx1BHbgcc9PU+Ra3dyS2mJAsvnQwbCha1bi4', "best tv show quotes")
first_fifty_results = bing_image.search(limit=50, format='json') #1-50

i = 0
for el in first_fifty_results:
    link = el.media_url
    try:
        urllib.urlretrieve(link, "static/Images/tv series/"+str(i) +".jpg")
    except IOError:
        pass
    i+=1
    print i