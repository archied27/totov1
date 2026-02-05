import { Routes, Route } from "react-router-dom";
import { ThemeProvider, createTheme, CssBaseline } from "@mui/material";
import MpvBrowser from "./pages/MpvBrowser"
import Dashboard from "./pages/Dashboard"
import TopNav from "./components/NavBar";
import GameBrowser from "./pages/GameBrowser";

function App() {
  const theme = createTheme({
  palette: {
    mode: "dark",
    primary: {
      main: "#698194ff",
    },
  },
  shape: {
    borderRadius: 12,
  },
  });
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline/>
      <TopNav />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/movies" element={<MpvBrowser />}/>
        <Route path="/games" element={<GameBrowser />}/>
      </Routes>
    </ThemeProvider>
  );
}

export default App;
