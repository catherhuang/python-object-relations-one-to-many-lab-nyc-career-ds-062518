class Trip:
    _all = []

    def __init__(self, start, destination, driver):
        self._start = start
        self._destination = destination
        self._driver = driver
        Trip.all().append(self)
	    # remember to associate a trip with a driver
    @classmethod
    def all(cls):
        return Trip._all
    @property
    def start (self):
        return self._start
    @property
    def destination (self):
        return self._destination
    @property
    def driver(self):
        return self._driver
