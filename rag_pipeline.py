import os

def get_documents():

    documents = []

    docs_folder = "docs"

    if not os.path.exists(docs_folder):
        return documents

    for filename in os.listdir(docs_folder):

        if filename.endswith(".md"):

            filepath = os.path.join(
                docs_folder,
                filename
            )

            try:

                with open(
                    filepath,
                    "r",
                    encoding="utf-8"
                ) as file:

                    content = file.read()

                    documents.append(
                        {
                            "name": filename,
                            "content": content
                        }
                    )

            except Exception as e:
                print(f"Error reading {filename}: {e}")

    return documents