import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";

// Corner dose counter for Danger Premium videos.
// The dose grows at `remPerHour` while the viewer "sits in the bowl";
// the bar fills against an average American's yearly dose.
export const DoseCounter: React.FC<{
  remPerHour: number;
  yearRem: number;
  limitRem: number;
}> = ({ remPerHour, yearRem, limitRem }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const dose = (frame / fps / 3600) * remPerHour;
  const appear = interpolate(frame, [0, 12], [0, 1], { extrapolateRight: "clamp" });
  const over = dose >= limitRem;
  const ratio = Math.min(dose / yearRem, 1);
  const times = dose / yearRem;
  const accent = over ? "#E53935" : "#F9C80E";
  return (
    <div
      style={{
        position: "absolute",
        top: 36,
        right: 40,
        width: 360,
        padding: "18px 22px",
        borderRadius: 18,
        background: "rgba(20,24,28,0.82)",
        border: `4px solid ${accent}`,
        color: "white",
        fontFamily: "Arial Black, Arial, sans-serif",
        opacity: appear,
      }}
    >
      <div style={{ fontSize: 26, letterSpacing: 2, color: accent }}>☢ YOUR DOSE</div>
      <div style={{ fontSize: 64, lineHeight: 1.05 }}>
        {dose.toFixed(2)} <span style={{ fontSize: 32 }}>rem</span>
      </div>
      <div style={{ marginTop: 10, height: 18, background: "#3a3f45", borderRadius: 9, overflow: "hidden" }}>
        <div style={{ width: `${ratio * 100}%`, height: "100%", background: accent }} />
      </div>
      <div style={{ marginTop: 8, fontSize: 22, fontFamily: "Arial, sans-serif" }}>
        {times < 1
          ? `${Math.round(times * 100)}% of a normal year`
          : `${times.toFixed(1)}× a normal year`}
        {over ? " · OVER THE YEARLY LIMIT" : ""}
      </div>
    </div>
  );
};
