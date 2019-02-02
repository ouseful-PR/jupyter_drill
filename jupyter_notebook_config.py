c.ServerProxy.servers = {
    'drill': {
        #this probably won't work because it wants a terminal - to run as a daemon, requires zookeeper...
        #Also, there is no port option? Or can we prefix start command with an env var to specify the port?
        'command': ['/home/jovyan/apache-drill-1.15.0/bin/drill-embedded'],
        'timeout': 120,
        'absolute_url': True, 
        'port':8047,
        'launcher_entry': {
            'enabled': True,
            #'icon_path': '',
            'title': 'Apache Drill',
        },
    },
}
