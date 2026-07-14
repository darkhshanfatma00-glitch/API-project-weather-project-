from fastapi import APIRouter, Depends, HTTPException, Query, status
from data import Weather, ResponseModel, WeatherRequestModel, UpdateRequestModel
from dependencies import verify_employee, verify_token

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)

@router.get(
    "/weather",
    response_model=list[ResponseModel],
    dependencies=[Depends(verify_employee), Depends(verify_token)]
)
def read_all(
    city: str | None = Query(
        default=None,
        title="City Name",
        description="Enter your city name",
        min_length=1,
        max_length=20,
    ),
    temperature: float | None = Query(
        default=None,
        ge=0,
        le=100,
        title="Temperature",
        description="Enter temperature",
    ),
    condition: str | None = Query(
        default=None,
        min_length=1,
        max_length=10,
    ),
    humidity: int | None = Query(
        default=None,
        ge=0,
        le=100,
    ),
    wind_speed: int | None = Query(
        default=None,
        ge=0,
        le=50,
    ),
    country: str | None = Query(
        default=None,
        min_length=1,
        max_length=10,
    ),
    created_by: str | None = Query(
        default=None,
        min_length=1,
        max_length=30,
    ),
    admin_note: str | None = Query(
        default=None,
        min_length=1,
        max_length=40,
    ),
):

    if (
        city is None and
        temperature is None and
        condition is None and
        humidity is None and
        wind_speed is None and
        country is None and
        created_by is None and
        admin_note is None
    ):
        return Weather

    result = []

    for weather in Weather:

        if city is not None and weather["city"].lower() != city.lower():
            continue

        if temperature is not None and weather["temperature"] != temperature:
            continue

        if condition is not None and weather["condition"].lower() != condition.lower():
            continue

        if humidity is not None and weather["humidity"] != humidity:
            continue

        if wind_speed is not None and weather["wind_speed"] != wind_speed:
            continue

        if country is not None and weather["country"].lower() != country.lower():
            continue

        if created_by is not None and weather["created_by"].lower() != created_by.lower():
            continue

        if admin_note is not None and weather["admin_note"].lower() != admin_note.lower():
            continue

        result.append(weather)

    return result





@router.get(
    "/weather/{id}",
    response_model=ResponseModel,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_employee), Depends(verify_token)]
)
def read_one(id: int):

    for weather in Weather:

        if weather["id"] == id:
            return weather

    raise HTTPException(
        status_code=404,
        detail="Weather not found"
    )




@router.post(
    "/weather",
    response_model=ResponseModel,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_employee), Depends(verify_token)]
)
def create_weather(weather: WeatherRequestModel):

    new_weather = {
        "id": len(Weather) + 1,
        "city": weather.city,
        "temperature": weather.temperature,
        "condition": weather.condition,
        "humidity": weather.humidity,
        "wind_speed": weather.wind_speed,
        "country": weather.country,
        "created_by": weather.created_by,
        "admin_note": weather.admin_note,
    }

    Weather.append(new_weather)

    return new_weather




@router.put(
    "/weather/{id}",
    response_model=ResponseModel,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_employee), Depends(verify_token)]
)
def update(id: int, weather: WeatherRequestModel):

    for existing_weather in Weather:

        if existing_weather["id"] == id:

            existing_weather["city"] = weather.city
            existing_weather["temperature"] = weather.temperature
            existing_weather["condition"] = weather.condition
            existing_weather["humidity"] = weather.humidity
            existing_weather["wind_speed"] = weather.wind_speed
            existing_weather["country"] = weather.country
            existing_weather["created_by"] = weather.created_by
            existing_weather["admin_note"] = weather.admin_note

            return existing_weather

    raise HTTPException(
        status_code=404,
        detail="Not found"
    )





@router.patch(
    "/weather/{id}",
    response_model=ResponseModel,
    dependencies=[Depends(verify_employee), Depends(verify_token)]
)
def update_one(id: int, weather: UpdateRequestModel):

    for existing_weather in Weather:

        if existing_weather["id"] == id:

            if weather.city is not None:
                existing_weather["city"] = weather.city

            if weather.temperature is not None:
                existing_weather["temperature"] = weather.temperature

            if weather.condition is not None:
                existing_weather["condition"] = weather.condition

            if weather.humidity is not None:
                existing_weather["humidity"] = weather.humidity

            if weather.wind_speed is not None:
                existing_weather["wind_speed"] = weather.wind_speed

            if weather.country is not None:
                existing_weather["country"] = weather.country

            if weather.created_by is not None:
                existing_weather["created_by"] = weather.created_by

            if weather.admin_note is not None:
                existing_weather["admin_note"] = weather.admin_note

            return existing_weather

    raise HTTPException(
        status_code=404,
        detail="Not found"
    )





@router.delete(
    "/weather/{id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_employee), Depends(verify_token)]
)
def delete_weather(id: int):

    for existing_weather in Weather:

        if existing_weather["id"] == id:

            Weather.remove(existing_weather)

            return {
                "existing_weather": existing_weather,
                "message": "Weather deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Not found"
    )