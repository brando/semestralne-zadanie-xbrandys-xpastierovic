"""Custom topology with 16 nodes and 2 hosts

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )
        switch4 = self.addSwitch( 's4' )
        switch5 = self.addSwitch( 's5' )
        switch6 = self.addSwitch( 's6' )
        switch7 = self.addSwitch( 's7' )
        switch8 = self.addSwitch( 's8' )
        switch9 = self.addSwitch( 's9' )
        switch10 = self.addSwitch( 's10' )
        switch11 = self.addSwitch( 's11' )
        switch12 = self.addSwitch( 's12' )
        switch13 = self.addSwitch( 's13' )
        switch14 = self.addSwitch( 's14' )
        switch15 = self.addSwitch( 's15' )
        switch16 = self.addSwitch( 's16' )

        # Add links
        self.addLink( leftHost, switch1 )
        self.addLink( switch1, switch2 )
        self.addLink( switch2, switch3 )
        self.addLink( switch2, switch4 )
        self.addLink( switch3, switch7 )
        self.addLink( switch3, switch4 )
        self.addLink( switch4, switch6 )
        self.addLink( switch4, switch5 )
        self.addLink( switch7, switch6 )
        self.addLink( switch7, switch8 )
        self.addLink( switch6, switch8 )
        self.addLink( switch6, switch5 )
        self.addLink( switch5, switch9 )
        self.addLink( switch8, switch9 )
        self.addLink( switch8, switch10 )
        self.addLink( switch9, switch13 )
        self.addLink( switch10, switch11 )
        self.addLink( switch10, switch12 )
        self.addLink( switch11, switch12 )
        self.addLink( switch13, switch12 )
        self.addLink( switch13, switch14 )
        self.addLink( switch12, switch15 )
        self.addLink( switch14, switch15 )
        self.addLink( switch15, switch16 )
        self.addLink( switch16, rightHost )


topos = { 'mytopo': ( lambda: MyTopo() ) }