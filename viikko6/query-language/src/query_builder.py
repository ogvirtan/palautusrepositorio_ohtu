from matchers import And, Or, Not, All, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher

    def plays_in(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))
    
    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))
    
    def one_of(self, *builders):
        matchers = [qb.build() for qb in builders]
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self._matcher