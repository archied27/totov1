import MpvOverlay from "../components/MpvOverlay";
import MovieList from "../components/MovieList";

export default function MpvBrowser() {
  return (
    <div className="app">
      <MovieList />
      <MpvOverlay/>
    </div>
  );
}
