""" Sample file to serve as the basis for inspect examples.
"""


def module_level_function(arg1, arg2='default', *args, **kwargs):
    """This function is declared in the module."""
    local_variable = arg1
    return


class A(object):
    """The A class."""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Returns the name of the instance."""
        return self.name


instance_of_a = A('sample_instance')


class B(A):
    """
    This is the B class.
    It is derived from A.(a subclass of A)
    """

    # This method is not part of A
    def do_something(self):
        """Does some work"""
        pass

    def get_name(self):
        """Overrides version from A"""
        return 'B(' + self.name + ')'
