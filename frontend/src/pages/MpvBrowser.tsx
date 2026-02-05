import MovieList from "../components/MovieList";
import MpvSelecter from "../components/MpvSelecter";
import { isMpvOn } from "../api/mpv";
import { useEffect, useState } from "react";
import FullRemote from "../components/MovieRemote";

export default function MpvBrowser() {
  const [playing, setPlaying] = useState<boolean>(false)

  async function getPlaying() {
      const isPlaying = await isMpvOn();
      setPlaying(isPlaying.status);
  }

  useEffect(() => {
    getPlaying();
  }, []);

  return (
    <div className="app">
      {playing ? <><FullRemote onStopped={getPlaying}/></> : <><MpvSelecter />
      <MovieList onChanged={getPlaying}/>
      </>}
      
    </div>
  );
}
