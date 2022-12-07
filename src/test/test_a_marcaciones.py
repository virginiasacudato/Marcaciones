from src.TestBase.WebDriverSetup import WebDriverSetup
from src.Pages.PreconditionSQL import *
from src.Pages.Marcaciones import MarcacionesPage


class Marcaciones(WebDriverSetup):

    def test_a_marcacion_entrada(self):
        condtionsSQL()
        driver = self.driver
        marc = MarcacionesPage(driver)
        marc.new_marcacion()

    def test_b_marcacion_salida(self):
        driver = self.driver
        marc = MarcacionesPage(driver)
        marc.marcacion_salida()
        drop_all()
