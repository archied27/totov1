import { Box, Grid } from "@mui/material";
import CurrentWeather from "../components/CurrentWeather";

export default function Dashboard() {
  return (
    <Box sx={{p : 2, height: "80vh"}}>
      <Grid container spacing={1} sx={{height: "100%"}}>
        <Grid size={{xs:6, sm:4, md:2}}>
          <CurrentWeather/>
        </Grid>
        <Grid size="grow">
          <CurrentWeather/>
        </Grid>
      </Grid>
    </Box>
  );
}
