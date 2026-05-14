from rest_framework import viewsets

from .models import (
    Department,
    Employee,
    EmployeeProfile,
    Project
)

from .serializers import (
    DepartmentSerializer,
    EmployeeSerializer,
    EmployeeProfileSerializer,
    ProjectSerializer
)


class DepartmentViewSet(
    viewsets.ModelViewSet
):

    queryset = Department.objects.all()

    serializer_class = DepartmentSerializer


class EmployeeViewSet(
    viewsets.ModelViewSet
):

    queryset = Employee.objects.all()

    serializer_class = EmployeeSerializer


class EmployeeProfileViewSet(
    viewsets.ModelViewSet
):

    queryset = EmployeeProfile.objects.all()

    serializer_class = EmployeeProfileSerializer


class ProjectViewSet(
    viewsets.ModelViewSet
):

    queryset = Project.objects.all()

    serializer_class = ProjectSerializer