from fhir.resources.coverage import Coverage
from fhir.resources.fhirreference import FHIRReference
from fhir.resources.period import Period

def create_coverage(patient_id, org_id, subscriber_id, start, end):
    cov = Coverage()
    cov.status = "active"

    cov.beneficiary = FHIRReference(reference=f"Patient/{patient_id}")
    cov.payor = [FHIRReference(reference=f"Organization/{org_id}")]

    cov.subscriberId = subscriber_id

    cov.period = Period(start=start, end=end)

    return cov
