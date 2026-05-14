from rest_framework import serializers
from datetime import date
import re

from .models import (
    Department,
    Employee,
    EmployeeProfile,
    Project
)


class DepartmentSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Department
        fields = '__all__'

    def validate_name(self, value):

        if len(value) < 3:
            raise serializers.ValidationError(
                "Department name too short"
            )

        return value


class ProjectSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Project
        fields = '__all__'

    def validate_deadline(self, value):

        if value < date.today():
            raise serializers.ValidationError(
                "Deadline cannot be in the past"
            )

        return value


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    project_count = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = [
            'name',
            'email',
            'salary',
            'joining_date',
            'department',
            'projects',
            'project_count',
            'id'
        ]

    def get_project_count(self, obj):
        return obj.projects.count()

    # Name validation
    def validate_name(self, value):

        if len(value) < 3:
            raise serializers.ValidationError(
                "Name must be at least 3 characters"
            )

        return value

    # Salary validation
    def validate_salary(self, value):

        if value < 10000:
            raise serializers.ValidationError(
                "Salary must be at least 10000"
            )

        return value

    # Joining date validation
    def validate_joining_date(self, value):

        if value > date.today():
            raise serializers.ValidationError(
                "Joining date cannot be future date"
            )

        return value


class EmployeeProfileSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = EmployeeProfile
        fields = '__all__'

    # Phone number validation
    def validate_phone_number(self, value):

        if not re.fullmatch(r'^[6-9]\d{9}$', value):

            raise serializers.ValidationError(
                "Enter valid 10 digit phone number"
            )

        return value

    # Emergency contact validation
    def validate_emergency_contact(
        self,
        value
    ):

        if not re.fullmatch(
            r'^[6-9]\d{9}$',
            value
        ):

            raise serializers.ValidationError(
                "Invalid emergency contact"
            )

        return value