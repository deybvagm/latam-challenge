from pydantic import BaseModel, validator


class Flight(BaseModel):
    OPERA: str
    TIPOVUELO: str
    MES: int

    @validator("OPERA")
    def validate_airline(cls, v):
        valid_airlines = [
            'Grupo LATAM',
            'Sky Airline',
            'Aerolineas Argentinas',
            'Copa Air',
            'Latin American Wings',
            'Avianca',
            'JetSmart SPA',
            'Gol Trans',
            'American Airlines',
            'Air Canada',
            'Iberia',
            'Delta Air',
            'Air France',
            'Aeromexico',
            'United Airlines',
            'Oceanair Linhas Aereas',
            'Alitalia',
            'K.L.M.',
            'British Airways',
            'Qantas Airways',
            'Lacsa',
            'Austral',
            'Plus Ultra Lineas Aereas'
        ]
        if v not in valid_airlines:
            raise ValueError("Invalid OPERA")
        return v

    @validator("TIPOVUELO")
    def validate_tipo_vuelo(cls, v):
        if v not in ["N", "I"]:
            raise ValueError("Invalid TIPOVUELO")
        return v

    @validator("MES")
    def validate_mes(cls, v):
        if v < 1 or v > 12:
            raise ValueError("Invalid MES")
        return v
