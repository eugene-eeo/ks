"""
    prudent.queue
    ~~~~~~~~~~~~~

    Implements a lazy FIFO queue that is internally
    based on a stream.
"""


from prudent.stream import Stream


class Queue(Stream):
    """
    A queue is a FIFO stream that is modifiable
    by inserting (enqueuing) and poping (dequing),
    but only from the end.
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
