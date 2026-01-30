import MpvOverlay from "../components/MpvOverlay";
import MovieList from "../components/MovieList";
import MpvSelecter from "../components/MpvSelecter";

export default function MpvBrowser() {
  return (
    <div className="app">
      <MpvSelecter />
      <MovieList />
      <MpvOverlay/>
    </div>
  );
}
