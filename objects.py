'''
Here we have objects that we use
'''

def add_nums(x, y):
    '''
    Adds two numbers together
    
    :param x: a real number
    
    :param y: a real number
           
    :returns: x+y
    '''

class Dog:
    '''
    This is an implementation of a dog. He barks and wags his tail
    '''
    
    def __init___(self):
        pass
        
    def bark(self):
        '''
        Makes the dog bark
        '''
        print 'Woof!'
        
    def wag_tail(self, n_times = 1):
        '''
        Makes the dog wag its tail
        n_times: the number of times the dog wags its tail
        '''
        for i in xrange(n_times):
            print 'wag tail'
