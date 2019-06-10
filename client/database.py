from cloudant.client import Cloudant


class CloudantDBClientException(BaseException):
    pass


class CloudantDBClient:
    """
    A simple Python wrapper for connecting to and searching in Cloudant DBs
    """

    def __init__(self):
        self.connection = None
        self.db = None
        self.design_doc = None
        self.index = None
        self.query_params = None
        self.response = None

    def connect(self, db_url, username=None, auth_token=None):
        """
        Connect to the Cloudant DB
        """
        if isinstance(self.connection, Cloudant):
            return
        self.connection = Cloudant(
            cloudant_user=username,
            auth_token=auth_token,
            url=db_url,
            connect=True,
            use_basic_auth=True  # FYI: Well, it took time to figure out, how to skip Cookie auth and user&passwd :)
        )

    def disconnect(self):
        """
        Disconnect from the Cloudant DB
        """
        if isinstance(self.connection, Cloudant):
            self.connection.disconnect()

    def get_db(self, db_name):
        """
        Gets the current DB, if connected.
        """
        if not isinstance(self.connection, Cloudant):
            raise CloudantDBClientException('Not connected to any DB! Use "connect()" first!')
        self.db = self.connection[db_name]

    def _get_design_doc(self, ddoc_id):
        """
        Gets the current DesignDocument, if DB was set.
        """
        if not self.db.exists():
            raise CloudantDBClientException('Not connected to any DB')
        self.design_doc = self.db.get_design_document(ddoc_id)
        if not self.design_doc:
            raise CloudantDBClientException('DesignDocument "{}" was not found!'.format(ddoc_id))

    def _get_index(self, index_name):
        """
        Gets the current index, if DesignDocument was set.
        """
        if not self.design_doc:
            raise CloudantDBClientException('No DesignDocument was selected! Use "_get_design_doc" first!')
        self.index = self.design_doc.get_index(index_name)
        if not self.index:
            raise CloudantDBClientException(
                'Index "{}" was not found! DesignDocument: "{}"'.format(index_name,
                                                                        self.design_doc['_id'])
            )

    # TODO: define query parameters, Lucene syntax
    def build_query(self, query_params):
        """
        Builds a Lucene query, based on incoming parameters

        :param query_params dict: contains all parameters, in min-max value range
        :return:
        """
        return

    def search(self, ddoc_id, index_name, query_params, sort):
        """
        Checks if the defined ddoc and index are exist, and runs the query on the index.

        :param ddoc_id: DesignDocument Id, which contains the index
        :param index_name: Index name, which used in search
        :param query_params: Lucene query in raw string
        :param sort: one or more field name in string or in list of strings
        :return: Query-matched documents
        """
        self._get_design_doc(ddoc_id=ddoc_id)
        self._get_index(index_name=index_name)

        result = self.db.get_search_result(
            ddoc_id=self.design_doc['_id'],
            index_name=index_name,
            query=query_params,
            sort=sort
        )
        return result
