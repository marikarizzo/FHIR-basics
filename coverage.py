import json

class SimpleCoverage:
    def __init__(self, patient_id, org_id, subscriber_id, start, end):
        # Armamos un recurso FHIR Coverage "a mano" en formato dict
        self.data = {
            "resourceType": "Coverage",
            "status": "active",
            # Quién es el beneficiario de la cobertura
            "beneficiary": {
                "reference": f"Patient/{patient_id}"
            },
            # Quién paga / brinda la cobertura
            "payor": [
                {
                    "reference": f"Organization/{org_id}"
                }
            ],
            # Número de afiliado
            "subscriberId": str(subscriber_id),
            # Período de vigencia
            "period": {
                "start": start,
                "end": end
            }
        }

    # Este método es lo único que necesita base.py
    def json(self):
        return json.dumps(self.data)


def create_coverage(patient_id, org_id, subscriber_id, start, end):
    """
    Crea un recurso Coverage simple que cumple con la consigna:
    - entidad que brinda la cobertura (Organization)
    - número de afiliado
    - período de vigencia
    - relación con el paciente (beneficiary)
    """
    return SimpleCoverage(
        patient_id=patient_id,
        org_id=org_id,
        subscriber_id=subscriber_id,
        start=start,
        end=end,
    )
