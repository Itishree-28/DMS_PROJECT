from django.db import models
from core.models import BaseModel
from users.models import UserDetails


class Department(BaseModel):
    dept_name = models.CharField(max_length=255)
    head = models.ForeignKey(
        "Employee", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        db_table = "department"

    def __str__(self):
        return self.dept_name


class Employee(BaseModel):
    employee_code = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    email_address = models.CharField(max_length=255)
    doj = models.DateField()
    phone_number = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=255)

    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    pan = models.CharField(max_length=255)
    aadhar = models.CharField(max_length=255)
    uan = models.CharField(max_length=255)
    bank_account_id = models.CharField(max_length=255)
    profile_photo_path = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.full_name


class Attendance(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    total_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    work_type = models.CharField(
        max_length=50,
        choices=[("Remote", "Remote"), ("Onsite", "Onsite"), ("Field", "Field"), ("Other", "Other")]
    )
    remarks = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "attendance"


class LeaveRequest(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(
        max_length=50,
        choices=[
            ("Casual", "Casual"),
            ("Sick", "Sick"),
            ("Earned", "Earned"),
            ("Unpaid", "Unpaid"),
            ("Other", "Other")
        ]
    )
    start_date = models.DateField()
    end_date = models.DateField()
    total_days = models.IntegerField()

    status = models.CharField(max_length=255)
    approver = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, related_name="approver"
    )
    reason = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "leave_requests"


class Payroll(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.IntegerField()
    year = models.IntegerField()
    gross_salary = models.DecimalField(max_digits=12, decimal_places=2)
    deductions = models.DecimalField(max_digits=12, decimal_places=2)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2)

    payment_status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("Paid", "Paid"),
            ("Failed", "Failed"),
            ("PartiallyPaid", "PartiallyPaid")
        ]
    )
    payment_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "payroll"


class PerformanceReview(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_period_start = models.DateField()
    review_period_end = models.DateField()
    reviewed_by = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, related_name="reviewer"
    )

    kpi = models.TextField()
    attendance_score = models.DecimalField(max_digits=5, decimal_places=2)
    behaviour_score = models.DecimalField(max_digits=5, decimal_places=2)
    overall_score = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "performance_review"
