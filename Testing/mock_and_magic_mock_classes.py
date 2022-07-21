class SomeClass():

    def hidden_method(self):
	    return 0

    def public_method(self, x):
    	return self.hidden_method() + x