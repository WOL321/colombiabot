"""
🇨🇴 Colombia Pride Bot - Kingdom Data Fetcher
Fetches live data from colombiadmc.site and DiplomaticaMC map
"""

import aiohttp
import json
import re
from typing import Optional, Dict, List

WEBSITE_URL = "https://colombiadmc.site"
MAP_URL = "https://map.diplomaticamc.com"

# Cache to avoid too many requests
_cache = {
    "data": None,
    "timestamp": 0
}
CACHE_DURATION = 300  # 5 minutes


async def fetch_map_data() -> Optional[Dict]:
    """Fetch live data from the Dynmap API."""
    try:
        async with aiohttp.ClientSession() as session:
            # Dynmap typically has these endpoints
            async with session.get(f"{MAP_URL}/up/worlds") as response:
                if response.status == 200:
                    worlds = await response.json()
                    return {"worlds": worlds}
    except Exception as e:
        print(f"Error fetching map data: {e}")
        return None


async def fetch_website_data() -> Optional[str]:
    """Fetch the website HTML."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(WEBSITE_URL) as response:
                if response.status == 200:
                    return await response.text()
    except Exception as e:
        print(f"Error fetching website: {e}")
        return None


def parse_towns_from_html(html: str) -> List[Dict]:
    """Parse town data from the website HTML."""
    towns = []
    
    # Pattern to match town sections with resident counts
    # Looking for: #### TownName\n\nX residents
    pattern = r'####\s+([A-Za-z\s]+?)\s*\n\n(\d+)\s+resident'
    matches = re.findall(pattern, html)
    
    for town_name, resident_count in matches:
        towns.append({
            "name": town_name.strip(),
            "residents": int(resident_count)
        })
    
    return towns


async def get_kingdom_data() -> Dict:
    """Get kingdom data with caching."""
    import time
    current_time = time.time()
    
    # Return cached data if fresh
    if _cache["data"] and (current_time - _cache["timestamp"]) < CACHE_DURATION:
        return _cache["data"]
    
    # Fetch fresh data
    html = await fetch_website_data()
    
    if html:
        towns = parse_towns_from_html(html)
        
        # Filter towns with at least 1 resident
        active_towns = [t for t in towns if t["residents"] > 0]
        
        # Sort by resident count
        active_towns.sort(key=lambda x: x["residents"], reverse=True)
        
        # Calculate totals
        total_residents = sum(t["residents"] for t in active_towns)
        total_towns = len(active_towns)
        
        data = {
            "towns": active_towns,
            "total_residents": total_residents,
            "total_towns": total_towns,
            "leadership": {
                "king": "9_88",
                "prime_minister": "OliveTree316",
                "ministers": [
                    "Novum_Vetus",
                    "Crowlia",
                    "qulipzz",
                    "pato541"
                ]
            }
        }
        
        # Cache the data
        _cache["data"] = data
        _cache["timestamp"] = current_time
        
        return data
    
    # Return empty data if fetch failed
    return {
        "towns": [],
        "total_residents": 0,
        "total_towns": 0,
        "leadership": {}
    }


async def get_towns_with_residents() -> List[Dict]:
    """Get list of towns that have at least 1 resident."""
    data = await get_kingdom_data()
    return data.get("towns", [])


async def get_total_residents() -> int:
    """Get total number of residents across all towns."""
    data = await get_kingdom_data()
    return data.get("total_residents", 0)


async def get_town_count() -> int:
    """Get total number of towns with residents."""
    data = await get_kingdom_data()
    return data.get("total_towns", 0)
