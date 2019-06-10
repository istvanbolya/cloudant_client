import unittest

from database import CloudantDBClient, CloudantDBClientException


class TestCloudantDBClient(unittest.TestCase):

    def setUp(self):
        self.client = CloudantDBClient()
        self.client.connect('https://mikerhodes.cloudant.com')

    def tearDown(self):
        self.client.disconnect()

    def test_get_db_missing(self):
        db_missing = 'nodbhere'
        with self.assertRaises(CloudantDBClientException) as context:
            self.client.get_db(db_missing)
        self.assertTrue('Cannot get DB' in str(context.exception))

    def test_get_db_exists(self):
        db_exists = 'airportdb'
        self.client.get_db(db_exists)
        self.assertTrue(self.client.db.exists())

    # TODO: Well, it seems that even the Ddoc doesn't exist, the "_get" creates that, with empty values.
    #       So this test unfortunatelly passes. Dunno, how to check properly?
    def test_get_design_doc_missing(self):
        self.client.get_db('airportdb')

        design_doc_missing = '_design/noviewhere'
        self.client._get_design_doc(design_doc_missing)
        self.assertEqual(self.client.design_doc['_id'], design_doc_missing)

    def test_get_design_doc_exists(self):
        self.client.get_db('airportdb')

        design_doc_exists = '_design/view1'
        self.client._get_design_doc(design_doc_exists)
        self.assertEqual(self.client.design_doc['_id'], design_doc_exists)

    def test_get_index_missing(self):
        self.client.get_db('airportdb')
        design_doc_name = '_design/view1'
        self.client._get_design_doc(design_doc_name)

        index_missing = 'noindex'
        with self.assertRaises(CloudantDBClientException) as context:
            self.client._get_index(index_missing)
        self.assertTrue('was not found' in str(context.exception))

    def test_get_index_exists(self):
        self.client.get_db('airportdb')
        design_doc_name = '_design/view1'
        self.client._get_design_doc(design_doc_name)

        index_exists = 'geo'
        self.client._get_index(index_exists)
        self.assertTrue(isinstance(self.client.index, dict))


if __name__ == '__main__':
    unittest.main()
