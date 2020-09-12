import selenium.webdriver
import time
import os

# Custom modules
import callmaker
import xmlgen
import messagemaker

group_url = 'ROBLOX_GROUP_URL'

account = 'YOUR_TWILIO_ACCOUNT_SID'
token = 'YOUR_TWILIO_ACCOUNT_TOKEN'

call_make = False
source = 'YOUR_FREE_TRIAL_PHONE_NUMBER_IN_TWILIO'
destination = 'DESTINATION_NUMBER'

url_xml = 'XML_WEB_SERVER_LOCATION'
time_wait = 60

########################################################################
# DO NOT CHANGE ANYTHING ELSE BELOW THIS COMMENT HERE PLEASE #
########################################################################

options = selenium.webdriver.ChromeOptions()
options.headless = True
prefs = {'profile.default_content_setting_values': {'images': 2, 'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                    'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                                                    'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                    'media_stream_mic': 2, 'media_stream_camera': 2,
                                                    'protocol_handlers': 2, 'ppapi_broker': 2, 'automatic_downloads': 2,
                                                    'midi_sysex': 2, 'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                    'metro_switch_to_desktop': 2, 'protected_media_identifier': 2,
                                                    'app_banner': 2, 'site_engagement': 2, 'durable_storage': 2}}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = selenium.webdriver.Chrome(options=options)

driver.get(group_url)

if not os.path.isfile("messages"):
    f = open("messages", "w")
    f.close()

while 3 > 2:
    time.sleep(2)

    print("====================================================")
    perfil = driver.find_element_by_xpath('//*[@id="group-container"]/div/div/div/div[3]/div/div[1]/div[2]/div[2]/div[1]/a')
    print()
    print(perfil.text)

    texto = driver.find_element_by_xpath('//*[@id="group-container"]/div/div/div/div[3]/div/div[1]/div[2]/div[2]/div[2]')
    print()
    print(texto.text)

    data = driver.find_element_by_xpath('//*[@id="group-container"]/div/div/div/div[3]/div/div[1]/div[2]/div[2]/div[3]/div')
    print()
    print(data.text)

    with open("messages", "r") as f:
        if texto.text in f.read():
            print("\nMessage already alerted. Skipping.")
            f.close()
        elif texto.text not in f:
            try:
                xmlgen.generate_xml(perfil.text, texto.text, data.text, "/var/www/html/message.xml")
                print("\nXML file created")
            except:
                print("\nError creating the XML file")

            try:
                messagemaker.run(account, token, perfil.text, texto.text, data.text, source, destination)
                print(f"\nMessage sent to {destination}")
            except:
                print("\nError sending the message.")
                if call_make:
                    try:
                        callmaker.run(account, token, source, destination, url_xml)
                        print(f"\nCalling {destination} using {source} phone number.")
                    except:
                        print("\nThe call couldn't be made.")
                else:
                    print("Call method not enabled")

            with open("messages", "a") as r:
                r.write("{}{}".format(texto.text, "\n"))
                r.close()
        f.close()

    print("====================================================")

    try:
        time.sleep(time_wait)
    except TypeError:
        print("Waiting time variable not correctly defined (verify if you did input a number and not a word/string)")

    driver.refresh()