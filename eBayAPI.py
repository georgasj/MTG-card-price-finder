# eBay API program for API github check here for APIs https://github.com/timotheus/ebaysdk-python/wiki/Finding-API-Class

"""

# SANDBOX API, app name on ebay: find mtg card prices

from ebaysdk.finding import Connection as Finding

api = Finding(domain='svcs.sandbox.ebay.com', appid="IoannisG-findmtgc-SBX-45833820b-b3ad37f7", config_file=None)
response = api.execute('findItemsAdvanced', {'keywords': 'chair'}, {'limit': 10})

print(response.dict())

"""

# PRODUCTION API

from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from pprint import pprint

try:
    api = Finding(appid='IoannisG-findmtgc-PRD-208e4a4c1-390d1366', config_file="/Users/ygeorgas/mtgchk/ebay.yaml")
    response = api.execute('findItemsAdvanced', {
        'keywords': 'Chrome Mox',
        'paginationInput': {
            'entriesPerPage': '3',
            'pageNumber': '1'
        }
    })

    # Use the pprint function to print the response in a human readable format
    pprint(response.dict())

except ConnectionError as e:
    print(e)
    print(e.response.dict())

"""
import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

try:
    api = Connection(appid='IoannisG-findmtgc-PRD-208e4a4c1-390d1366', config_file="/Users/ygeorgas/mtgchk/ebay.yaml")
    response = api.execute('findItemsAdvanced', {
        'keywords': 'nike shoes',
        'paginationInput': {
            'entriesPerPage': '3',
            'pageNumber': '1'
        }
    })

    assert(response.reply.ack == 'Success')
    assert(type(response.reply.timestamp) == datetime.datetime)
    assert(type(response.reply.searchResult.item) == list)

    item = response.reply.searchResult.item[0]
    assert(type(item.listingInfo.endTime) == datetime.datetime)
    assert(type(response.dict()) == dict)

except ConnectionError as e:
    print(e)
    print(e.response.dict())
"""
