from client.database import CloudantDBClient

DB_URL = 'https://mikerhodes.cloudant.com'
DB_NAME = 'airportdb'
DESIGN_DOC = '_design/view1'
INDEX = 'geo'


def call_search():
    client = CloudantDBClient()
    client.connect(db_url=DB_URL)

    client.get_db(db_name=DB_NAME)
    # client._get_design_doc(DESIGN_DOC)
    # client._get_index(INDEX)
    results = client.search(ddoc_id=DESIGN_DOC,
                            index_name=INDEX,
                            query_params='lon:[0 TO 15] AND lat:[0 TO 5]',
                            sort=['lat', 'lon'])
    client.disconnect()
    return results


if __name__ == '__main__':
    result = call_search()
    for item in result['rows']:
        print(item)
