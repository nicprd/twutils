from scipy.stats.mstats import gmean

def tag2words(word,model):
    """
    utility for decomposing hastags given a word model
    """

    exists = lambda x : x in model.keys()
    
    paths = [[word]]

    if exists(word): 
        return paths
    
    for i,x in enumerate(word):    
        head = word[:-i]
        tail = word[-i:]
                                        
        if exists(head):       
            paths += [ [head] + i for i in  tag2words(tail,model)]
        elif exists(tail):
            paths += [ [tail] + i for i in  tag2words(head,model)]
            
    return paths[1:] if len(paths) > 1  else paths

def most_probable_combo(words,wordc):
    """
    Replace taglist by the more probable combination of words
    """
    #we dont want 0 use words and we prefer short number of words
    order = [-gmean([wordc[i] for i in w])/(len(w)**2) for w in words]

    return " ".join(words[np.argsort(order)[0]])

if __name__ == "__main__":

    import sys 
    model = {
            "hola" : 1,
            "amigo": 1,
            "fiesta": 1,
            }

    print(most_probable_combo(tag2words(sys.argv[1],model)))
