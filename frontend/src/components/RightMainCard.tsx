import { useState, useEffect } from "react"
import { Card, CardContent, Box, IconButton, Skeleton, Typography } from "@mui/material"
import FullRemote from "./MovieRemote"
import { getCurrentDetails, getPause, togglePlay, close } from "../api/mpv"
import { CloseOutlined, Pause, PlayArrow } from "@mui/icons-material"

type MovieSummary = {
  title: string,
  poster_path: string
  file_path: string
}

export default function RightMainCard() {
    const [paused, setPaused] = useState(false)
    const [movieDetails, setMovieDetails] = useState<MovieSummary | null>(null)

    async function getPauseStatus()
    {
        const data = await getPause()
        setPaused(data.pause)
    }

    useEffect(() => {
        async function getMovieDetails() {
            const data = await getCurrentDetails();
            setMovieDetails(data);
        }
        getMovieDetails();
        getPauseStatus();
    }, []);

    async function handleTogglePlay()
    {
        await togglePlay();
        getPauseStatus();
    }

    return (
        <Card sx={{height: "100%"}}>
            <CardContent>
                { movieDetails ?
                <Box sx={{display:"flex", alignItems: "center", flexDirection:"row", gap: 0}}>
                    <Box sx={{display: "flex", p:1, width: "100%", justifyContent:"center", height:"100%", objectFit:"cover"}}>
                        <img src={`https://image.tmdb.org/t/p/original${movieDetails.poster_path}`} alt={movieDetails.title} style={{ width: "100%", maxWidth: "42vh", maxHeight: "79vh", height:"auto", borderRadius: 8}}/>
                    </Box>
                    <Box sx={{display:"flex", gap:1, width:"100%", height:"100%", alignItems:"center", alignContent:"content", flexDirection:"column"}}>
                        <Typography variant="h6" color="text.secondary" fontWeight={600}>{movieDetails.title}</Typography>
                        <Box sx={{display:"flex", flexDirection:"row", justifyContent:"center", width:"100%"}}>
                            <IconButton size="large" onClick={handleTogglePlay}>
                                {paused ? <PlayArrow fontSize="large" /> : <Pause fontSize="large"/>}
                            </IconButton>
                            <IconButton size="large" onClick={close}>
                                <CloseOutlined fontSize="large"/>
                            </IconButton>
                        </Box>
                    </Box>
                </Box> : <Skeleton variant="rectangular" height={100}/>}
            </CardContent>
        </Card>
    )
}