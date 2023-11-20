import java.io.FileWriter;
import java.io.IOException;

class Row {
    String Topic;
    String Image;
    String Content;

    public Row(String topic, String image, String content) {
        Topic = topic;
        Image = image;
        Content = content;
    }
}

public class Main {
    public static void main(String[] args) {
        Row[] data = {
            new Row("Topic 1", "![Image 1](./images/1.jpg)", "Content 1"),
            new Row("Topic 2", "![Image 2](./images/2.jpg)", "Content 2"),
            new Row("Topic 3", "![Image 3](./images/3.jpg)", "Content 3")
        };

        StringBuilder markdownContent = new StringBuilder("| Topic | Image | Content |\n| --- | --- | --- |\n");

        for (Row row : data) {
            markdownContent.append(String.format("| %s | %s | %s |\n", row.Topic, row.Image, row.Content));
        }

        String markdownName = "tables.md";

        try (FileWriter fileWriter = new FileWriter(markdownName)) {
            fileWriter.write(markdownContent.toString());
            System.out.println("File " + markdownName + " created.");
        } catch (IOException e) {
            System.err.println("Unable to open file " + markdownName);
            e.printStackTrace();
        }
    }
}
