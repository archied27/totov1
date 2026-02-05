import MovieList from "../components/MovieList";
import MpvSelecter from "../components/MpvSelecter";
import { isMpvOn } from "../api/mpv";
import { useEffect, useState } from "react";
import FullRemote from "../components/MovieRemote";
import ShowList from "../components/ShowList";

export default function MpvBrowser() {
  const [playing, setPlaying] = useState<boolean>(false)
  const [selected, setSelected] = useState("All");

  async function getPlaying() {
      const isPlaying = await isMpvOn();
      setPlaying(isPlaying.status);
  }

  useEffect(() => {
    getPlaying();
  }, []);

  return (
    <div className="app">
      {playing ? <><FullRemote onStopped={getPlaying}/></> : <><MpvSelecter selected={selected} onSelectionChange={setSelected}/>
      <MovieList onChanged={getPlaying} filter={selected}/>
      <ShowList onChanged={getPlaying} filter={selected}/>
      </>}
      
    </div>
  );
}
