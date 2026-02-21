/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}", // must match your files
  ],
  theme: {
    extend: {
      colors: {
        primary: "#FFCE1A",
        secondary: "#3b82f6",
        blackBG: "#F3F3F3",
        favorite: "#71717a",
      },
      fontFamily: {
        primary: ["Montserrat", "sans-serif"],
        secondary: ["Nunito Sans", "sans-serif"],
      },
    },
  },
  plugins: [],
};
