from django.core.management.base import BaseCommand, CommandError

from calls.models import PhoneCall, Employee

import csv, datetime

import pytz


class Command(BaseCommand):
    help = 'Load data'

    def handle(self, *args, **options):
        with open("data/employees_parks.csv") as csvfile:
            employee_reader = csv.DictReader(csvfile)

            for row in employee_reader:
                employee = Employee()
                employee.name = row['Name']
                employee.business_title = row['business_title']
                employee.department = row['department/org_chart']
                employee.extension = row['extension']
                employee.save()

        with open('data/calls_parks.csv') as csvfile:
            call_reader = csv.DictReader(csvfile)

            for row in call_reader:
                call = PhoneCall()
                call.extension = row['extension']
                call.phone_number = row['phone_number']
                
                # Create the call
                call_date, call_time = row['call_date_time'].split(' ')
                call_month, call_day, call_year = call_date.split('/')
                call_year = "20%s" % call_year
                call_hour, call_minute = call_time.split(":")

                call.call_date_time = datetime.datetime(
                    int(call_year), int(call_month), int(call_day),
                    int(call_hour), int(call_minute),
                    tzinfo = pytz.timezone('US/Eastern')
                )

                call.duration_in_seconds = row['duration_in_seconds']
                call.inbound = True if row['inbound'] == "TRUE" else False
                call.save()

