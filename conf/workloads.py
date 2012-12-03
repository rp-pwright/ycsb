root = '/opt/ycsb'

data = {    #global YSCB properties
    #'recordcount': 500000000,  #SSD
    'recordcount': 50000000,    #RAM
    'fieldcount': 10,
    'fieldlength': 10,
    'fieldnameprefix': 'f',
    'operationcount': 10000000,
    'threadcount': 32,
    'workload': 'com.yahoo.ycsb.workloads.CoreWorkload',
    'exportmeasurementsinterval': 30000,
    #'warmupexecutiontime': 60000,
    'insertretrycount': 1000000,
    'readretrycount': 1000,
    'updateretrycount': 1000,
    'retrydelay': 1,
    #'readallfields': 'false',
    #'writeallfields': 'false',
}

workloads = {
    'A': {
        'name': 'workloada',    #name of the workload to be part of the log files
        'propertyfiles': [ root + '/workloads/workloada' ], #workload properties files
    },
    'B': {
        'name': 'workloadb',
        'propertyfiles': [ root + '/workloads/workloadb' ],
    },
    'C': {
        'name': 'workloadc',
        'propertyfiles': [ root + '/workloads/workloadc' ],
        'properties': {     #additional workload properties, overrides the global ones
            'operationcount': 10000000,
            'maxexecutiontime': 60000,
        },
    },
}
