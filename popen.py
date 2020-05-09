import subprocess
wind_syunkan_max = 20
wind_heikin_10min = 30
send_msg='最大瞬間風速= {0:.2f}m/s \n10分平均風速= {1:.2f} m/s'.format( wind_syunkan_max,wind_heikin_10min)

#subprocess.Popen('/usr/bin/python3 /home/harumiki/python/sendmail_wind_alert.py' )
command = ['python3' , '/home/harumiki/python/sendmail_wind_alert.py' , send_msg]
subprocess.Popen(command )
#subprocess.Popen('/usr/bin/python3' )
