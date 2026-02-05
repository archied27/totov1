import { apiGet, apiPost } from "./client";

type GamesList = {
    [key: string]: string
}

export function play(filePath: string) {
  return apiPost("/dolphin/play", { filePath });
}

export function fullscreen() {
  return apiPost("/dolphin/fullscreen");
}

export function close() {
  return apiPost("/dolphin/close");
}

export function togglePlay() {
    return apiPost("/dolphin/playPause")
}

export function showGamesList(): Promise<GamesList> {
  return apiGet<GamesList>("/dolphin/gameList")
}