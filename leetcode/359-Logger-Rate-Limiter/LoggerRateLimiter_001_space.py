class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log_hash = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        hs = self.log_hash
        if message in hs and timestamp - hs[message] < 10:
            return False
        else:
            hs[message] = timestamp
            return True
                


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
