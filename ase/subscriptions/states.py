from enum import IntEnum


class SubscriptionState(IntEnum):
    ACTIVE = 1
    DEACTIVATED = 2

    @classmethod
    def choices(cls, do=None):
        state = []
        if do:
            for s in cls:
                if s.value in do:
                    state.append(s)
        else:
            state = [s for s in cls]
        return tuple((s.value, "{}".format(SubscriptionState(s.value).name)) for s in state)
