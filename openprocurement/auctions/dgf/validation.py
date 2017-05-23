# -*- coding: utf-8 -*-

def validate_change_value_minimalStep_guarantee(request):
    if request.authenticated_role == 'Administrator' and request.context.status == 'active.tendering':
        if request.context.value.amount < request.validated['data'].get('value').get('amount'):
            request.errors.add('body', 'data', 'Only reducing value is allowed')
            request.errors.status = 403
        if request.context.minimalStep.amount < request.validated['data'].get('minimalStep').get('amount'):
            request.errors.add('body', 'data', 'Only reducing minimalStep is allowed')
            request.errors.status = 403
        if request.context.guarantee and request.context.guarantee.amount < request.validated['data'].get('guarantee').get('amount'):
            request.errors.add('body', 'data', 'Only reducing guarantee is allowed')
            request.errors.status = 403
