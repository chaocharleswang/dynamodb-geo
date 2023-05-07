
"""
Purpose: A signle point of entry for all the table and dynamodb client configuration
"""
from s2sphere import RegionCoverer as S2RegionCoverer


class GeoDataManagerConfiguration:

    MERGE_THRESHOLD = 2  # still not clear

    geohashIndexName = "geohash-index"  # name of the LSI

    def __init__(self, dynamoDBClient: 'dynamoDB client', tableName: str, gSIName: str, gSIHashKeyName: str,
                 gSIRangeKeyName: str):
        self.dynamoDBClient = dynamoDBClient  # dynamodb client taken from aws sdk
        self.tableName = tableName
        self.S2RegionCoverer = S2RegionCoverer  # this is form the s2 library
        self.hashKeyAttributeName = "hashKey"
        self.rangeKeyAttributeName = "rangeKey"
        self.geohashAttributeName = "geohash"
        self.locationAttributeName = "location"
        self.hashKeyLength = 2
        self.locationPointType = "Point"  # for now only point is supported
        self.gSIName = gSIName  # Global secondary index name
        self.gSIHashKeyName = gSIHashKeyName  # Global secondary index hash key name
        self.gSIRangeKeyName = gSIRangeKeyName  # Global secondary index range key name
