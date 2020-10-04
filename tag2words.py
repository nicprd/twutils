
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


if __name__ == "__main__":

    import sys 
    model = {
            "hola" : 1,
            "amigo": 1,
            "fiesta": 1,
            }

    print(tag2words(sys.argv[1],model))
