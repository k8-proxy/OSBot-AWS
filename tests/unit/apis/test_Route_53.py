from gw_bot.helpers.Test_Helper import Test_Helper
from osbot_aws.apis.Route_53 import Route_53


class test_ACM(Test_Helper):

    def setUp(self):
        super().setUp()
        self.route_53 = Route_53()

    def test__ctor__(self):
        assert type(self.route_53).__name__ == 'Route_53'

    def test_record_set_upsert(self):
        name                = 'gw-proxy.com.'
        record_type         = 'A'
        dns_name            = 'd-noho75bpih.execute-api.eu-west-1.amazonaws.com.'
        hosted_zone_id      = '/hostedzone/ZMHOWKWA1ZN69'
        alias_hosted_zone_id = 'ZLY8HYME6SFDD'
        self.result = self.route_53.record_set_upsert(name, record_type, dns_name,hosted_zone_id,alias_hosted_zone_id)

    def test_record_sets(self):
        self.result = self.route_53.record_sets()
        
    def test_domains(self):
        self.result = self.route_53.domains(index_by='DomainName')

    def test_hosted_zones(self):
        self.result = self.route_53.hosted_zones(index_by='Name')