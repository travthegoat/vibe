/** @type {import('tailwindcss').Config} */
module.exports = {
    // NOTE: Update this to include the paths to all of your component files.
    content: ["./app/**/*.{js,jsx,ts,tsx}"],
    presets: [require("nativewind/preset")],
    theme: {
      extend: {
        colors: {
            primary: '#1877F2',
            secondary: '#F0F2F5',
            accent: '#00ff99'
        }
      },
    },
    plugins: [],
  }