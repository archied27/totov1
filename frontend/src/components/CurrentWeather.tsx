import { useEffect, useState } from "react";
import { getCurrentWeather } from "../api/weather";
import { Box, Card, CardContent, Typography, Skeleton, Stack } from "@mui/material";

type WeatherCondition = {
    location: string,
    temp: number,
    condition: string,
    icon: string,
    precip: number
}

export default function CurrentWeather() {
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
                {currWeather ? 
                <>
                    <Typography variant="subtitle2" color="text.secondary">
                        {currWeather.location}
                    </Typography>
                    <Stack direction="row" alignItems="center" spacing={2} sx={{my:1}}>
                        <Typography variant="h3">{currWeather.temp}</Typography>
                        <Box component="img" src={currWeather.icon} alt={currWeather.condition} sx={{ width: 64, height: 64}}/>
                    </Stack>

                    <Typography variant="body1">{currWeather.condition}</Typography>

                    <Typography variant="body2" color="text.secondary">{currWeather.precip}mm</Typography>
                </>
            : <Skeleton variant="rectangular" height={100} />}
            </CardContent>
        </Card>
    )
}