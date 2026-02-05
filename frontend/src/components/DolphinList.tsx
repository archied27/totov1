
import { useEffect, useState } from "react";
import { Grid, Box, Skeleton, Typography } from "@mui/material";
import { showGamesList, play } from "../api/dolphin";
import DolphinRemote from "./DolphinRemote";

type GamesList = {
    [key: string]: string
}

export default function GamesList() {
  const [games, setGames] = useState<GamesList | null>(null);

  useEffect(() => {
    async function fetchGames() {
      const data = await showGamesList();
      setGames(data);
    }
    fetchGames();
  }, []);

  async function handlePlay(file_path: string) {
    await play(file_path);
  }

  return (
    <Grid container spacing={2}>
      {games
        ? Object.entries(games).map(([id, game]) => (
            <Grid key={id} size={{xs:4, sm:3, md: 2}}>
              <Box sx={{
                cursor: "pointer",
                "&:hover": { transform: "scale(1.05)"},
                display: "flex",
                transition: "transform 0.2s",
                justifyContent: "center",
                border: "1px solid #ccc",
                borderRadius: 1
              }} onClick={() => handlePlay(game)}>
                <Typography variant="h6" align="center">{id}</Typography>
              </Box>
            </Grid>
          ))
        : <Skeleton variant="rectangular" height={100}/>
      }
      <DolphinRemote/>
    </Grid>
  );
}
