from httpx import AsyncClient
from typing import List
from fastapi import FastAPI

from models import CreateLead, Lead, DomainSearch
import os

app = FastAPI(title="Hunter Leads API")


@app.get("/all_leads", response_model=CreateLead)
async def get_all_leads() -> CreateLead:
    """Get all leads."""
    async with AsyncClient() as client:
        response = await client.get(
            f"https://api.hunter.io/v2/leads?api_key={os.environ.get('HUNTER_API_KEY')}"
        )
        response.raise_for_status()
        list_leads = response.json()
        return CreateLead(**list_leads)


@app.get("/domain-search/{domain}", response_model=DomainSearch)
async def domain_search(domain: str) -> DomainSearch:
    """Search domain by domain name."""
    async with AsyncClient() as client:
        response = await client.get(
            f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={os.environ.get('HUNTER_API_KEY')}"
        )
        response.raise_for_status()
        search_data = response.json()
        return DomainSearch(**search_data)


@app.post("/leads", response_model=Lead)
async def create_lead(lead_data: CreateLead) -> Lead:
    """Create new lead."""
    async with AsyncClient() as client:
        response = await client.post(
            f"https://api.hunter.io/v2/leads?api_key={os.environ.get('HUNTER_API_KEY')}",
            json=lead_data.model_dump(),
        )
        response.raise_for_status()
        response_lead_data = response.json()
        return Lead(**response_lead_data)