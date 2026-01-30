import Remote from "./Remote";
import NowPlaying from "./NowPlaying";

export default function MpvOverlay() {
    return (<div className="mpv-overlay">
        <NowPlaying/>
        <Remote/>
    </div>)
}