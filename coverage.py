import requests
import json

# Servidor público HAPI FHIR (R4)
BASE_URL = "https://hapi.fhir.org/baseR4"

def crear_organization():
    """
    Crea una Organization que representa la cobertura médica
    """

    organization = {
        "resourceType": "Organization",
        "name": "Obra Social TP6",
        "identifier": [
            {
                "system": "http://example.org/obra-social-id",
                "value": "OS-TP6-001"
            }
        ]
    }

    response = requests.post(
        f"{BASE_URL}/Organization",
        headers={"Content-Type": "application/fhir+json"},
        data=json.dumps(organization)
    )

    print("Status Organization:", response.status_code)
    print("Respuesta Organization:", response.json())

    org_id = response.json().get("id")
    print(f"Organization creada con ID: {org_id}\n")
    return org_id


def crear_coverage(patient_id, organization_id):
    """
    Crea un recurso Coverage asociado a:
    - patient_id: Patient beneficiario
    - organization_id: Organization que actúa como payor
    """

    coverage = {
        "resourceType": "Coverage",
        "status": "active",

        # Paciente beneficiario de la cobertura
        "beneficiary": {
            "reference": f"Patient/{patient_id}"
        },

        # Entidad que brinda la cobertura (obra social / prepaga)
        "payor": [
            {
                "reference": f"Organization/{organization_id}"
            }
        ],

        # Número de afiliado
        "subscriberId": "AFI-TP6-12345678",

        # Relación con el titular: en este ejemplo, el paciente es el titular
        "relationship": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/subscriber-relationship",
                    "code": "self",
                    "display": "Self"
                }
            ]
        },

        # Período de vigencia de la cobertura
        "period": {
            "start": "2024-01-01",
            "end": "2025-12-31"
        }
    }

    response = requests.post(
        f"{BASE_URL}/Coverage",
        headers={"Content-Type": "application/fhir+json"},
        data=json.dumps(coverage)
    )

    print("Status Coverage:", response.status_code)
    print("Respuesta Coverage:", response.json())

    cov_id = response.json().get("id")
    print(f"Coverage creada con ID: {cov_id}\n")
    return cov_id


if __name__ == "__main__":
    # PATIENT_ID = "52911438"
    PATIENT_ID = input("Ingresa Patient ID: ")

    # 1) Crear la Organization (obra social)
    org_id = crear_organization()

    # 2) Crear la Coverage asociada al Patient y a la Organization
    coverage_id = crear_coverage(PATIENT_ID, org_id)
