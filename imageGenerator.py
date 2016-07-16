import os
import random
import numpy
from py_bing_search import PyBingImageSearch
import urllib

def weighted_choice(dict):
    if dict is None:
        return
    sum = 0
    for _,v in dict.iteritems():
        sum += v
    tags,probs = [],[]
    for k,v in dict.iteritems():
        tags.append(k)
        probs.append(float(v)/float(sum))
    weighted_tags = numpy.random.choice(tags,15,probs)
    everything = []
    for el in weighted_tags:
        if not os.path.exists("static/Images/"+ el):
            os.makedirs("static/Images/"+ el)
            bing_image = PyBingImageSearch('6b82m95vx1BHbgcc9PU+Ra3dyS2mJAsvnQwbCha1bi4', el)
            first_ten_results = bing_image.search(limit=15, format='json')  # 1-50
            i = 0
            for e in first_ten_results:
                link = e.media_url
                try:
                    urllib.urlretrieve(link, "static/Images/" + el +"/" + str(i) + ".jpg")
                except IOError:
                    pass
                i += 1
                print i
        paths = os.listdir("static/Images/"+ el)
        full_paths = ["Images/"+ el +"/"+ path for path in paths]
        everything += full_paths
    return [random.choice(everything) for _ in xrange(20 )]
