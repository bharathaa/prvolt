from httpx import AsyncClient
from fastapi import FastAPI, HTTPException
from models import LeadsData, DomainSearchData, CreateLead, GetLeadsData

app = FastAPI(title="Hunter Leads API")

@app.get("/leads", response_model=LeadsData)
async def get_leads():
    apiKey = "af6af38ccb697fb408411f0a3c64bec9835a11ae"
    url = f"https://api.hunter.io/v2/leads?api_key={apiKey}"
    
    async with AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch leads data")
        return response.json()
    

@app.get("/domain-search/{domain}", response_model=DomainSearchData)
async def get_list_search_domain(domain: str):
    api_key = "af6af38ccb697fb408411f0a3c64bec9835a11ae"
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api_key}"
    
    async with AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch domains data")
        return response.json()


@app.post("/lead", response_model=GetLeadsData)
async def create_lead(lead_data: CreateLead):
    api_key = "af6af38ccb697fb408411f0a3c64bec9835a11ae"
    url = f"https://api.hunter.io/v2/leads?api_key={api_key}"
    
    async with AsyncClient() as client:
        response = await client.post(url, json=lead_data.model_dump(exclude_none=True))
        if response.status_code not in [200, 201]:
            raise HTTPException(status_code=response.status_code, detail="Failed to create lead")
        return response.json()
