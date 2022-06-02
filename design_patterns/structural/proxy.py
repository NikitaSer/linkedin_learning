import time


class Producer:
    """Define the 'resource-intensive' object to instantiate!"""
    def produce(self):
        print("Producer is working")

    def meet(self):
        print("Producer has time to meet you now")


class Proxy:
    """Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""
    def __init__(self):
        self.occupied = False
        self.producer = None

    def produce(self):
        """Check if producer is available"""
        print("Artist checking if Producer is available")

        if self.occupied is False:
            # If the producer is available, create a producer object
            self.producer = Producer()
            time.sleep(2)

            # Make the producer to meet guest
            self.producer.meet()

        else:
            # Otherwise do not instantiate the producer
            time.sleep(2)
            print("Producer is busy")


# Instantiate the proxy
p = Proxy()

# Make the proxy: Artist produce until the producer is available
p.produce()

# Change the state to occupied
p.occupied = True

# Make the producer produce
p.produce()
