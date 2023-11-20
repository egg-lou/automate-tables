#include <iostream>
#include <fstream>
#include <vector>
#include <string>

struct Row {
    std::string Topic;
    std::string Image;
    std::string Content;
};

int main() {
    std::vector<Row> data = {
        {"Topic 1", "![Image 1](./images/1.jpg)", "Content 1"},
        {"Topic 2", "![Image 2](./images/2.jpg)", "Content 2"},
        {"Topic 3", "![Image 3](./images/3.jpg)", "Content 3"},
    };

    std::string markdownContent = "| Topic | Image | Content |\n| --- | --- | --- |\n";

    for (const auto& row : data) {
        markdownContent += "| " + row.Topic + " | " + row.Image + " | " + row.Content + " |\n";
    }

    std::string markdownName = "tables.md";

    std::ofstream file(markdownName);

    if (file.is_open()) {
        file << markdownContent;
        file.close();
        std::cout << "File " << markdownName << " created." << std::endl;
    } else {
        std::cerr << "Unable to open file " << markdownName << std::endl;
    }

    return 0;
}
