Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@guanmche 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


This repository has been archived by the owner. It is now read-only.
sgalal
/
cs61a
Archived
3
101
Code
Pull requests
Actions
Security
Insights
cs61a/Labs/lab11/buffer.py /
@sgalal
sgalal Emplace protogenic lab 11 and 12
Latest commit 5969adb on Aug 10, 2019
 History
 1 contributor
50 lines (46 sloc)  1.48 KB
  
class Buffer(object):
    """A Buffer provides a way of accessing a sequence one at a time.
    Its constructor takes a sequence, called the "source".
    The Buffer supplies elements from source one at a time through its remove_front()
    method. In addition, Buffer provides a current() method to look at the
    next item to be supplied, without moving past it.
    >>> buf = Buffer(['(', '+', 15, 12, ')'])
    >>> buf.remove_front()
    '('
    >>> buf.remove_front()
    '+'
    >>> buf.current()
    15
    >>> buf.remove_front()
    15
    >>> buf.current()
    12
    >>> buf.remove_front()
    12
    >>> buf.remove_front()
    ')'
    >>> buf.remove_front()  # returns None
    """
    def __init__(self, source):
        self.index = 0
        self.source = source

    def remove_front(self):
        """Remove the next item from self and return it. If self has
        exhausted its source, returns None."""
        current = self.current()
        self.index += 1
        return current

    def current(self):
        """Return the current element, or None if none exists."""
        if self.index >= len(self.source):
            return None
        else:
            return self.source[self.index]

    def expect(self, expected):
        actual = self.remove_front()
        if expected != actual:
            raise SyntaxError("expected '{}' but got '{}'".format(expected, actual))
        else:
            return actual

    def __str__(self):
        return str(self.source[self.index:])
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
