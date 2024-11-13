from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip  

class WhatsAppBot:
    def __init__(self, profile_path):
        self.options = Options()
        self.options.add_argument("-profile")
        self.options.add_argument(profile_path)
        
        try:
            self.driver = webdriver.Firefox(options=self.options)
        except TypeError:
            try:
                self.driver = webdriver.Firefox(firefox_options=self.options)
            except:
                self.driver = webdriver.Firefox()
                
        self.driver.get("https://web.whatsapp.com")
        print("Esperando a que WhatsApp Web cargue...")
        time.sleep(20)  

    def buscar_chat(self, nombre_chat):
        try:
            print(f"Buscando el chat '{nombre_chat}'...")
            search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
            search_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, search_xpath))
            )
            search_box.clear()
            time.sleep(2)  
            search_box.send_keys(nombre_chat)
            time.sleep(4)  
            
            chat_xpath = f'//span[@title="{nombre_chat}"]'
            chat = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, chat_xpath))
            )
            chat.click()
            time.sleep(4)  
            print(f"Chat '{nombre_chat}' encontrado y seleccionado")
            return True
        except Exception as e:
            print(f"Error al buscar el chat: {e}")
            return False

    def enviar_mensaje(self, mensaje):
        try:
            
            pyperclip.copy(mensaje)
            
            input_xpath = '//div[@contenteditable="true"][@data-tab="10"]'
            input_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, input_xpath))
            )
            
            input_box.clear()
            time.sleep(2)
            
            input_box.click()
            time.sleep(2)
            
            input_box.send_keys(Keys.CONTROL + 'v')
            
            time.sleep(2)
            
            input_box.send_keys(Keys.ENTER)
            
            time.sleep(3)
            return True
            
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")
            return False

    def cerrar(self):
        try:
            if hasattr(self, 'driver'):
                self.driver.quit()
        except Exception as e:
            print(f"Error al cerrar el navegador: {e}")

def obtener_mensaje_reporte():
    return """Esto es un mensaje programado"""

def main():
    profile_path = "/root/.mozilla/firefox/8rvg6zii.jorge"
    bot = None
    
    try:
        bot = WhatsAppBot(profile_path)
        print("Bot iniciado correctamente")
        
        nombre_chat = "pornodeenanoscondiarrea"
        
        if bot.buscar_chat(nombre_chat):
            print(f"Chat '{nombre_chat}' encontrado")
            
            contador = 0
            while True:
                mensaje = obtener_mensaje_reporte()
                print(f"\nPreparando para enviar reporte #{contador + 1}")
                print("Esperando 5 segundos antes de enviar...")
                time.sleep(5)
                
                if bot.enviar_mensaje(mensaje):
                    contador += 1
                    print(f"Reporte #{contador} enviado correctamente")
                else:
                    print("Error al enviar el reporte")
                
                
                print("Creador; jorgekhemamadas")
                time.sleep(3600)
                
    except KeyboardInterrupt:
        print("\nDeteniendo el bot...")
    except Exception as e:
        print(f"Error general: {e}")
    finally:
        if bot:
            bot.cerrar()

if __name__ == "__main__":
    main()
