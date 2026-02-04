import MovieList from "../components/MovieList";
import MpvSelecter from "../components/MpvSelecter";
import { isMpvOn } from "../api/mpv";
import { useEffect, useState } from "react";
import FullRemote from "../components/MovieRemote";

export default function MpvBrowser() {
  const [playing, setPlaying] = useState<boolean>(true)

  useEffect(() => {
    async function getPlaying() {
      const isPlaying = await isMpvOn();
      setPlaying(isPlaying.status);
    }
    getPlaying();
  }, []);

  return (
    <div className="app">
      {playing ? <><FullRemote/></> : <><MpvSelecter />
      <MovieList />
      </>}
      
    </div>
  );
}
