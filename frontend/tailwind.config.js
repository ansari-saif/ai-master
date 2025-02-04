/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        "cancerycolors-950": "#40140a",
        "cancerycolors-100": "#fdebd7",
        black: "#000",
        "cancerycolors-500": "#ef6c20",
        chocolate: "#d65205",
        "cancerycolors-600": "#e05316",
        gray: "#0a0a0a",
        "neutral-900": "#171717",
        navajowhite: {
          "100": "#f8d48d",
          "200": "rgba(248, 212, 141, 0.25)",
        },
        "neutral-300": "#d4d4d4",
        "neutral-200": "#e5e5e5",
        "neutral-400": "#a3a3a3",
        "neutral-700": "#404040",
        "neutral-100": "#f5f5f5",
        "neutral-50": "#fafafa",
        white: "#fff",
      },
      spacing: {},
      fontFamily: {
        manrope: "Manrope",
        figtree: "Figtree",
      },
      borderRadius: {
        "13xl": "32px",
        "mid-6": "17.6px",
        "3xl-5": "22.5px",
        "3xl-7": "22.7px",
      },
    },
    fontSize: {
      "5xl": "24px",
      lgi: "19px",
      base: "16px",
      "15xl": "34px",
      "17xl": "36px",
      "10xl": "29px",
      "3xl": "22px",
      lg: "18px",
      "11xl": "30px",
      "base-7": "16.7px",
      inherit: "inherit",
    },
    screens: {
      lg: {
        max: "1200px",
      },
      mq1125: {
        raw: "screen and (max-width: 1125px)",
      },
      mq1025: {
        raw: "screen and (max-width: 1025px)",
      },
      mq750: {
        raw: "screen and (max-width: 750px)",
      },
      mq450: {
        raw: "screen and (max-width: 450px)",
      },
    },
  },
  corePlugins: {
    preflight: false,
  },
};
