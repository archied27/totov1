import { ButtonGroup, Button, Box } from "@mui/material";
import { fullscreen, close, togglePlay, getPause } from "../api/mpv";
import {
  Play,
  Pause,
  Square,
  Maximize
} from "lucide-react";
import { useEffect, useState } from "react";



export default function Remote() {
  const [paused, setPaused] = useState(false)

  async function getPauseStatus()
  {
    const data = await getPause()
    setPaused(data.pause)
  }

  useEffect(() => {
    getPauseStatus()
  }, [])

  async function handleTogglePlay()
  {
    await togglePlay();
    getPauseStatus();
  }

  return (
    <Box sx={{
      position: "fixed",
      bottom: 0,
      left: 0,
      textAlign: "center",
      width: "100%",
      bgcolor: "background",
      p: 1,
      boxShadow: 3,
      zIndex:1000
    }}>
      <ButtonGroup variant="contained">
        <Button onClick={() => handleTogglePlay()}>
          {paused ? <Play size={32}/> : <Pause size={32}/>}
        </Button>
        <Button onClick={() => fullscreen()}>
          <Maximize size={32}/>
        </Button>
        <Button onClick={() => close()}>
          <Square size={32} />
        </Button>
      </ButtonGroup>
    </Box>
  );
}
