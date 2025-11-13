import asyncio
from fastapi import FastAPI

app=FastAPI()

async def get_user_profile(user_id:int)->dict:
    await asyncio.sleep(0.1)
    return {"name":"aniket","email":"aniket@gmail.com"}

async def get_recent_order(user_id:int)-> list:
    await asyncio.sleep(0.2)
    return [{"order_id":101,"total":99.99},{"order_id":102,"total":19.50}]

async def get_recommendations(user_id:int)->list:
    await asyncio.sleep(0.15)
    return [{"Product name":"New Laptop"},{"Product name":"Wireless Mouse"}]

@app.get("/users/{user_id}/dashboard")
async def get_user_dashboard(user_id:int):
    profile_task=asyncio.create_task(get_user_profile(user_id))
    order_task=asyncio.create_task(get_recent_order(user_id))
    recs_task=asyncio.create_task(get_recommendations(user_id))
    
    
    profile,order,recommendation=await asyncio.gather(
        profile_task,order_task,recs_task
    )
    
    return{
        "profile":profile,
        "recent_orders":order,
        "recommendations":recommendation,        
    }