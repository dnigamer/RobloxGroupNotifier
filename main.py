import selenium.webdriver
import time

# Módulos personalizados
import callmaker
import xmlgen
import messagemaker

account = ''
token = ''
source = ''
destination = ''
url = ''

options = selenium.webdriver.ChromeOptions()
options.headless = True
prefs = {'profile.default_content_setting_values': {'images': 2, 'plugins': 2, 'popups': 2, 'geolocation': 2, 'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 'durable_storage': 2}}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = selenium.webdriver.Chrome(options=options)

driver.get('https://www.roblox.com/groups/645836/Pinewood-Builders-Security-Team')

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

    with open("mensagens_passadas.txt", "r") as f:
        if texto.text in f.read():
            print("\nMensagem já foi alertada. Skipped")
            f.close()
        elif texto.text not in f:
            try:
                xmlgen.generate_xml(perfil.text, texto.text, data.text, "/var/www/html/message.xml")
                print("\nFicheiro xml criado")
            except:
                print("\nErro ao criar o ficheiro XML")

            try:
                messagemaker.run(account, token, perfil.text, texto.text, data.text, source, destination)
                print("\nMensagem enviada para +351935272868")
            except:
                print("\nErro ao enviar mensagem")
                try:
                    callmaker.run(account, token, source, destination, url)
                    print("\nChamada a ser realizada")
                except:
                    print("\nA chamada não foi realizada")

            with open("mensagens_passadas.txt", "a") as r:
                r.write("{}{}".format(texto.text, "\n"))
                r.close()
        f.close()

    print("====================================================")
    time.sleep(900)
    driver.refresh()