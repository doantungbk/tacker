#from keystoneclient.auth.identity import v2
#from keystoneclient import session
#from ceilometerclient import client


#auth=v2.Password(auth_url="hosturl:5000/v2.0/", username="admin", password="pass", tenant_id="123456")
#sess = session.Session(auth=auth, verify=False)
#token=auth.get_token(sess)



#cclient =client.get_client(2,ceilometer_url="hosturl:8777/",token=token,verify=False)
#cclient.alarms.create()

# Requirement for AMOD here:
# Something related to alarm should be expressed here:
# two ways: 1 - call alarm from Heat API             2 - call alarm from Ceilometer API
# If alarms trigger then log


from oslo_config import cfg
from tacker.common import log
from tacker.openstack.common import log as logging
from tacker.vm.monitor_drivers import abstract_driver
from tacker.i18n import _LW

# Alarms processes: create, receive, and process.

LOG = logging.getLogger(__name__)
OPTS = [
    cfg.StrOpt('period', default='60',
               help=_('period time)),
    cfg.StrOpt('evaluation_period', default='1',
               help=_('evaluation period')),
    cfg.StrOpt('threshold', default='70',
               help=_('threshold'))
]
cfg.CONF.register_opts(OPTS, 'monitor_amod')

class VNFMonitoringAlarm(abstract_driver.VNFMonitorAbstractDriver):  # Here abstract_driver is used

    def get_type(self):
        return 'alarm_listener for ceilometer'
    def get_name(self):
        return 'alarm_listener for ceilometer'
    def get_description(self):
        return 'Tacker alarm-based monitoring driver for VNF using Ceilometer'
    def monitor_url(self, plugin, context, device):
        LOG.debug(_('monitor_url %s'), device)
        return device.get('monitor_url', '')
    @log.log
    def monitor_call(self, device, kwargs):


    @log.log
    def create_alarm(self, plugin, device):

    @log.log
    def get_alarm(self, plugin, device):

    @log.log
    def process_alarm(self, plugin, device):




# Create new webhook here?

















































