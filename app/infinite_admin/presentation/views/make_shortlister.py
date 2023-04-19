from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.views import View
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from shortlist.models import ShortList


User = get_user_model()


class MakeShortlisterReviewerView(View):

    model = User
    context_object_name = 'staff'

    def get(self, request, **kwargs):
        user_id = self.kwargs.get('pk')
        user = get_object_or_404(User, pk=user_id)
        if not user:
            error_message = _(
                'user not found.')
            messages.add_message(
                self.request, messages.ERROR, error_message)
            return redirect(reverse_lazy('accounts:dashboard'))
        shortlisters_group, created = Group.objects.get_or_create(
            name='shortlisters')
        content_type = ContentType.objects.get_for_model(ShortList)
        permission, created = Permission.objects.get_or_create(
            codename='can_view_shortlist',
            name='Can view shortlist',
            content_type=content_type)
        shortlisters_group.permissions.add(permission)
        user.groups.add(shortlisters_group)
        user.is_reviewer = True
        user.save()
        success_message = _('Great, staff member ') + \
            str(user) + _(' can now view shortlists.')
        messages.add_message(
            self.request, messages.SUCCESS, success_message)
        return redirect(reverse_lazy('basic_admin:staff'))
