# A silly example of a certain variation of the Builder
# Pattern, as described by Josh Bloch.


class Pizza(object):

    class PizzaBuilder(object):
        """
        The PizzaBuilder inner class returns itself from
        all methods except build(), which returns a
        new instance of Pizza built with the selected options.
        """
        def __init__(self):
            self.extra_cheese = False
            self.garlic = False

        def add_garlic(self):
            self.garlic = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True
            return self

        def build(self):
            return Pizza(self)

    def __init__(self, builder):
        """
        The constructor for the class takes an instance
        of its builder as a parameter.
        """
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese


def main():
    print "Building a pizza..."

    # We can do this nice option chaining.
    pizza = Pizza.PizzaBuilder().add_garlic().add_extra_cheese().build()

    if pizza.garlic:
        print "The pizza has garlic."
    if pizza.extra_cheese:
        print "The pizza has extra cheese."

if __name__ == "__main__":
    main()
