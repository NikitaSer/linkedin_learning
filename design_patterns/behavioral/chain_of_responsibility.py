"""
Opens up various possibilities of processing for a given request.
Decouples the request and its processing.

Problem - many types of processing need to be done depending on the request.

Solution:
abstract handler - which stores a successor which handle the request
if the current handler can't handle it
concrete handlers - check if they can handle the request,
if they can, they handle it and return a true value,
indicating that the request was handled.

Composite pattern is related to Chain of responsibility
"""


class Handler:
    """Abstract Handler"""

    def __init__(self, successor):
        # Define who is the next handler
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)

        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError(
            "Must provide an implementation of the _handle method"
        )


class ConcreteHandler1(Handler):
    """Concrete Handler"""

    def _handle(self, request):
        # Provide a condition for handling
        if 0 < request <= 10:
            print(f"Request {request} handled in handler 1")
            return True


class DefaultHandler(Handler):
    """Default Handler"""

    def _handle(self, request):
        """If there is no handler available"""
        # No condition checking since this is a default handler
        print(f"End of the chain, no handler for the requst={request}")
        return True


class Client:
    def __init__(self):
        """Create handlers and use them in a sequence you want"""
        self.handler = ConcreteHandler1(successor=DefaultHandler(successor=None))

    def delegate(self, requests):
        """Send your requests one at a time"""
        for request in requests:
            self.handler.handle(request)


# Create a client
c = Client()

# Create requests
requests = [2, 5, 30]

# Send the requests
c.delegate(requests)
