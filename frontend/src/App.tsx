import MovieList from "./components/MovieList";
import NowPlaying from "./components/NowPlaying";
import Remote from "./components/Remote";

export default function App() {
  return (
    <div className="app">
      <NowPlaying />
      <Remote />
      <MovieList />
    </div>
  );
}
