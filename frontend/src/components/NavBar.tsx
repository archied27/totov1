import * as React from "react";
import BottomNavigation from "@mui/material/BottomNavigation";
import BottomNavigationAction from "@mui/material/BottomNavigationAction";
import Paper from "@mui/material/Paper";

import DashboardIcon from "@mui/icons-material/Dashboard";
import MovieIcon from "@mui/icons-material/Movie";

import { useLocation, useNavigate } from "react-router-dom";

export default function TopNav() {
  const location = useLocation();
  const navigate = useNavigate();

  return (
    <Paper
      elevation={3}
      sx={{
        position: "sticky",
        top: 0,
        zIndex: 1100,
      }}
    >
      <BottomNavigation
        value={location.pathname}
        onChange={(event, newValue) => {
          navigate(newValue);
        }}
        showLabels
      >
        <BottomNavigationAction
          label="Dashboard"
          value="/"
          icon={<DashboardIcon />}
        />

        <BottomNavigationAction
          label="Movies"
          value="/movies"
          icon={<MovieIcon />}
        />
      </BottomNavigation>
    </Paper>
  );
}
