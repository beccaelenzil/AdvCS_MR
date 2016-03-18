
#
# Problem Set 1, Problem 1: Dates
#
# Name:
#
import time

class Date():
    """ a user-defined data structure that
        stores and manipulates dates
    """


    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year

    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
        as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def tomorrow(self):
        leapYear = self.isLeapYear()
        fdays = 0
        if leapYear:
            fdays = 29
        else:
            fdays = 28
        dim = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
        monthDays = dim[self.month]
        if self.month == 12 and self.day == 31:
            self.month = 1
            self.day = 1
            self.year += 1
        elif self.day == monthDays:
            self.month += 1
            self.day = 1
        else:
            self.day += 1

    def yesterday(self):
        leapYear = self.isLeapYear()
        fdays = 0
        if leapYear:
            fdays = 29
        else:
            fdays = 28
        dim = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
        monthDays = dim[self.month]
        if self.month == 1 and self.day == 1:
            self.year -= 1
            self.month = 12
            self.day = 31
        elif self.day == 1:
            self.month -=1
            self.day = monthDays
        else:
            self.day -= 1


    def addNDays(self, d2):
        days = d2
        for i in range(0, days):
            self.tomorrow()

    def subNDays(self, d2):
        days = d2
        for i in range (0, days):
            self.yesterday()

    def isBefore(self, d):
        """
        return true if self if before d
        """

        if d.year > self.year:
            return True
        #elif d.month > self.month and d.year == self.year:
        #    return False
        elif d.year == self.year:
            if d.month == self.month:
                if d.day > self.day:
                    return True
                else:
                    return False
            elif d.month > self.month:
                return True
            else:
                return False
        else:
            return False

    def isAfter(self, d):
        """
        return true if self if after d
        """
        if d.year < self.year:
            return True
        #elif d.month < self.month and d.year == self.year:
        #    return False

        elif d.year == self.year:
            if d.month == self.month:
                if d.day < self.day:
                    return True
                else:
                    return False
            elif d.month < self.month:
                return True
            else:
                return False
        else:
            return False

<<<<<<< Updated upstream
    def diff (self, d2):

        # make a copy of the two days
        refDay = self.copy()
        day2 = d2.copy()

        # True if refDay is before day2
        beforeBool = refDay.isBefore(day2)

        # True if refDay is after day2
        afterBool = refDay.isAfter(day2)

        counterInt = 0
        keepCounting = True

        if beforeBool:
            counterInt = 0
            keepCounting = True
            while refDay.isBefore(day2):#keepCounting:
                #if refDay.isBefore(day2):
                counterInt += 1
                refDay.tomorrow()
                #else:
                #    #keepCounting = False
                #   counterInt -= 1
            return counterInt
        elif afterBool:
            counterInt = 0
=======
<<<<<<< HEAD
    def diff(self, d2):
        beforeBool = self.isBefore(d2)
        afterBool = self.isAfter(d2)
        counterInt = 0
        print "counterInt"
        #t1 = time.clock()
        if beforeBool:
            counterInt = 0
            keepCounting = True
            while (keepCounting):
                if self.isBefore(d2):
                    self.yesterday()
                    counterInt += 1

                else:
                    keepCounting = False
                    counterInt -= 1
        elif afterBool:
            counterInt = 0
            keepCounting = True
            while (keepCounting):
                if self.isAfter(d2):
                    self.tomorrow()
                    counterInt += 1
                    print counterInt
                else:
                    keepCounting = False
                    counterInt -= 1

        #else:
        #    counterInt = 0
        t2 = time.clock()
       ## print t2 - t1
        return counterInt







=======
    def diff (self, d2):

        # make a copy of the two days
        refDay = self.copy()
        day2 = d2.copy()

        # True if refDay is before day2
        beforeBool = refDay.isBefore(day2)

        # True if refDay is after day2
        afterBool = refDay.isAfter(day2)

        counterInt = 0
        keepCounting = True

        if beforeBool:
            counterInt = 0
            keepCounting = True
            while refDay.isBefore(day2):#keepCounting:
                #if refDay.isBefore(day2):
                counterInt += 1
                refDay.tomorrow()
                #else:
                #    #keepCounting = False
                #   counterInt -= 1
            return counterInt
        elif afterBool:
            counterInt = 0
>>>>>>> Stashed changes
            #keepCounting = True
            while refDay.isAfter(day2):#keepCounting:
                #if refDay.isAfter(day2):
                refDay.yesterday()
                counterInt -= 1
               #else:
                    #keepCounting = False
                    #counterInt -= 1
            return counterInt

        #return counterInt

"""
<<<<<<< Updated upstream
=======
>>>>>>> origin/master
>>>>>>> Stashed changes
my = Date(3,15,2012)
my2 = Date(4,14,2015)
my3 = Date(3,14,2016).diff(Date(3,14,2017))
my4 = Date(3,14,2016).diff(Date(3,14,2116))
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
my5 = Date(3,14,2013)
print my5.diff(my2)
#print my2
=======
>>>>>>> Stashed changes
my5 = Date(3,14,2012)
"""
firstDay = Date(3,15,2012)
secondDay = Date(4,15,2013)

# your isBefore and isAfter methods weren't working correctly, so I made changes to these and added a docstring explaining what they do
# your diff is still off by one day, I'll leave that for you to fix!

print secondDay.diff(firstDay)
print firstDay.diff(secondDay)


<<<<<<< Updated upstream
=======
>>>>>>> origin/master
>>>>>>> Stashed changes
