import requests
from model.indicador_uf import IndicadorUF


class DolarService:

    URL = "https://indicadores.cl/api/v1/dolar.json"

    @staticmethod
    def obtener_dolar():
        try:
            respuesta = requests.get(
                DolarService.URL,
                timeout=15
            )

            respuesta.raise_for_status()

            datos = respuesta.json()

            if "valor" not in datos or "fecha" not in datos:
                raise ValueError("La API no entregó datos del dólar.")

            return IndicadorUF(
                valor=datos["valor"],
                fecha=datos["fecha"]
            )

        except requests.RequestException:
            print("No fue posible obtener el dólar desde Internet.")
            return None

        except (ValueError, KeyError):
            print("La respuesta de la API del dólar no es válida.")
            return None