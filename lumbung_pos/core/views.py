from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def dashboard(request): 
    return render(request, 'dashboard.html')
def notifications(request): 
    return render(request, 'notifications.html')
def products(request): 
    return render(request, 'products.html')
def add_product(request): 
    return render(request, 'add_product.html')
def categories(request): 
    return render(request, 'categories.html')
def inventory_planner(request): 
    return render(request, 'inventory_planner.html')
def stock_movement(request): 
    return render(request, 'stock_movement.html')
def sales_insights(request): 
    return render(request, 'sales_insights.html')
def pricing_strategies(request): 
    return render(request, 'pricing_strategies.html')
def store_comparison(request): 
    return render(request, 'store_comparison.html')
def request_items(request): 
    return render(request, 'request_items.html')
def shipments_tracking(request): 
    return render(request, 'shipments_tracking.html')
def delivery_status(request): 
    return render(request, 'delivery_status.html')
def reports(request): 
    return render(request, 'reports.html')
def market_trends(request): 
    return render(request, 'market_trends.html')
def custom_reports(request): 
    return render(request, 'custom_reports.html')
def competitor_analysis(request): 
    return render(request, 'competitor_analysis.html')
def vendor_management(request): 
    return render(request, 'vendor_management.html')
def business_health(request): 
    return render(request, 'business_health.html')
def trend_tracker(request): 
    return render(request, 'trend_tracker.html')
def performance_metrics(request): 
    return render(request, 'performance_metrics.html')
def technical_diagnostics(request): 
    return render(request, 'technical_diagnostics.html')
def team_management(request): 
    return render(request, 'team_management.html')
def activity_log(request): 
    return render(request, 'activity_log.html')
def workforce_planner(request): 
    return render(request, 'workforce_planner.html')
def system_tutorials(request): 
    return render(request, 'system_tutorials.html')
def staff_training(request): 
    return render(request, 'staff_training.html')
def feedback_tracker(request): 
    return render(request, 'feedback_tracker.html')
def loyalty_program(request): 
    return render(request, 'loyalty_program.html')
def user_guide(request): 
    return render(request, 'user_guide.html')
def support_center(request): 
    return render(request, 'support_center.html')
def settings(request): 
    return render(request, 'settings.html')
def incoming_tasks(request): 
    return render(request, 'incoming_tasks.html')
def system_notifications(request): 
    return render(request, 'system_notifications.html')
def task_scheduler(request): 
    return render(request, 'task_scheduler.html')
def promotion_calendar(request): 
    return render(request, 'promotion_calendar.html')
def profile(request): 
    return render(request, 'profile.html')
def form_logout(request): 
    return render(request, 'form_logout.html')

@user_passes_test(lambda u: u.is_superuser)
@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
