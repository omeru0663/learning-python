def fred(First = "Hello", Second = "Goodbye"):
    return(f"{First} and {Second}") 
  
    
def barney():
    global x 
    x = 1
    while True:
        x = x + 1
        yield x
print(fred(9))

