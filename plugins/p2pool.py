from PyQt4.QtGui import *
from PyQt4.QtCore import *
from electrum_gui.qt.util import *
from electrum.util import *
from electrum import Transaction
from electrum.i18n import _
from electrum.plugins import BasePlugin
from electrum.bitcoin import *
from electrum.transaction import parse_redeemScript
import base64
 
class Plugin(BasePlugin):
    def fullname(self): return 'MyriadCoin P2Pool Node List'
 
    def description(self): return _('Returns details of P2Pool Nodes and Mining Information.')
 
    def __init__(self, gui, name):
        BasePlugin.__init__(self, gui, name)
        self._is_available = True
        self.base_unit = "MYR" # Should support multi base units like the rest of Electrum UI
        self.cb = QApplication.clipboard()
        self.inited = None
 
    # Create The Marketplace tab if it does not exist
    def load_wallet(self, wallet):
        self.wallet = wallet
        if(self.inited == None):
            self.gui.main_window.tabs.addTab(self.create_tmp_tab(), _('Mining Pool's (P2Pool)') )
            self.inited = True
 
    # Create the Mining Pools tab that contains buttons for the various
    # features of the plugin
    def create_tmp_tab(self):
        w = QWidget()
 
        grid = QGridLayout()
        grid.setSpacing(8)
        grid.setColumnMinimumWidth(3,300)
        grid.setColumnStretch(5,1)
 
        pool_list = QListWidget()
        pool_list.addItem('asiap2pool.cryptopools.com') 
        pool_list.addItem('usp2pool.cryptopools.com')
        
        grid.addWidget(poollist, 2, 8)
        w.setLayout(grid)
 
        w2 = QWidget()
        vbox = QVBoxLayout()
        vbox.addWidget(w)
        vbox.addStretch(1)
        w2.setLayout(vbox)
 
        return w2
 
