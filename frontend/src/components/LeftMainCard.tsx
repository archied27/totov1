import { useState, useEffect } from "react"
import { getCurrentWeather } from "../api/weather"
import { Box, Card, CardContent, Skeleton, Stack, Typography } from "@mui/material"

type WeatherCondition = {
    location: string,
    temp: number,
    condition: string,
    icon: string,
    precip: number
}

export default function LeftMainCard() {
    const [currWeather, setCurrWeather] = useState<WeatherCondition | null>(null)
    const [time, setTime] = useState(new Date());

    useEffect(() => {
        const interval = setInterval(() => {
            setTime(new Date());
        }, 10000);
        return () => clearInterval(interval);
    }, [])

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
                {currWeather ? <>
                    <Stack direction="row" alignItems="center" spacing={1} sx={{my:1}}>
                        <Box component="img" src={currWeather.icon} alt={currWeather.condition} sx={{ width: 64, height: 64}}/>
                        <Stack direction="column" spacing={0}>
                            <Typography variant="h5" color="text.secondary"> {currWeather.temp}°c </Typography>
                            <Typography variant="body1" color="text.secondary"> {currWeather.condition} </Typography>
                        </Stack>
                    </Stack>
                    
                </>
                : <Skeleton variant="rectangular" height={100}/>}
                <Stack flexGrow={1} justifyContent="center" alignItems="center" py={2}>
                    <Typography variant="h2" fontFamily="system-ui" fontWeight={600} letterSpacing={1} lineHeight={2} sx={{opacity: 0.8}}>
                        {time.toLocaleTimeString([], {hour:"numeric", minute: "2-digit"})}
                    </Typography>
                </Stack>
            </CardContent>
        </Card>
    )
}