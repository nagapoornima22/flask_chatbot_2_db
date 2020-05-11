import json


class EmployeeDTO():
    def __init__(self, item):
        # print(item)
        if (item != None):
            self.id = item[0]
            self.name = item[1]
            self.salary = item[4]
            self.age = item[2]
            self.address = item[3]

        #if (item != None):
            #self.id = item['id'] if item['id'] != None else item[0]
            #self.employee_name = item['employee_name'] if item['employee_name'] != None else item[1]
            #self.employee_salary = item['employee_salary'] if item['employee_salary'] != None else item[2]
            #self.employee_age = item['employee_age'] if item['employee_age'] != None else item[3]
    #def getItem(item):
        #if (item != None):
            #dict = {"id": item['id'], "employee_name": item['employee_name'],
                    #"employee_salary": item['employee_salary'], "employee_age": item['employee_age'],
                    #"profile_image": item['profile_image']}

        #return dict
    def getItem(item):
        if (item != None):
            dict = {"id": item[0], "name": item[1],"age": item[2], "address": item[3],"salary": item[4]}

        return dict


class DomainDTO():
    def __init__(self, item):
        print(item)
        if (item != None):
            self.name = item[0]
            self.id = item[1]
            self.domain = item[2]

    def getItem(item):
        if (item != None):
            dict = {'id': item[0], "name": item[1], "domain": item[2]}
        return dict
