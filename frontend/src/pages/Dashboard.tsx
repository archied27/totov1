import { Box, Grid } from "@mui/material";
import LeftMainCard from "../components/LeftMainCard";
import RightMainCard from "../components/RightMainCard";

export default function Dashboard() {
  return (
    <Box sx={{ p: 2, height: "80vh" }}>
      <Grid 
        container 
        spacing={1} 
        sx={{
          flexDirection: { xs: "column", sm: "row" },
          height: "100%"
        }}
      >
        <Grid size={{ xs: 12, sm: 4 }} height="100%">
          <LeftMainCard />
        </Grid>
        <Grid size={{ xs: 12, sm: 8 }} height="100%">
          <RightMainCard/>
        </Grid>
      </Grid>
    </Box>
  );
}