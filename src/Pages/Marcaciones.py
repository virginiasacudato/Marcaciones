import os
import time
from seleniumpagefactory.Pagefactory import PageFactory



class MarcacionesPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver  # Se inicializa el controlador en el constructor (método init)
        self.timeout = 15

    # Localizadores en diccionario
    locators = {
        'btn_control': ('XPATH', '/html/body/main/aside/section/nav/ul/li[4]/div/label'),
        'btn_marcaciones': ('ID', 'fichadasUrl'),
        'btn_add': ('XPATH', '//*[@id="formCargarFichadas"]/div[3]/button'),
        'inpt_time': ('XPATH', '//*[@id="TimeHoraFichada"]'),
        'check_after': ('XPATH', '//*[@id="divFechaHoraFichada"]/div[2]/div/div/label'),
        'save_fich': ('ID', 'GuardarNuevaFichada'),
        'info_marc': ('XPATH', '//*[@id="tableBody"]/tr/td[4]'),
        'second_table': ('XPATH', '//*[@id="tableBody"]/tr[2]/td[4]')

    }

    def new_marcacion(self):

        self.btn_control.click_button()
        self.btn_marcaciones.click_button()

        self.btn_add.click_button()
        time.sleep(3)
        self.inpt_time.clear_text()
        self.inpt_time.set_text("22:00")
        time.sleep(2)
        self.save_fich.click_button()
        time.sleep(2)
        info_e_s = self.info_marc.get_text()
        short_e_s = info_e_s[6:9]
        if short_e_s == '(E)':
            print('Se genero la marcacion de entrada.')
            assert True
        else:
            assert False

    def marcacion_salida(self):
        self.btn_control.click_button()
        self.btn_marcaciones.click_button()
        self.btn_add.click_button()
        time.sleep(3)
        self.inpt_time.clear_text()
        self.inpt_time.set_text("6:00")
        self.check_after.click_button()
        time.sleep(2)
        self.save_fich.click_button()
        time.sleep(2)
        info_e_s = self.second_table.get_text()
        short_e_s = info_e_s[6:10]
        if short_e_s == '(+S)':
            print('Se genero la marcacion de salida.')
            assert True
        else:
            assert False
