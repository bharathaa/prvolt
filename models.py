from typing import Optional, List
from pydantic import BaseModel

class Lead(BaseModel):
    id: int
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    position: Optional[str] = None
    company: Optional[str] = None
    company_industry: Optional[str] = None
    confidence_score: Optional[int] = None
    website: Optional[str] = None
    country_code: Optional[str] = None
    company_size: Optional[str] = None
    source: Optional[str] = None
    linkedin_url: Optional[str] = None
    phone_number: Optional[str] = None
    twitter: Optional[str] = None
    sync_status: Optional[str] = None
    notes: Optional[str] = None
    sending_status: Optional[str] = None
    last_activity_at: Optional[str] = None
    last_contacted_at: Optional[str] = None
    verification: Optional[dict] = None
    leads_list: Optional[dict] = None
    created_at: Optional[str] = None

class LData(BaseModel):
    leads: List[Lead]
    offset: Optional[int] = None
    limit: Optional[int] = None
    total: Optional[int] = None

class LeadsData(BaseModel):
    data: LData
    meta: Optional[dict] = None

class Email(BaseModel):
    value: str
    type: Optional[str] = None
    confidence: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    position: Optional[str] = None
    seniority: Optional[str] = None
    department: Optional[str] = None
    linkedin: Optional[str] = None
    twitter: Optional[str] = None
    phone_number: Optional[str] = None

class DomainSearch(BaseModel):
    domain: Optional[str] = None
    disposable: Optional[bool] = None
    webmail: Optional[bool] = None
    accept_all: Optional[bool] = None
    pattern: Optional[str] = None
    organization: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    emails: List[Email]

class DomainSearchData(BaseModel):
    data: DomainSearch
    meta: Optional[dict] = None

class CreateLead(BaseModel):
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    position: Optional[str] = None
    company: Optional[str] = None
    linkedin_url: Optional[str] = None
    phone_number: Optional[str] = None
    notes: Optional[str] = None

class GetLeadsData(BaseModel):
    data: Lead
    meta: Optional[dict] = None

