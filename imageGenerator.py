import os
import random
import numpy

def weighted_choice(dict):

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
        paths = os.listdir(os.path.dirname(os.path.abspath(__file__))+"/static/Images/"+ el)
        full_paths = [os.path.dirname(os.path.abspath(__file__))+"/static/Images/"+ el +"/"+ path for path in paths]
        everything += full_paths

    return [random.choice(everything) for _ in xrange(15)]
