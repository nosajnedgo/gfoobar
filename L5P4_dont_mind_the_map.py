# Challenge: http://pastebin.com/WD5XwqHX

from collections import OrderedDict
from itertools import combinations
from itertools import product

class Route():
    def __init__(self, subway):
        self.subway = subway
        self.reverse = self._reverse(subway)
        self.reductPairs = self._initReductPairs(self.reverse)
        self.lastLevel = self.reductPairs.copy()
    
    def exists(self):
        """Return whether a common reduction path exists"""
        stations, foundReduct = set(range(len(self.subway))), True
        while len(stations) > 1 and foundReduct:
            foundReduct = False
            for rpair, ops in self._genReductPairs():
                if len(rpair.intersection(stations)) > 1:
                    stations = self._apply(ops, stations)
                    foundReduct = True
                    break
        return (len(stations) == 1)

    def _initReductPairs(self, reverse):
        """Add the primary reduction pairs to the list"""
        rs = OrderedDict()
        for station, inlets in enumerate(reverse):
            for track, sources in enumerate(inlets):
                for pair in combinations(sources, 2):
                    rs[frozenset(pair)] = [track]
        return rs
        
    def _genReductPairs(self):
        """Generate a list of valid reduction pairs as needed"""
        for i in self.reductPairs.iteritems():
            yield i
        while len(self.lastLevel):
            nextLevel = OrderedDict()
            for rpair, ops in self.lastLevel.iteritems():
                self._addNextLevel(rpair, ops, nextLevel)
            self.reductPairs.update(nextLevel)
            self.lastLevel = nextLevel
            for i in self.lastLevel.iteritems():
                yield i

    def _addNextLevel(self, rpair, ops, nextLevel):
        """Trace reduction pairs back one level to a new reduction pair"""
        tracks = range(len(self.subway[0]))
        s1, s2 = rpair
        for t in tracks:
            for pair in product(self.reverse[s1][t], self.reverse[s2][t]):
                pair = frozenset(pair)
                if pair not in self.reductPairs:
                    nextLevel[pair] = [t] + ops[:]

    def _reverse(self, subway):
        """Create an index of what lines/stations come into a station"""
        tracks, stations = range(len(subway[0])), range(len(subway))
        reverse = [[[] for i in tracks] for i in stations]
        for station, outlet in enumerate(subway):
            for track, dest in enumerate(outlet):
                reverse[dest][track].append(station)
        return reverse

    def _apply(self, ops, stations):
        """Apply the given operations to the set of stations"""
        for op in ops:            
            result = set()
            for s in stations:
                result.add(self.subway[s][op])
            stations = result.copy()
        return result
        

def closeStation(closed, original):
    """Change the subway structure for closing the given station"""
    subway = []
    for i in original: subway.append(i[:])
    for station, outlets in enumerate(subway):
        for track, dest in enumerate(outlets):
            if dest == closed:
                if subway[closed][track] == closed:
                    subway[station][track] = station
                else:
                    subway[station][track] = subway[closed][track]
    del subway[closed]
    for station, outlets in enumerate(subway):
        for track, dest in enumerate(outlets):
            if dest > closed:
                subway[station][track] = dest - 1
    return subway


def answer(subway): 
    route = Route(subway)
    if route.exists():
        return -1
    for station in range(len(subway)):
        closedSub = closeStation(station, subway)
        route = Route(closedSub)
        if route.exists():
            return station
    return -2
