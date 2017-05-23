# -*- coding: utf-8 -*-

def validate_change_value_minimalStep_guarantee(request):
    if request.authenticated_role == 'Administrator' and request.context.status == 'active.tendering':
        new_value = request.validated['data'].get('value').get('amount')
        new_minimalStep = request.validated['data'].get('minimalStep').get('amount')
        if request.context.value.amount <  new_value:
            request.errors.add('body', 'data', 'Only reducing value not more than 50% is allowed')
            request.errors.status = 403
        elif 100 - (new_value * 100 / request.context.value.amount) > 50:
            request.errors.add('body', 'data', 'Only reducing value not more than 50% is allowed')
            request.errors.status = 403
        if request.context.minimalStep.amount < new_minimalStep:
            request.errors.add('body', 'data', 'Only reducing minimalStep is allowed')
            request.errors.status = 403
        if request.context.guarantee and request.context.guarantee.amount < request.validated['data'].get('guarantee').get('amount'):
            request.errors.add('body', 'data', 'Only reducing guarantee is allowed')
            request.errors.status = 403
        if request.errors.status == 403:
            return