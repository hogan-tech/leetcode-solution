import fs from "fs";
import fetch from "node-fetch";

const username = "hogantech"; 
const url = `https://leetcard.jacoblin.cool/${username}?ext=heatmap`;

const outputPath = "./assets/leetcode.svg";

async function updateLeetCodeCard() {
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const svg = await response.text();
    fs.writeFileSync(outputPath, svg);
    console.log("LeetCode stats card updated successfully!");
  } catch (err) {
    console.error("Failed to update LeetCode stats:", err);
  }
}

updateLeetCodeCard();
