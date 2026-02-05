import { showShowList, play } from "../api/mpv";
import { useEffect, useState } from "react";
import { Grid, Box, Skeleton } from "@mui/material";

// Type definition for your movies
type ShowDetails = {
  [key: string]: {
    title: string;
    poster_path: string;
    file_path: string
  }
};

export default function ShowList({ onChanged, filter }: { onChanged: ()=>void; filter:string }) {
  const [shows, setShows] = useState<ShowDetails | null>(null);

  useEffect(() => {
    async function fetchMovies() {
      const data = await showShowList();
      setShows(data);
    }
    fetchMovies();
  }, []);

  async function handlePlay(file_path: string) {
    
    onChanged();
  }

  if (filter !== "All" && filter!== "Shows")
  {
    return null;
  }

  return (
    <Grid container spacing={2} p={2}>
      {shows
        ? Object.entries(shows).map(([id, show]) => (
            <Grid key={id} size={{xs:4, sm:3, md: 2}}>
              <Box sx={{
                cursor: "pointer",
                "&:hover": { transform: "scale(1.05)"},
                display: "flex",
                transition: "transform 0.2s",
                justifyContent: "center"
              }} onClick={() => handlePlay(show.file_path)}>
                <img src={`https://image.tmdb.org/t/p/original${show.poster_path}`} alt={show.title} style={{ width: "100%", height:"auto", borderRadius: 8}}/>
              </Box>
            </Grid>
          ))
        : <Skeleton variant="rectangular" height={100}/>
      }
    </Grid>
  );
}
