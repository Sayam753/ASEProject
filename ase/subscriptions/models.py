from django.db import models
from django.utils import timezone

from users.models import UserProfile
from subscriptions.states import SubscriptionState as State


class Subscription(models.Model):
    """
    Subscription model has the details of both previous and current subscriptions of a user
    #Field Descriptions
    > subscription.status is an IntegerField with values equvivalent to enums corresponding to the subscription state
        1 = Trail Active
        2 = Trial Ended
        3 = Active
        4 = Deactivated
    > trial_limit is the default number of searches available in trial period
    > search_limit is the seaches allowed for user in active subscription period
    > searches_completed is the searches completed so far. Decrements by one for every search

    #Method Descriptions
    Every time a subscription is set to active, new row is created in the database
    decrement_searches increases the searc by 1 for every search
    has_searches_left returns a boolean for searches left
    """

    user = models.ForeignKey('users.UserProfile', related_name='user_profile_subscription', on_delete=models.CASCADE)
    status = models.IntegerField(
        default=State.ACTIVE,
        choices=State.choices(),
        help_text='current subscription status of the user'
    )
    trial_limit = models.IntegerField(default=5, null=True, help_text='default search limit for trials')
    search_limit = models.IntegerField(default=0, null=False, help_text='search limit for the subscription')
    searches_completed = models.IntegerField(default=0, null=False, help_text='searches completed')

    class Meta:
        ordering = ('-searches_completed',)

    def __str__(self):
        return user

    @property
    def change_to_active(self, searches):
        new_subscription = Subscription.create(
            user=self.user,
            status=State.ACTIVE,
            search_limit=searches,
            trial_limit=None
        )
        new_subscription.save()
        self.status = State.TRIAL_ENDED if self.status == State.TRIAL_ACTIVE else self.status
        self.save()
        return new_subscription

    @property
    def change_to_trial_ended(self):
        self.status = State.TRIAL_ENDED
        self.save()
        return self

    @property
    def change_to_deactivated(self):
        self.status = State.DEACTIVATED
        self.save()
        return self

    @property
    def decrement_searches(self):
        self.searches_completed += 1
        self.save()
        return self

    @property
    def has_searches_left(self):
        return True if self.searches_completed < (self.trial_limit or self.search_limit) else False
