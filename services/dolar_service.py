import requests
from model.indicador_uf import IndicadorUF


class DolarService:

    URL = "https://mindicador.cl/api/dolar"

    @staticmethod
    def obtener_dolar():
        try:
            respuesta = requests.get(
                DolarService.URL,
                timeout=5
            )

            respuesta.raise_for_status()

            datos = respuesta.json()

            if "serie" not in datos or not datos["serie"]:
                raise ValueError("La API no entregó datos del dólar.")

            dato = datos["serie"][0]

            return IndicadorUF(
                valor=dato["valor"],
                fecha=dato["fecha"]
            )

        except requests.RequestException:
            print("No fue posible obtener el dólar desde Internet.")
            return None

        except (ValueError, KeyError):
            print("La respuesta de la API del dólar no es válida.")
            return None