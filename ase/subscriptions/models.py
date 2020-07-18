from django.db import models
from django.utils import timezone

from users.models import UserProfile
from subscriptions.states import SubscriptionState as State
from subscriptions.plans import SubscriptionPlan as Plans

class Plan(models.Model):
    """
    Plan model has the plan details
    plan is an IntegerField with values equivalent to enums corresponding to plan cost
    """

    plan = models.IntegerField(
        default=Plans.BASIC,
        choices=Plans.choices(),
        unique=True,
        help_text='amount for searches'
    )

    def __str__(self):
        return '{}  {}'.format(Plans.plan_name(self.plan), self.plan)

    @property
    def plan_name(self):
        return Plans.plan_name(self.plan)

    @property
    def plan_amount(self):
        return self.plan

    @property
    def search_limit(self):
        if self.plan == Plans.TRIAL:
            return 10
        elif self.plan == Plans.BASIC:
            return 60
        elif self.plan == Plans.PREMIUM:
            return 300
        elif self.plan == Plans.DIAMOND:
            return 700

class Subscription(models.Model):
    """
    Subscription model has the details of both previous and current subscriptions of a user
    #Field Descriptions
    > subscription.status is an IntegerField with values equvivalent to enums corresponding to the subscription state
        1 = Active ---> current plan is active
        2 = Deactivated  ---> no active plan existing
    > plan is the plan associated with the active subscription
    > searches_completed is the searches completed so far. Decrements by one for every search

    #Method Descriptions
    Every time a subscription is set to active, new row is created in the database
    decrement_searches increases the searc by 1 for every search
    has_searches_left returns a boolean for searches left
    """

    user = models.ForeignKey('users.UserProfile', related_name='user_profile_subscription', on_delete=models.CASCADE)
    plan = models.ForeignKey('subscriptions.Plan', related_name='subscription_plan', on_delete=models.PROTECT, null=True)
    status = models.IntegerField(
        default=State.ACTIVE,
        choices=State.choices(),
        help_text='current subscription status of the user'
    )
    searches_completed = models.IntegerField(default=0, null=False, help_text='searches completed')

    class Meta:
        ordering = ('-searches_completed',)

    def __str__(self):
        return self.user.username

    @property
    def change_to_deactivated(self):
        self.status = State.DEACTIVATED
        self.save()
        return self

    @property
    def decrement_searches(self):
        print('hiiiiiiiiiiii')
        print(self.searches_completed)
        self.searches_completed += 1
        self.save()
        return self

    @property
    def has_searches_left(self):
        return True if self.searches_completed < self.plan.search_limit else False
