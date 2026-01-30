import { showMovieList, play } from "../api/mpv";
import { useEffect, useState } from "react";
import { Grid, Box } from "@mui/material";

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
    <Grid container spacing={2}>
      {movies
        ? Object.entries(movies).map(([id, movie]) => (
            <Grid key={id} size={{xs:4, sm:3, md: 2}}>
              <Box sx={{
                cursor: "pointer",
                "&:hover": { transform: "scale(1.05)"},
                display: "flex",
                transition: "transform 0.2s",
                justifyContent: "center"
              }} onClick={() => play(movie.file_path)}>
                <img src={`https://image.tmdb.org/t/p/w200${movie.poster_path}`} alt={movie.title} style={{ width: "100%", height:"auto", borderRadius: 8}}/>
              </Box>

            </Grid>
          ))
        : <p>Loading...</p>
      }
    </Grid>
  );
}
