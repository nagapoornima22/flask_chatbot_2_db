import json
from flask import Flask, Blueprint
from app.main.commands.employee.getEmployeesCommand import GetEmployeesList

employees_blueprint = Blueprint('employees', __name__)


@employees_blueprint.route("/employees/", methods=["GET"])
def getEmployees():
    res = GetEmployeesList()
    result = res.execute()
    jsdata = json.dumps(result)
    return jsdata

