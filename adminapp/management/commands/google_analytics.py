import os
from datetime import datetime

from django.core.management.base import BaseCommand
import httplib2
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from analytics_service_object import initialize_service
from oauth2client.file import Storage
from oauth2client import tools
import argparse


client_data = 'client_data.json'

FLOW = flow_from_clientsecrets(
    client_data,
    scope='https://www.googleapis.com/auth/analytics.readonly',
    message='%s is missing' % client_data
)

TOKEN_FILE_NAME = 'credentials.dat'


def prepare_credentials():
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    flags = parser.parse_args()

    storage = Storage(TOKEN_FILE_NAME)
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(FLOW, storage, flags)
    return credentials


def initialize_service():
    http = httplib2.Http()
    credentials = prepare_credentials()
    http = credentials.authorize(http)
    # Build the Analytics Service Object with the authorized http object
    return build('analytics', 'v3', http=http)


def get_accounts_data(service):
    accounts = service.management().accounts().list().execute()
    data = []
    if accounts.get('items'):
        for account in accounts['items']:
            data.append(account['id'])
    return data


# def get_sessions(service, profile_id, start_date, end_date):
#     ids = "ga:" + profile_id
#     metrics = "ga:sessions"
#     data = service.data().ga().get(
#         ids=ids, start_date=start_date, end_date=end_date, metrics=metrics
#     ).execute()
#     return data["totalsForAllResults"][metrics]

not_source_filters = {
    "social": "ga:hasSocialSourceReferral==No",
    "organic": "ga:medium!=organic",
    "direct": "ga:source!=(direct),ga:medium!=(none);ga:medium!=(not set)",
    "email": "ga:medium!=email",
    "referral": "ga:medium!=referral,ga:hasSocialSourceReferral!=No"
}

source_filters = {
    "social": "ga:hasSocialSourceReferral==Yes",
    "organic": "ga:medium==organic",
    "direct": "ga:source==(direct);ga:medium==(none),ga:medium==(not set)",
    "email": "ga:medium==email",
    "referral": "ga:medium==referral;ga:hasSocialSourceReferral==No",
    "other": "%s;%s;%s;%s;%s" % (
        not_source_filters["social"], not_source_filters["organic"],
        not_source_filters["direct"], not_source_filters["email"],
        not_source_filters["referral"])
}


def get_source_sessions(service, profile_id, start_date, end_date, source):
    ids = "ga:" + profile_id
    metrics = "ga:sessions"
    filters = source_filters[source]
    data = service.data().ga().get(
        ids=ids, start_date=start_date, end_date=end_date, metrics=metrics,
        filters=filters).execute()
    return data["totalsForAllResults"][metrics]


class Command(BaseCommand):
    def handle(self, *args, **options):
        service = initialize_service()
        # Получить данные по пользователям
        get_accounts_data(service)

        # Данные c начала года разрезе источников
        profile_id = os.environ['profile']
        today = datetime.date.today()
        start_date = datetime.date(2019, 1, 1)
        end_date = today
        # start_date = end_date + dateutil.relativedelta.relativedelta(months=-1)
        for source in ["social", "organic", "direct", "email", "referral", "other"]:
            print(source, get_source_sessions(
                service, profile_id, start_date, end_date, source))

