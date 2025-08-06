import requests, time, sys, os

def animated(text):
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.1)

def animate(text):
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)

os.system("clear")
animated("\n\n\n\t\tTools is loading...")
time.sleep(2)
os.system("clear")
animated("\n\n\n\t\t\033[1;32mWelcome to our tools!")
time.sleep(2)
os.system("clear")

logo = '''
\033[1;31m
        ######  ####### #     # ### #       
        #     # #       #     #  #  #       
        #     # #       #     #  #  #       
        #     # #####   #     #  #  #       
        #     # #        #   #   #  #       
        #     # #         # #    #  #       
        ######  #######    #    ### #######
'''
info = '''
\033[1;32m ===============================================\033[1;36m
    AUTHOR   : Abdul Jabbar 
    Git Hub  : https://github.com/jsjabbar0
    Facebook : https://www.facebook.com/abdul.jabbar.267611
    Coder    : Jabbar 
\033[1;32m ===============================================           
'''
animate(logo)
animate(info)

animated("\n\t\033[1;32m★ IP Information + Live Location ★\n")
ip = input("\nEnter Target IP: ")

try:
    response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
    data = response.json()

    if data['status'] == 'success':
        lat = data['lat']
        lon = data['lon']
        maps_link = f"https://www.google.com/maps?q={lat},{lon}"

        print(f"\n\033[1;35mStatus   : {data['status']}")
        print(f"Country  : {data['country']}")
        print(f"Region   : {data['regionName']}")
        print(f"City     : {data['city']}")
        print(f"ISP      : {data['isp']}")
        print(f"Timezone : {data['timezone']}")
        print(f"IP       : {data['query']}")
        print(f"Latitude : {lat}")
        print(f"Longitude: {lon}")
        print(f"\033[1;34m[+] Live Location (Map): {maps_link}")
    else:
        print(f"\n\033[1;31m[!] Error: {data['message']}")
except Exception as e:
    print(f"\n\033[1;31m[!] Failed to get information: {e}")