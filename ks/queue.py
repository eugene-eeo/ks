"""
    ks.queue
    ~~~~~~~~
    Implements a lazy-eager hybrid queue that is
    internally based on a stream.
"""


from ks.stream import Stream


class Queue(Stream):
    """
    A queue is a FIFO stream that is modifiable
    by inserting (enqueuing) and poping (dequing).
    """

    def pop(self):
        """
        Removes an item from the queue.
        """
        for item in self:
            return item
        raise ValueError

    def push(self, datum):
        """
        Enqueues an item into the queue.
        """
        self.extend((datum,))
