#include <stdio.h>

struct Row {
    const char* Topic;
    const char* Image;
    const char* Content;
};

int main() {
    struct Row data[] = {
        {"Topic 1", "![Image 1](./images/1.jpg)", "Content 1"},
        {"Topic 2", "![Image 2](./images/2.jpg)", "Content 2"},
        {"Topic 3", "![Image 3](./images/3.jpg)", "Content 3"},
    };

    const char* markdownContent = "| Topic | Image | Content |\n| --- | --- | --- |\n";

    FILE* file = fopen("tables.md", "w");

    if (file != NULL) {
        fprintf(file, "%s", markdownContent);

        for (size_t i = 0; i < sizeof(data) / sizeof(data[0]); ++i) {
            fprintf(file, "| %s | %s | %s |\n", data[i].Topic, data[i].Image, data[i].Content);
        }

        fclose(file);
        printf("File tables.md created.\n");
    } else {
        fprintf(stderr, "Unable to open file tables.md\n");
    }

    return 0;
}
