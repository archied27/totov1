import { Box, Grid } from "@mui/material";
import CurrentWeather from "../components/CurrentWeather";

export default function Dashboard() {
  return (
    <Box sx={{p : 2}}>
      <Grid container spacing={2}>
        <Grid size={{xs:4, md:2}}>
          <CurrentWeather/>
        </Grid>
        <Grid size={{xs:8, md:4}}>
          <CurrentWeather/>
        </Grid>
      </Grid>
    </Box>
  );
}
