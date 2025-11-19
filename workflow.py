from patient import create_patient_resource
from organization import create_organization
from coverage import create_coverage
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir

if __name__ == "__main__":
    # 1) Crear y enviar Organization (obra social / prepaga)
    org = create_organization("OSDE")
    org_id = send_resource_to_hapi_fhir(org, "Organization")

    # 2) Crear y enviar Patient
    patient = create_patient_resource(
        family_name="Gonzalez",
        given_name="Imanol",
        birth_date="2003-01-01",
        gender="male",
        phone="1122334455",
    )
    patient_id = send_resource_to_hapi_fhir(patient, "Patient")

    # 3) Crear y enviar Coverage (cobertura médica)
    if patient_id and org_id:
        cov = create_coverage(
            patient_id=patient_id,
            org_id=org_id,
            subscriber_id="123456789",          # nro de afiliado
            start="2025-01-01",
            end="2025-12-31",
        )
        cov_id = send_resource_to_hapi_fhir(cov, "Coverage")

        # 4) Leer los tres recursos desde HAPI FHIR
        print("\n--- Leyendo recursos desde HAPI ---")
        get_resource_from_hapi_fhir(org_id, "Organization")
        get_resource_from_hapi_fhir(patient_id, "Patient")
        if cov_id:
            get_resource_from_hapi_fhir(cov_id, "Coverage")
    else:
        print("No se pudo crear patient u organization, no se crea el coverage.")
