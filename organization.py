from fhir.resources.organization import Organization


def create_organization(name: str, org_id: str | None = None) -> Organization:
    org = Organization()
    org.name = name
    if org_id:
        org.id = org_id
    return org
