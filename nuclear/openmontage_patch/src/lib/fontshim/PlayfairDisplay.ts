// Offline shim: the render container cannot reach fonts.gstatic.com.
export const loadFont = (..._args: unknown[]) => ({ fontFamily: "'Playfair Display', Georgia, serif" });
