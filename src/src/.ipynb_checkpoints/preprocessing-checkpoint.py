from pandas import DataFrame

def get_columns(): 
    return ['duration'
        ,'protocol_type'
        ,'service'
        ,'flag'
        ,'src_bytes'
        ,'dst_bytes'
        ,'land'
        ,'wrong_fragment'
        ,'urgent'
        ,'hot'
        ,'num_failed_logins'
        ,'logged_in'
        ,'num_compromised'
        ,'root_shell'
        ,'su_attempted'
        ,'num_root'
        ,'num_file_creations'
        ,'num_shells'
        ,'num_access_files'
        ,'num_outbound_cmds'
        ,'is_host_login'
        ,'is_guest_login'
        ,'count'
        ,'srv_count'
        ,'serror_rate'
        ,'srv_serror_rate'
        ,'rerror_rate'
        ,'srv_rerror_rate'
        ,'same_srv_rate'
        ,'diff_srv_rate'
        ,'srv_diff_host_rate'
        ,'dst_host_count'
        ,'dst_host_srv_count'
        ,'dst_host_same_srv_rate'
        ,'dst_host_diff_srv_rate'
        ,'dst_host_same_src_port_rate'
        ,'dst_host_srv_diff_host_rate'
        ,'dst_host_serror_rate'
        ,'dst_host_srv_serror_rate'
        ,'dst_host_rerror_rate'
        ,'dst_host_srv_rerror_rate'
        ,'class'
        ,'level']

def add_super_class(df: DataFrame):
    for cell in df:
        class_name = cell['class']
        super_class_name = ''
        match class_name :
            case 'normal':
                super_class_name = 'normal'
            case _ if class_name  in['back', 'land', 'neptune', 'pod', 'smurf', 'teardrop']:
                super_class_name = 'ddos'
            case _ if class_name  in['ipsweep', 'nmap', 'portsweep', 'satan']:
                super_class_name = 'ddos'
            case _ if class_name  in['ftp_write', 'httptunnel', 'guess_passwd', 'mscan', 'ps', 'sqlattack', 'imap', 'multihop', 'snmpgetattack','saint', 'phf', 'spy', 'warezclient', 'warezmaster', 'snmpguess', 'xsnoop', 'sendmail', 'xlock', 'named', 'xterm', 'worm']:
                super_class_name = 'r2l'
            case _ if class_name  in['buffer_overflow', 'loadmodule', 'perl', 'rootkit', 'processtable', 'mailbomb', 'apache2', 'udpstorm']:
                super_class_name = 'ddos'
            case _:
                raise ValueError('Attack class name was unexpected!', class_name )
        
        cell['super_class'] = super_class_name

def add_super_service(df: DataFrame):
    for cell in df:
        service_name = cell['service']
        super_service_name = ''
        match service_name :
            case _ if service_name  in['http', 'http_443', 'http_2784', 'http_8001', 'hostnames', 'gopher', 'whois', 'apache2', 'httptunnel']:
                super_service_name = 'web_services'
            case _ if service_name  in['ftp', 'ftp_data', 'tftp_u', 'uucp', 'uucp_path', 'efs', 'sql_net']:
                super_service_name = 'ftp_data'
            case _ if service_name  in['telnet', 'rej', 'ssh', 'klogin', 'kshell', 'login', 'exec' ,'shell', 'sunrpc']:
                super_service_name = 'remote_access_service'
            case _ if service_name  in['smtp', 'pop_2', 'pop_3', 'imap4', 'IRC', 'aol', 'mtp']:
                super_service_name = 'email'
            case _ if service_name  in['domain', 'domain_u', 'eco_i', 'tim_i', 'time', 'ntp_u', 'ping', 'netbios_ns', 'netbios_dgm', 'netbios_ssn', 'netstat', 'csnet_ns', 'link', 'nnsp', 'nntp']:
                super_service_name = 'network'
            case _ if service_name  in['time', 'tim_u', 'ntp_u', 'daytime']:
                super_service_name = 'time'
            case _ if service_name  in['private', 'red_i', 'snmpgetattack', 'mscan', 'security']:
                super_service_name = 'security'
            case _ if service_name  in['systat', 'echo', 'discard', 'ms', 'saint', 'processtable']:
                super_service_name = 'monitoring_management'
            case _ if service_name  in['auth', 'name', 'finger', 'ldap', 'remote_job', 'rje']:
                super_service_name = 'directory_auth'
            case _ if service_name  in['Z39_50', 'supdup', 'eco_i', 'ecr_i', 'iso_tsap', 'pm_dump']:
                super_service_name = 'legacy'
            case _ if service_name  in['vmnet', 'bgp', 'ctf', 'harvest', 'printer', 'courier', 'X11']:
                super_service_name = 'app_specific'
            case _ if service_name  in['red_i', 'urh_i', 'urp_i', 'vmnet']:
                super_service_name = 'experimental'
            case 'other':
                super_service_name = 'other'
            case _:
                raise ValueError('Service name was unexpected!', service_name )

        cell['super_service'] = super_service_name
