import { fullscreen, close, togglePlay, getPause } from "../api/mpv";
import {
  Play,
  Pause,
  Square,
  Maximize,
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
    <div className="remote">
      <button onClick={() => handleTogglePlay()}>
        {paused ? <Play size={32}/> : <Pause size={32}/>}
      </button>
      <button onClick={() => fullscreen()}>
        <Maximize size={32}/>
      </button>
      <button onClick={() => close()}>
        <Square size={32} />
      </button>
    </div>
  );
}
