import pytest
from httpx import AsyncClient
from fastapi import status
from main import app

@pytest.mark.asyncio
async def test_create_menu_item_valid(async_client: AsyncClient):
    response = await async_client.post("/menu/", json={
        "name": "Pizza",
        "description": "Cheesy pizza",
        "price": 12.5,
        "available": True
    })
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["name"] == "Pizza"
    assert data["price"] == 12.5
    assert data["available"] is True

@pytest.mark.asyncio
async def test_create_menu_item_missing_field(async_client: AsyncClient):
    response = await async_client.post("/menu/", json={
        "description": "No name",
        "price": 10.0
    })
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

@pytest.mark.asyncio
async def test_create_menu_item_duplicate_name(async_client: AsyncClient):
    await async_client.post("/menu/", json={
        "name": "Burger",
        "description": "Tasty burger",
        "price": 8.0
    })
    response = await async_client.post("/menu/", json={
        "name": "Burger",
        "description": "Another burger",
        "price": 9.0
    })
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "already exists" in response.text

@pytest.mark.asyncio
async def test_create_menu_item_invalid_price(async_client: AsyncClient):
    response = await async_client.post("/menu/", json={
        "name": "Salad",
        "description": "Healthy",
        "price": -5.0
    })
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY