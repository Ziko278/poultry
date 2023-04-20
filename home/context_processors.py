from admin_dashboard.models import SiteSetupModel


def layout_variable(request):
    site_info = SiteSetupModel.objects.first()

    return {
            'site_info': site_info,
        }



