import requests
from model.indicador_uf import IndicadorUF


class UFService:

    URL = "https://mindicador.cl/api/uf"

    @staticmethod
    def obtener_uf():
        try:
            respuesta = requests.get(UFService.URL, timeout=5)
            respuesta.raise_for_status()

            datos = respuesta.json()

            if "serie" not in datos or not datos["serie"]:
                raise ValueError("La API no entregó datos de UF.")

            dato = datos["serie"][0]

            return IndicadorUF(
                valor=dato["valor"],
                fecha=dato["fecha"]
            )

        except requests.RequestException:
            print("No fue posible obtener la UF desde Internet.")
            return None

        except (ValueError, KeyError):
            print("La respuesta de la API de UF no es válida.")
            return None

    @staticmethod
    def calcular_tasa_ahorro():
        indicador = UFService.obtener_uf()

        if indicador is None:
            return 0.01

        tasa_base = 0.01
        factor_uf = indicador.valor / 1_000_000

        return tasa_base + factor_uf