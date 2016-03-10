class Rational:
    def __init__(self,num,denom):
        self.numerator = num
        self.denominator = denom

    def __repr__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    def simplify(self):
        if "." not in str(self.numerator) and "." not in str(self.denominator):
            a = min(self.numerator, self.denominator)
            for n in range (a, 1, -1):
                if self.denominator%a == 0 and self.numerator%a == 0:
                    self.numerator /= n
                    self.denominator /=n
                    break
        else:
            return "Not a valid input!"


print "." not in str(3.14)

#Test simplify
r = Rational(3.14,3.14)
a = r.simplify()
print a