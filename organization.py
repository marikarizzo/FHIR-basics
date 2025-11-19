from fhir.resources.organization import Organization

def create_organization(name, org_id=None):
    org = Organization()
    org.name = name
    if org_id:
        org.id = org_id
    return org
