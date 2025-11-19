import json
import requests
from dataclasses import is_dataclass, asdict

def send_resource_to_hapi_fhir(resource, resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}"
    headers = {"Content-Type": "application/fhir+json"}

    # 1) Modelos FHIR nuevos (tienen model_dump_json)
    if hasattr(resource, "model_dump_json"):
        resource_json = resource.model_dump_json(by_alias=True)

    # 2) Modelos FHIR viejos (tienen json())
    elif hasattr(resource, "json"):
        resource_json = resource.json()

    # 3) Objetos "simples" como tu SimpleCoverage
    else:
        # Intentamos convertir a dict y luego a JSON
        if is_dataclass(resource):
            data = asdict(resource)
        elif isinstance(resource, dict):
            data = resource
        else:
            # Clase normal: usamos su __dict__
            data = resource.__dict__

        resource_json = json.dumps(data)

    response = requests.post(url, headers=headers, data=resource_json)

    if response.status_code == 201:
        print(f"{resource_type} creado exitosamente")
        return response.json().get("id")
    else:
        print(f"Error al crear el recurso {resource_type}: {response.status_code}")
        print(response.text)
        return None



# Buscar el recurso por ID
def get_resource_from_hapi_fhir(resource_id: str, resource_type: str):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}/{resource_id}"
    headers = {"Accept": "application/fhir+json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(f"{resource_type} le do desde HAPI FHIR:")
        print(response.json())
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.text)
