import { apiGet, apiPost } from "./client";

type MovieSummary = {
  title: string,
  poster_path: string
  file_path: string
}

type MovieDetails = {
  [key: string]: MovieSummary
}

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

export function showMovieList(): Promise<MovieDetails> {
  return apiGet<MovieDetails>("/mpv/movieListPlus");
}

export function getCurrentDetails(): Promise<MovieSummary>{
  return apiGet<MovieSummary>("/mpv/getCurrentDetails");
}

export function isMpvOn() {
  return apiGet<{status: boolean}>("/mpv/isOn");
}

export function showShowList(): Promise<MovieDetails> {
  return apiGet<MovieDetails>("/mpv/showListPlus");
}