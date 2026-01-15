import { showMovieList, play } from "../api/mpv";
import { useEffect, useState } from "react";

// Type definition for your movies
type MovieDetails = {
  [key: string]: {
    title: string;
    poster_path: string;
    file_path: string
  }
};

export default function MovieList() {
  const [movies, setMovies] = useState<MovieDetails | null>(null);

  useEffect(() => {
    async function fetchMovies() {
      const data = await showMovieList();
      setMovies(data);
    }
    fetchMovies();
  }, []);



  return (
    <div className="movie-grid">
      {movies
        ? Object.entries(movies).map(([id, movie]) => (
            <div key={id} className="movie-card">
              <img
                src={`https://image.tmdb.org/t/p/w200${movie.poster_path}`}
                alt={movie.title}
                onClick={() => play(movie.file_path) }
                className="poster"
              />
            </div>
          ))
        : <p>Loading...</p>
      }
    </div>
  );
}
