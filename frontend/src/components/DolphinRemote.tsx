import { ButtonGroup, Button, Box } from "@mui/material";
import { fullscreen, close, togglePlay } from "../api/dolphin";
import {
  Play,
  Pause,
  Square,
  Maximize
} from "lucide-react";
import { useState } from "react";



export default function DolphinRemote() {
  const [paused, setPaused] = useState(false)

  async function handleTogglePlay()
  {
    await togglePlay();
    setPaused((prev) => !prev);
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
