from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.permissions import HasModulePermission

from .models import (
    Department, Employee, Attendance, LeaveRequest,
    Payroll, PerformanceReview
)
from .serializers import (
    DepartmentSerializer, EmployeeSerializer, AttendanceSerializer,
    LeaveRequestSerializer, PayrollSerializer, PerformanceReviewSerializer
)


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "HRMS"
    submodule = "Organization"


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "HRMS"
    submodule = "Employee"


class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "HRMS"
    submodule = "Attendance"


class LeaveRequestViewSet(ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "HRMS"
    submodule = "Leave"


class PayrollViewSet(ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "HRMS"
    submodule = "Payroll"


class PerformanceReviewViewSet(ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "HRMS"
    submodule = "Performance"
