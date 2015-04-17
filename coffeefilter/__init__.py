from javax.servlet import Filter
from clamp import clamp_base

ClampedBase = clamp_base("")

# Given the above, the linkable Java class name is coffeefilter.CoffeeFilter

class CoffeeFilter(ClampedBase, Filter):
    def init(self, filterConfig):
        raise NotImplementedError("implement!")

    def doFilter(self, request, response, chain):
        raise NotImplementedError("implement!")
        
    def destroy(self):
        raise NotImplementedError("implement!")
