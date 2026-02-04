import { useState, useEffect } from "react"
import { getCurrentWeather } from "../api/weather"
import { Card, CardContent } from "@mui/material"

type WeatherCondition = {
    location: string,
    temp: number,
    condition: string,
    icon: string,
    precip: number
}

export default function LeftMainCard() {
    const [currWeather, setCurrWeather] = useState<WeatherCondition | null>(null)
    useEffect(() => {
            async function fetchWeather() {
                const data = await getCurrentWeather();
                setCurrWeather(data);
            }
            fetchWeather();
        }, []);
    
    return (
        <Card sx={{height: "100%"}}>
            <CardContent>
                
            </CardContent>
        </Card>
    )
}