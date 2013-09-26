#!/usr/bin/env python


# Create an abstract class for observers.


class Observer(object):
    """
    Abstract class to respond to changes in the subject.
    """

    def update(self):
        """
        Update observer state.
        """
        raise NotImplementedError("update() is not implemented.")


# Create a concrete class for the subject.


class Subject(object):
    """
    Maintains a list of observers and notifies
    them of state changes.
    """

    def __init__(self):
        """
        Initialize a list of observers.
        """
        self.state = 0
        self.observers = []

    def getState(self):
        """
        Return the state of the subject.
        """
        return self.state

    def setState(self, state):
        """
        Set the state of the subject and notify observers.
        """
        self.state = state
        self.notifyObservers()

    def attach(self, observer):
        """
        Add an observer to the list of observers
        to be notified of state changes.
        """
        self.observers.append(observer)

    def notifyObservers(self):
        """
        Iterate through observers and call the
        update() method on each one.
        """
        for observer in self.observers:
            observer.update()


# Create concrete classes for observers.


class BinaryObserver(Observer):
    """
    Observer that prints subject state in binary.
    """

    def __init__(self, subject):
        """
        Keep a reference to the subject.
        """
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print bin(self.subject.getState())


class OctalObserver(Observer):
    """
    Observer that prints subject state in octal.
    """

    def __init__(self, subject):
        """
        Keep a reference to the subject.
        """
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print oct(self.subject.getState())


class HexadecimalObserver(Observer):
    """
    Observer that prints subject state in hexadecimal.
    """

    def __init__(self, subject):
        """
        Keep a reference to the subject.
        """
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print hex(self.subject.getState())


def main():
    """
    Test the observer pattern implementation.
    """
    subject = Subject()
    BinaryObserver(subject)
    OctalObserver(subject)
    HexadecimalObserver(subject)

    print "First state change."
    subject.setState(10)

    print "Second state change."
    subject.setState(168438)


if __name__ == "__main__":
    main()
