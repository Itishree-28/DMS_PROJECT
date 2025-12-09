from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DepartmentViewSet, EmployeeViewSet, AttendanceViewSet,
    LeaveRequestViewSet, PayrollViewSet, PerformanceReviewViewSet
)

router = DefaultRouter()
router.register("department", DepartmentViewSet)
router.register("employee", EmployeeViewSet)
router.register("attendance", AttendanceViewSet)
router.register("leave", LeaveRequestViewSet)
router.register("payroll", PayrollViewSet)
router.register("performance", PerformanceReviewViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
