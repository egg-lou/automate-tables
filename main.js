const fs = require("fs");

const data = [
    {
        Topic: "Topic 1",
        Image: "![Image 1](./images/1.jpg)",
        Content: "Content 1",
    },
    {
        Topic: "Topic 2",
        Image: "![Image 2](./images/2.jpg)",
        Content: "Content 2",
    },
    {
        Topic: "Topic 3",
        Image: "![Image 3](./images/3.jpg)",
        Content: "Content 3",
    },
];

let markdownContent = "| Topic | Image | Content |\n| --- | --- | --- |\n";

data.forEach((row) => {
    markdownContent += `| ${row["Topic"]} | ${row["Image"]} | ${row["Content"]} |\n`;
});

const markdownName = "tables.md";

fs.writeFileSync(markdownName, markdownContent);

console.log(`File ${markdownName} created.`);
