# TOTO — Project Todo List

---

## 🎬 Phase 0 — Finish Media Foundation *(current)*

### Media Database & Progress
- [x] Finish backend database schema for movies/shows (episodes, seasons, metadata)
- [ ] Add progress tracking endpoint — store watched position per item
- [ ] Add "continue watching" query — returns items with partial progress
- [ ] Add "mark as watched" endpoint
- [ ] Add last watched timestamp to each item
- [ ] Test progress persists correctly across MPV sessions

### Movie/Show Browser Frontend
- [ ] Update frontend to consume new database structure
- [ ] Build episode/season browser for shows (season selector → episode list)
- [ ] Add progress bar indicator on each movie/show card
- [ ] Add "continue watching" row at top of browser
- [ ] Add watched/unwatched visual state on cards
- [ ] Make sure opening an item resumes from saved progress

---

## 🎨 Phase 1 — UI Solidified

### Design Tokens & Theme
- [ ] Define all CSS custom properties in one root file
  - [ ] Background levels: `--bg-base`, `--bg-surface`, `--bg-elevated`
  - [ ] Text levels: `--text-primary`, `--text-secondary`, `--text-muted`
  - [ ] One accent colour + opacity variants (`--accent`, `--accent-20`, `--accent-40`)
  - [ ] Border: `--border` (single value used everywhere)
  - [ ] Spacing scale: 4, 8, 12, 16, 24, 32px as custom properties
  - [ ] Radius scale: `--radius-sm` (6px), `--radius-md` (12px), `--radius-lg` (20px)
- [ ] Pick and import your font (Geist or Inter recommended)
- [ ] Set `overscroll-behavior: none` on body
- [ ] Set background colour on html/body to match `--bg-base` so no white flash
- [ ] Switch all `vh` units to `dvh` throughout the app

### Shell Layout
- [ ] Build persistent `<StatusBar>` component — real time, connection status dot
- [ ] Build `<BottomNav>` — icon only, accent dot for active, max 5 tabs
- [ ] Build `<SlideIndicator>` — pill-style dots showing current horizontal position
- [ ] Wire Swiper to single source of truth index state in App
- [ ] Sync BottomNav tap → swiper navigate
- [ ] Sync swiper slide change → BottomNav active state updates
- [ ] Set Swiper easing curve to `cubic-bezier(0.25, 0.46, 0.45, 0.94)`
- [ ] Lock swiper to `100vw × 100dvh` per slide, no overflow

### Core Reusable Components
- [ ] Build `<WidgetCard>` — the shared card shell every widget uses
- [ ] Build `<SkeletonBlock>` — animated grey placeholder for loading states
- [ ] Build `<ProgressBar>` — used by media and potentially focus/other plugins
- [ ] Build `<IconButton>` — consistent tappable icon with haptic feedback
- [ ] Add `navigator.vibrate(10)` to all button press handlers
- [ ] Build `<DrawerSheet>` — reusable bottom/top drawer with drag-to-dismiss

### Dashboard Screen
- [ ] Build the CSS grid layout (2 column, named size classes)
- [ ] Build `Dashboard` component that reads from plugin registry and auto-places widgets
- [ ] Make widget tap navigate to that plugin's slide
- [ ] Handle odd widget counts gracefully (no orphaned gaps)
- [ ] Make dashboard the first/default slide

### Overlay System
- [ ] Build `<QuickControlsDrawer>` — swipe down from top, lives outside Swiper
- [ ] Build `<ScratchpadDrawer>` — swipe up from bottom, lives outside Swiper
- [ ] Add gesture detection for both (touch start/end on screen edges)
- [ ] Make both drag-to-dismiss
- [ ] Add dimmed backdrop behind open drawers

---

## 🧹 Phase 2 — Backend Cleanup

### Structure
- [ ] Audit current FastAPI file structure — identify anything that doesn't belong in its current location
- [ ] Separate concerns: routes, services, models into distinct folders per feature
- [ ] Create a `/core` folder for shared utilities (db connection, config, ws hub)
- [ ] Move all hardcoded config (paths, ports, API keys) into a `.env` file with `pydantic-settings`
- [ ] Add a `/health` endpoint that confirms all services are running

### WebSocket
- [ ] Build centralised `Hub` class if not already done (single WS connection for everything)
- [ ] Move all current ad-hoc WS logic into the Hub
- [ ] Add reconnection handling on the frontend — auto-reconnect if connection drops
- [ ] Add a visible connection status indicator (the dot in the StatusBar)
- [ ] Test WS stability over long periods (laptop sleep/wake etc.)

### MPV
- [ ] Audit current MPV IPC implementation — clean up any hacky polling
- [ ] Make sure all MPV events go through the Hub broadcaster
- [ ] Add proper error handling for when MPV isn't running
- [ ] Handle MPV process being killed externally (crash recovery)

### Error Handling Generally
- [ ] Add global exception handler in FastAPI that returns consistent error shape
- [ ] Make sure frontend handles API errors gracefully — no blank screens
- [ ] Add logging throughout backend (Python `logging` module, not print statements)

---

## 🔌 Phase 3 — Plugin Architecture

### Backend Plugin System
- [ ] Create `/plugins` folder structure
- [ ] Build `plugin_registry.py` — auto-discovers and loads plugin folders
- [ ] Define plugin `__init__.py` manifest shape (id, name, version, ws_events)
- [ ] Make registry auto-include each plugin's router with `/api/{plugin_id}` prefix
- [ ] Add `GET /api/plugins` endpoint — returns all registered plugin manifests
- [ ] Migrate existing media code into `/plugins/media/`
- [ ] Migrate existing weather code into `/plugins/weather/`
- [ ] Test auto-discovery works after migration

### Frontend Plugin System
- [ ] Create `/plugins` folder structure in React project
- [ ] Define TypeScript plugin contract (manifest shape, Widget, Page exports)
- [ ] Build `PluginRegistry.ts` — single file where plugins are imported and listed
- [ ] Build `<PluginSlide>` — generic wrapper the shell uses to render any plugin's Page
- [ ] Migrate existing media frontend into `/plugins/media/`
- [ ] Migrate existing weather frontend into `/plugins/weather/`
- [ ] Build central `useWS` hook for subscribing to WS events by name
- [ ] Build `useNavigateToPlugin(id)` hook for widgets to jump to their page
- [ ] Test that adding a new empty plugin appears in nav and dashboard automatically

---

## ✨ Phase 4 — New Features/Plugins

### Focus Plugin
- [ ] Backend: Pomodoro timer state endpoint (start, pause, reset, current state)
- [ ] Backend: Emit WS event on tick and on session complete
- [ ] Frontend Widget: Big countdown, session type label (focus/break), fills a `wide` slot
- [ ] Frontend Page: Full screen timer, task name input, start/pause/reset, session history

### System Stats Plugin
- [ ] Backend: Endpoint returning CPU %, RAM %, disk usage, active processes
- [ ] Backend: Poll every 5s and emit via WS
- [ ] Frontend Widget: CPU + RAM bars in a `small` slot
- [ ] Frontend Page: Full breakdown — all stats, list of killable processes

### Quick Notes / Scratchpad
- [ ] Backend: Simple file or SQLite backed notes store
- [ ] Backend: Endpoints for save, load, list notes
- [ ] Frontend: Wire up the ScratchpadDrawer (built in Phase 1) to actually save notes
- [ ] Frontend Page: List of saved notes, tap to expand, swipe to delete

### Dolphin/Games Plugin Cleanup
- [ ] Migrate existing Dolphin browser into plugin structure
- [ ] Add game artwork/thumbnail support if not already there
- [ ] Add last played timestamp per game
- [ ] Add "recently played" row at top of games browser

### Quick Controls Drawer Content
- [ ] Master volume slider (via PulseAudio/pipewire CLI)
- [ ] Kill current MPV instance button
- [ ] Kill current game button
- [ ] System stats summary (CPU/RAM at a glance)
- [ ] Allow plugins to register their own quick controls via manifest

---

## 🔒 Phase 5 — Polish & Robustness

- [ ] Add PWA manifest icons at all required sizes
- [ ] Test install-to-homescreen flow on your actual phone
- [ ] Test landscape orientation — lock to portrait if it looks bad
- [ ] Add skeleton screens to every plugin (no spinners anywhere)
- [ ] Audit all tap targets — minimum 44×44px on mobile
- [ ] Test on smallest screen you might use (375px width)
- [ ] Test laptop sleep/wake — does everything recover cleanly?
- [ ] Test what happens when FastAPI server isn't running — graceful frontend error state
- [ ] Add a simple "server offline" screen shown when WS can't connect