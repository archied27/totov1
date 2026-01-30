import { useEffect, useState } from "react";
import { getTitle } from "../api/mpv";

export default function NowPlaying() {
  const [title, setTitle] = useState<string | null>(null);

  useEffect(() => {
    const load = async () => {
      try {
        const data = await getTitle();
        setTitle(data.title);
      } catch {
        setTitle(null);
      }
    };

    load();
    const interval = setInterval(load, 10000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="now-playing">
      <p>{title ?? ""}</p>
    </div>
  );
}
