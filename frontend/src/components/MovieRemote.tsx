import { Box, Skeleton, IconButton } from "@mui/material";
import { close, togglePlay, getPause, getCurrentDetails } from "../api/mpv";
import { useEffect, useState } from "react";
import { CloseOutlined, Pause, PlayArrow } from "@mui/icons-material";

type MovieSummary = {
  title: string,
  poster_path: string
  file_path: string
}

export default function FullRemote({ onStopped }: { onStopped: ()=>void}) {
  const [paused, setPaused] = useState(false)
  const [movieDetails, setMovieDetails] = useState<MovieSummary | null>(null)

  async function getPauseStatus()
  {
    const data = await getPause()
    setPaused(data.pause)
  }

  function sleep(ms: number) {
    return new Promise(resolve => setTimeout(resolve, ms));
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

  async function handleClose()
  {
    await close();
    await sleep(500);
    onStopped();
  }

  return (
    movieDetails ?
    <Box sx={{display:"flex", alignItems: "center", flexDirection:"column", gap: 2}}>
        <Box sx={{display: "flex", p:2, justifyContent: "center", alignItems:"center", width: "100%", height:"100%", objectFit:"cover"}}>
            <img src={`https://image.tmdb.org/t/p/original${movieDetails.poster_path}`} alt={movieDetails.title} style={{ width: "100%", height:"auto", borderRadius: 8}}/>
        </Box>
        <Box sx={{display:"flex", gap:1, mt:1}}>
            <IconButton size="large" onClick={handleTogglePlay}>
                {paused ? <PlayArrow fontSize="large" /> : <Pause fontSize="large"/>}
            </IconButton>
            <IconButton size="large" onClick={handleClose}>
                <CloseOutlined fontSize="large"/>
            </IconButton>
        </Box>
    </Box> : <Skeleton variant="rectangular" height={100}/>);
}
