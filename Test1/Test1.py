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
        keepLoop = True
        i = 1
        while keepLoop == True:
          i += 1
          simpNum = self.numerator / i
          simpDenom =  self.denominator / i
          if ((simpNum/simpDenom) == (self.numerator/self.denominator)):
            keepLoop = False
            self.numerator = simpNum
            self.denominator = simpDenom


#Test simplify
r = Rational(7.0,20.0)
r.simplify()
print r