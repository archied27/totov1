import { apiGet } from "./client";

type WeatherCondition = {
    location: string,
    temp: number,
    condition: string,
    icon: string,
    precip: number
}

export function getCurrentWeather() {
    return apiGet<WeatherCondition>("/weather/current");
}