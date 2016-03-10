class Rational:
    def __init__(self,num,denom):
        self.numerator = num
        self.denominator = denom

    def __repr__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    def simplify(self):
        """
        This method should return the rational number in simplest for in place.
        For example, if r = Rational(10,20), after calling r.simplify(), r should be equal to Rational(1,2)
        """


#Test simplify
r = Rational(10,20)
r.simplify()
print r