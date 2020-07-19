from enum import IntEnum


class SubscriptionPlan(IntEnum):
    #10 searches
    TRIAL = 2
    #60 searches
    BASIC = 199
    #300 searches
    PREMIUM = 399
    #700
    DIAMOND = 799

    @classmethod
    def choices(cls, do=None):
        state = []
        if do:
            for s in cls:
                if s.value in do:
                    state.append(s)
        else:
            state = [s for s in cls]
        return tuple((s.value, "{}".format(SubscriptionPlan(s.value).name)) for s in state)

    @classmethod
    def plan_name(cls, plan):
        for s in cls:
            if s.value==plan:
                return s.name
