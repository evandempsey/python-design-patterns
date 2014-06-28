# A demonstration of how the Observer Pattern might
# be coded in a more Pythonic way, with __setattr__
# on the subject overridden to update the observers.


class Subject(object):
    """
    Maintains a list of observers and notifies
    them of state changes.
    """
    def __init__(self):
        """
        Initialize a list of observers.
        """
        self.__dict__['state'] = 0
        self.__dict__['observers'] = []

    def __setattr__(self, name, value):
        """
        Override to notify observers of state
        changes when the state is updated.
        """
        self.__dict__[name] = value
        if name == 'state':
            self.notify_observers()

    def register(self, observer):
        """
        Add an observer to the list of observers
        to be notified of state changes.
        """
        if observer not in self.observers:
            self.observers.append(observer)

    def deregister(self, observer):
        """
        Remove an observer.
        """
        self.observers.remove(observer)

    def notify_observers(self):
        """
        Iterate through observers and call the
        update() method on each one.
        """
        for observer in self.observers:
            observer.update()


# Create an abstract base class for and concrete classes for observers.

class Observer(object):
    """
    Abstract class to respond to changes in the subject.
    """
    def update(self):
        """
        Update observer state.
        """
        raise NotImplementedError("update() is not implemented.")


class BinaryObserver(Observer):
    """
    Observer that prints subject state in binary.
    """
    def __init__(self, subject):
        """
        Keep a reference to the subject.
        """
        self.subject = subject
        self.subject.register(self)

    def update(self):
        print bin(self.subject.state)


class OctalObserver(Observer):
    """
    Observer that prints subject state in octal.
    """
    def __init__(self, subject):
        """
        Keep a reference to the subject.
        """
        self.subject = subject
        self.subject.register(self)

    def update(self):
        print oct(self.subject.state)


class HexadecimalObserver(Observer):
    """
    Observer that prints subject state in hexadecimal.
    """
    def __init__(self, subject):
        """
        Keep a reference to the subject.
        """
        self.subject = subject
        self.subject.register(self)

    def update(self):
        print hex(self.subject.state)


def main():
    """
    Test the observer pattern implementation.
    """
    subject = Subject()
    BinaryObserver(subject)
    OctalObserver(subject)
    HexadecimalObserver(subject)

    print "First state change."
    subject.state = 10

    print "Second state change."
    subject.state = 168438


if __name__ == "__main__":
    main()
