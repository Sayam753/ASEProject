from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe

from users.models import UserProfile
from subscriptions.models import Subscription, Plan
from subscriptions.states import SubscriptionState as State
from subscriptions.plans import SubscriptionPlan as Plans

stripe.api_key = settings.STRIPE_PRIVATE_KEY

def subscribe(request):
    user = request.user
    if user.is_authenticated:
        subscription = Subscription.objects.filter(user=user).order_by('-id').first()
        if not subscription:
            return render(request, 'subscriptions/new_subscription.html')
        elif subscription.status == State.DEACTIVATED:
            return render(request, 'subscriptions/renew_subscription.html')
        elif subscription and subscription.status == State.ACTIVE:
            return redirect(reverse('home'))
    else:
        return redirect(reverse('login'))


@csrf_exempt
def trial(request):
    session = stripe.checkout.Session.create(
                    customer_email = request.user.email,
                    payment_method_types = ['card'],
                    line_items = [{
                        #price id from Stripe Dashboard
                        'price' : 'price_1H60pwI24oCI0OTByU54LFUB',
                        'quantity' : 1,
                    }],
                    mode = 'payment',
                    success_url = request.build_absolute_uri(reverse('home')) + '?session_id={CHECKOUT_SESSION_ID}',
                    cancel_url = request.build_absolute_uri(reverse('subscribe')),
    )
    return JsonResponse({
        'session_id' : session.id,
        'strip_public_key' : settings.STRIPE_PUBLIC_KEY
    })


@csrf_exempt
def basic(request):
    session = stripe.checkout.Session.create(
                    customer_email = request.user.email,
                    payment_method_types = ['card'],
                    line_items = [{
                        #price id from Stripe Dashboard
                        'price' : 'price_1H60viI24oCI0OTBOf07Jt9e',
                        'quantity' : 1,
                    }],
                    mode = 'payment',
                    success_url = request.build_absolute_uri(reverse('home')) + '?session_id={CHECKOUT_SESSION_ID}',
                    cancel_url = request.build_absolute_uri(reverse('subscribe')),
    )
    return JsonResponse({
        'session_id' : session.id,
        'strip_public_key' : settings.STRIPE_PUBLIC_KEY
    })


@csrf_exempt
def premium(request):
    session = stripe.checkout.Session.create(
                    customer_email = request.user.email,
                    payment_method_types = ['card'],
                    line_items = [{
                        #price id from Stripe Dashboard
                        'price' : 'price_1H61H2I24oCI0OTBSaW6awEL',
                        'quantity' : 1,
                    }],
                    mode = 'payment',
                    success_url = request.build_absolute_uri(reverse('home')) + '?session_id={CHECKOUT_SESSION_ID}',
                    cancel_url = request.build_absolute_uri(reverse('subscribe')),
    )
    return JsonResponse({
        'session_id' : session.id,
        'strip_public_key' : settings.STRIPE_PUBLIC_KEY
    })


@csrf_exempt
def diamond(request):
    session = stripe.checkout.Session.create(
                    customer_email = request.user.email,
                    payment_method_types = ['card'],
                    line_items = [{
                        #price id from Stripe Dashboard
                        'price' : 'price_1H61OOI24oCI0OTBmW5Dy2sw',
                        'quantity' : 1,
                    }],
                    mode = 'payment',
                    success_url = request.build_absolute_uri(reverse('home')) + '?session_id={CHECKOUT_SESSION_ID}',
                    cancel_url = request.build_absolute_uri(reverse('subscribe')),
    )
    return JsonResponse({
        'session_id' : session.id,
        'strip_public_key' : settings.STRIPE_PUBLIC_KEY
    })



@csrf_exempt
def stripe_webhook(request):
    #test
    # endpoint_secret = 'whsec_0bFVho9jv8RwpCNQ9oC0AINEKGZDO18O'
    #deployed
    endpoint_secret = 'whsec_lhBWqqPoYUghCa4ecsjqyrbZWsKMFCQE'
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
    )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    print(event['type'])
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session['customer_email']
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        price_id = line_items['data'][0]['price']['id']

        #price id is of Trial
        if price_id == 'price_1H60pwI24oCI0OTByU54LFUB':
            current_plan, created = Plan.objects.get_or_create(plan=Plans.TRIAL)
            if created:
                current_plan.save()

        #price_id is of Basic
        elif price_id == 'price_1H60viI24oCI0OTBOf07Jt9e':
            current_plan, created = Plan.objects.get_or_create(plan=Plans.BASIC)
            if created:
                current_plan.save()

        #price_id is of Premium
        elif price_id == 'price_1H61H2I24oCI0OTBSaW6awEL':
            current_plan, created = Plan.objects.get_or_create(plan=Plans.PREMIUM)
            if created:
                current_plan.save()

        #price_id is of Diamond
        elif price_id == 'price_1H61OOI24oCI0OTBmW5Dy2sw':
            current_plan, created = Plan.objects.get_or_create(plan=Plans.DIAMOND)
            if created:
                current_plan.save()

        user_profile = UserProfile.objects.get(email=customer_email)
        user_profile.subscribed = True
        user_profile.save()

        previous_subscription = Subscription.objects.filter(user=user_profile).order_by('-id').first()
        if previous_subscription:
            previous_subscription.status = State.DEACTIVATED
            previous_subscription.save()
        new_subscription = Subscription.objects.create(
                            user=user_profile,
                            plan=current_plan,
                            status=State.ACTIVE)
        new_subscription.save()

    return HttpResponse(status=200)
