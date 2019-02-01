c.ServerProxy.servers = {
    'drill': {
        #this probably won't work because it wants a terminal
        #Also, there is no port option?
        'command': ['/home/jovyan/apache-drill-1.15.0/bin/drill-embedded'],
        'timeout': 120,
        'absolute_url': True, 
        'launcher_entry': {
            'enabled': True,
            #'icon_path': '',
            'title': 'Apache Drill',
        },
    },
}
