from __future__ import annotations
from abc import ABC, abstractmethod

from commands.abstractcommands import AbstractCommand
from services.employee_service import EmployeeService


class GetEmployeesList(AbstractCommand):
    def __init__(self):
        self.employeeService = EmployeeService()

    def execute(self):
        return self.employeeService.getEmployees()


if __name__ == "__main__":
    emp= GetEmployeesList()
    emp.execute()


