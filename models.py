from typing import TypedDict
from pydantic import BaseModel

class LeadData(TypedDict):
    email: str
    first_name: str
    last_name: str
    position: str
    company: str

class LeadMetaData(TypedDict):
    source: str
    campaign: str

class CreateLead(BaseModel):
    """Create Lead model."""
    
    data: LeadData
    meta: LeadMetaData

class Lead(BaseModel):
    """Lead response model."""
    
    id: int
    email: str
    first_name: str
    last_name: str
    position: str
    company: str

class DomainSearchData(TypedDict):
    leads: list[Lead]
    total_count: int

class DomainSearchMetaData(TypedDict):
    page: int
    per_page: int

class DomainSearch(BaseModel):
    """Complete domain search response."""
    
    data: DomainSearchData
    meta: DomainSearchMetaData