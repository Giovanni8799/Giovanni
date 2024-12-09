from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import (
    register_nurse_view, thank_you_view, admin_search_view, 
    export_nurses_excel_view, cost_calculator_view,
    admin_calendar_view, admin_calendar_events,
    admin_add_shift_view, admin_nurse_detail_view,
    admin_shift_detail_view, admin_shift_delete_view,
    admin_contracts_view, admin_contracts_add_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_nurse_view, name='register_nurse'),
    path('thank_you/', thank_you_view, name='thank_you'),
    path('admin_search/', admin_search_view, name='admin_search'),
    path('export_nurses_excel/', export_nurses_excel_view, name='export_nurses_excel'),
    path('admin_cost_calculator/', cost_calculator_view, name='admin_cost_calculator'),
    path('admin_calendar/', admin_calendar_view, name='admin_calendar'),
    path('admin_calendar_events/', admin_calendar_events, name='admin_calendar_events'),
    path('admin_add_shift/', admin_add_shift_view, name='admin_add_shift'),
    path('admin_nurse_detail/<int:nurse_id>/', admin_nurse_detail_view, name='admin_nurse_detail'),
    path('admin_shift_detail/<int:shift_id>/', admin_shift_detail_view, name='admin_shift_detail'),
    path('admin_shift_delete/<int:shift_id>/', admin_shift_delete_view, name='admin_shift_delete'),

    # Avtal
    path('admin_contracts/', admin_contracts_view, name='admin_contracts'),
    path('admin_contracts_add/', admin_contracts_add_view, name='admin_contracts_add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
