import { apiGet, apiPost } from "./client";

export function getTitle() {
  return apiGet<{ title: string | null }>("/mpv/title");
}

export function play(filePath: string) {
  return apiPost("/mpv/play", { filePath });
}

export function fullscreen() {
  return apiPost("/mpv/fullscreen");
}

export function close() {
  return apiPost("/mpv/close");
}

export function togglePlay() {
    return apiPost("/mpv/togglePause")
}

export function getPause(): Promise<{pause: boolean}> {
  return apiGet<{pause: boolean}>("/mpv/getPause");
}